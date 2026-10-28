# Google Jules Rules for German-Company-Scraper

## Role & Objectives
You are Google Jules assisting with **German-Company-Scraper**, an asynchronous client and parsing tool for German commercial registers (Handelsregister) and official corporate open data (bund.dev / bundesAPI).

## Core Principles & Domain Standards
1. **German Corporate Registry Formats:**
   - Accurately parse and normalize German commercial register numbers (HRA, HRB, GnR, PR, VR).
   - Normalize register courts (Amtsgerichte) across all German federal states (Bundesländer).
2. **Polite Ingestion & Rate Limiting:**
   - Adhere to rate limits and exponential backoff to avoid overloading public endpoints.
   - Use mock responses or cached fixtures in automated unit tests.
3. **Data Integrity & Legal Compliance (DSGVO):**
   - Strictly process publicly accessible business data. Never scrape or persist private, non-commercial personal information without a lawful basis.
4. **Code Quality & Testing:**
   - All tests in `tests/` must pass (`pytest -v`).
   - Use asynchronous I/O (`httpx`, `asyncio`) for scalable querying.
