# German Company Scraper (Handelsregister & Unternehmensregister)

Modern Python scraping and data extraction pipeline for German corporate registries (`Handelsregister.de`, `Unternehmensregister.de`, `Bundesanzeiger`), integrating open data standards inspired by [`bundesAPI/handelsregister`](https://github.com/bundesAPI/handelsregister) and `bund.dev`.

---

## 1. Key Capabilities
- **Handelsregister Search:** Query companies across German federal states by name, city, register court (`Amtsgericht`), and register number (`HRA`, `HRB`, `GnR`, `PR`, `VR`).
- **Structured Schema:** Exports strongly typed models (`CompanyRecord`) with Pydantic / Dataclasses.
- **Open Data & API Integration:**
  - `bund.dev` / `bundesAPI/handelsregister` OpenAPI specifications.
  - Integration readiness for North Data, OpenRegister, and ELSTER company lookup.
- **Resilient Retrieval:** Asynchronous `httpx` client with exponential backoff, user-agent rotation, and rate-limiting to prevent IP restrictions.

---

## 2. 🇩🇪 German Government & Registry API Integrations

This scraper integrates with official German public APIs for comprehensive company data:

| API | Purpose | Auth | Integration |
|---|---|---|---|
| [OpenRegister (Handelsregister)](https://openregister.de/api) | 4M+ German companies: ownership chains, financials, official registry documents. SDKs: Python/TS/Go. Zapier/n8n/MCP. | `apiKey` | Primary data source for company enrichment |
| [Handelsregister.ai](https://handelsregister.ai/) | Modern Handelsregister API: verified company data, financial KPIs, shareholders, insolvency notices. CRM sync, bulk export. | `apiKey` | Enriched company verification |
| [OffeneRegister (Bulk)](https://github.com/B2Trust-Infrastructure/registry-api-examples/tree/main/germany-offeneregister) | ~5.3M companies, JSONL bulk dump (1GB compressed). Open Knowledge Foundation Germany. | No | Initial dataset seeding |
| [Bundestag DIP API](https://dip.bundestag.de/ueber-dip/hilfe/api) | Laws, proceedings, persons, lobby register, party donations. | No | Legal compliance tracking |
| [Bundestag Live API](https://bundestag.api.bund.dev/) | Real-time plenary sessions, committees, agenda. | No | Legislative monitoring |
| [OpenPlz API](https://openplzapi.org/de/Localities) | Free German postal codes and cities database. | No | Address validation & autocomplete |
| [Feiertage API](https://feiertage-api.de/api/?jahr=2026) | Official holidays by Bundesland. | No | Scheduling optimizations |
| [Gesetze im Internet](https://www.gesetze-im-internet.de/) | BGB, HGB, DSGVO structured legal texts. | No | Legal reference for data handling |

---

## 3. Register Types Reference (Germany)
| Register Type | German Abbreviation | Entity Types |
|---|---|---|
| **Abteilung A** | `HRA` | Einzelkaufleute (e.K.), Offene Handelsgesellschaften (oHG), Kommanditgesellschaften (KG, GmbH & Co. KG) |
| **Abteilung B** | `HRB` | Gesellschaften mit beschränkter Haftung (GmbH, UG haftungsbeschränkt), Aktiengesellschaften (AG) |
| **Genossenschaftsregister** | `GnR` | Eingetragene Genossenschaften (eG) |
| **Partnerschaftsregister** | `PR` | Partnerschaftsgesellschaften (PartG) für Freie Berufe |
| **Vereinsregister** | `VR` | Eingetragene Vereine (e.V.) |

---

## 4. Quick Start

### Installation
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### Usage Example
```python
import asyncio
from src.handelsregister_client import HandelsregisterScraper

async def main():
    scraper = HandelsregisterScraper()
    results = await scraper.search_company("Siemens", state="Bayern")
    for company in results:
        print(f"{company.name} | {company.register_court} {company.register_number} ({company.status})")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 5. 🤖 AI Agent Skills Integration

### Recommended Skill Collections
```bash
# Skill management
npm install -g @skillkit/cli && skillkit init
skillkit recommend

# Python / Web Scraping / Data Pipeline skills
npx skills add seb1n/awesome-ai-agent-skills --skill python,scraping,pipeline
npx skills add alirezarezvani/claude-skills --skill scraping,data

# Security scan before install
npm install -g @nvidia/skillspector
skillspector scan <repo-url>
```

### MCP Server Configuration
Add to agent config (`.claude/settings.json`, `kilo.jsonc`):
```json
{
  "mcpServers": {
    "openregister": "openregister/openregister-sdk",
    "browser": "browser-use/browser-use",
    "bundestag": "local-bundestag-api"
  }
}
```

### Subagent Delegation (Kilo Multi-Agent)
Use native `task(agent="...", ...)` for specialized work:
- `task(agent="architect", ...)` — Before new modules, DB schema changes, API contracts
- `task(agent="debugger", ...)` — Test failures, scraping errors, parsing issues
- `task(agent="revisor", ...)` — Pre-commit: security scan, coverage, diff analysis

---

## 6. Architecture & Guidelines
For detailed agent directives and maintenance standards, see [AGENTS.md](AGENTS.md) and [HANDOFF.md](HANDOFF.md).

## License
MIT License — see [LICENSE](LICENSE) for details.
