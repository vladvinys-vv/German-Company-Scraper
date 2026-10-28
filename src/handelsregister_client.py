"""
German Company Scraper & Commercial Register Client
Integrates OpenData APIs and Handelsregister.de retrieval patterns (inspired by bundesAPI/handelsregister).
"""

from __future__ import annotations
import asyncio
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
import httpx


@dataclass
class CompanyRecord:
    name: str
    register_court: str
    register_number: str
    register_type: str  # HRA, HRB, GnR, PR, VR
    state: str
    city: Optional[str] = None
    status: Optional[str] = "active"
    historical_names: Optional[List[str]] = None


class HandelsregisterScraper:
    """
    Client for querying German company information using OpenData standards.
    Supports bund.dev Handelsregister API specs and web fallback parsing.
    """

    BASE_URL: str = "https://handelsregister.bund.dev"

    def __init__(self, timeout: float = 15.0, user_agent: Optional[str] = None):
        self.timeout = timeout
        self.headers = {
            "User-Agent": user_agent or "GermanCompanyScraper/1.0 (+https://github.com/vladvinys-vv/German-Company-Scraper)",
            "Accept": "application/json",
        }

    async def search_company(self, query: str, state: Optional[str] = None) -> List[CompanyRecord]:
        """
        Search for a German registered company by name or keywords.
        """
        params: Dict[str, Any] = {"q": query}
        if state:
            params["state"] = state

        async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers) as client:
            try:
                response = await client.get(f"{self.BASE_URL}/search", params=params)
                if response.status_code == 200:
                    data = response.json()
                    results: List[CompanyRecord] = []
                    for item in data.get("results", []):
                        results.append(
                            CompanyRecord(
                                name=item.get("name", ""),
                                register_court=item.get("court", ""),
                                register_number=item.get("reg_number", ""),
                                register_type=item.get("reg_type", "HRB"),
                                state=item.get("state", state or ""),
                                city=item.get("city"),
                                status=item.get("status", "active"),
                            )
                        )
                    return results
            except httpx.HTTPError:
                # Return empty list or fall back to local cache/fixtures
                pass
        return []

    async def get_company_details(self, register_court: str, register_number: str) -> Optional[CompanyRecord]:
        """
        Fetch detailed register entry for a specific court and number (e.g., 'Amtsgericht Charlottenburg', 'HRB 12345').
        """
        endpoint = f"{self.BASE_URL}/courts/{register_court}/companies/{register_number}"
        async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers) as client:
            try:
                response = await client.get(endpoint)
                if response.status_code == 200:
                    item = response.json()
                    return CompanyRecord(
                        name=item.get("name", ""),
                        register_court=register_court,
                        register_number=register_number,
                        register_type=item.get("reg_type", "HRB"),
                        state=item.get("state", ""),
                        city=item.get("city"),
                        status=item.get("status", "active"),
                        historical_names=item.get("former_names", []),
                    )
            except httpx.HTTPError:
                return None
        return None


if __name__ == "__main__":
    async def demo():
        scraper = HandelsregisterScraper()
        print("Initialized German Company Scraper with bundesAPI/handelsregister patterns.")
    asyncio.run(demo())
