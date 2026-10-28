# German-Company-Scraper — Project Handoff

## Current Status (October 2026)
- **Unified Location:** Standardized at `C:\Users\vladv\projects\German-Company-Scraper`.
- **Default Branch:** `main` (clean, synchronized with `origin/main`).
- **Open-Source Integration:** Integrated `bundesAPI/handelsregister` architecture with asynchronous `httpx` client in `src/handelsregister_client.py`.
- **Hygiene & Standards:**
  - Modern Python 3.11+ type annotations and dataclass models.
  - Comprehensive `README.md`, `requirements.txt`, `AGENTS.md`, and this `HANDOFF.md`.

## Quick Start
```bash
pip install -r requirements.txt
python src/handelsregister_client.py
```

## Verification Commands
```bash
python -m py_compile src/handelsregister_client.py
```
