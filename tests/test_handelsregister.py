import pytest
import httpx
from unittest.mock import AsyncMock, patch
from src.handelsregister_client import HandelsregisterScraper, CompanyRecord


def test_company_record_dataclass():
    record = CompanyRecord(
        name="Test GmbH",
        register_court="Amtsgericht Charlottenburg",
        register_number="HRB 12345",
        register_type="HRB",
        state="Berlin",
        city="Berlin",
        status="active",
    )
    assert record.name == "Test GmbH"
    assert record.register_court == "Amtsgericht Charlottenburg"
    assert record.register_number == "HRB 12345"
    assert record.register_type == "HRB"
    assert record.status == "active"


def test_scraper_initialization():
    scraper = HandelsregisterScraper(timeout=20.0, user_agent="CustomAgent/1.0")
    assert scraper.timeout == 20.0
    assert "CustomAgent/1.0" in scraper.headers["User-Agent"]
    assert scraper.headers["Accept"] == "application/json"


@pytest.mark.asyncio
async def test_search_company_mocked():
    scraper = HandelsregisterScraper(timeout=0.1)
    fake_payload = {
        "results": [
            {
                "name": "Musterfirma GmbH",
                "court": "Amtsgericht München",
                "reg_number": "HRB 9999",
                "reg_type": "HRB",
                "state": "Bayern",
                "city": "München",
                "status": "active",
            }
        ]
    }
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = httpx.Response(200, json=fake_payload, request=httpx.Request("GET", "https://handelsregister.bund.dev/search"))
        results = await scraper.search_company("Musterfirma", state="Bayern")
        assert len(results) == 1
        assert results[0].name == "Musterfirma GmbH"
        assert results[0].register_number == "HRB 9999"
        assert results[0].city == "München"
