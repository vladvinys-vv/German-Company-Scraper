# German Company Scraper

Web scraping and directory extraction pipeline for German company registries and corporate registers.

## 🇩🇪 German Government API Integrations

This scraper integrates with official German public APIs for comprehensive company data:

| API | Purpose | Auth | Integration |
|---|---|---|---|
| [OpenRegister (Handelsregister)](https://openregister.de/api) | 4M+ German companies: ownership chains, financials, official registry documents. SDKs: Python/TS/Go. Zapier/n8n/MCP. | `apiKey` | Primary data source for company enrichment |
| [Handelsregister.ai](https://handelsregister.ai/) | Modern Handelsregister API: verified company data, financial KPIs, shareholders, insolvency notices. CRM sync (Salesforce, HubSpot, Pipedrive), bulk export. | `apiKey` | Enriched company verification |
| [OffeneRegister (Bulk)](https://github.com/B2Trust-Infrastructure/registry-api-examples/tree/main/germany-offeneregister) | ~5.3M companies, JSONL bulk dump (1GB compressed). Open Knowledge Foundation Germany. | No | Initial dataset seeding |
| [Bundestag DIP API](https://dip.bundestag.de/ueber-dip/hilfe/api) | Laws, proceedings, persons, lobby register, party donations. | No | Legal compliance tracking |
| [Bundestag Live API](https://bundestag.api.bund.dev/) | Real-time plenary sessions, committees, agenda. | No | Legislative monitoring |
| [Bundespuls](https://bundespuls.de/) | Real-time Bundestag pulse: DIP, lobby register, donations. WebSocket + REST. | No | Live legislative updates |
| [OpenPlz API](https://openplzapi.org/de/Localities) | Free German postal codes and cities database. | No | Address validation & autocomplete |
| [Feiertage API](https://feiertage-api.de/api/?jahr=2026) | Official holidays by Bundesland. | No | Scheduling optimizations |
| [Gesetze im Internet](https://www.gesetze-im-internet.de/) | BGB, HGB, DSGVO structured legal texts. | No | Legal reference for data handling |
| [BrightSky / DWD](https://api.brightsky.dev/) | German Weather Service forecasts & historical data. | No | Weather-aware operations |

> **Note:** APIs marked with `apiKey` require environment variables in `.env`. MCP-ready APIs work with Model Context Protocol agents.

## 🤖 AI Agent Skills Integration

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

### Verification Gates (Required per Commit)
```bash
pytest -q && make verify
# Secret scanning
npx -y gitleaks detect --no-git -v
```

## Guidelines
See [AGENTS.md](AGENTS.md) and [HANDOFF.md](HANDOFF.md) for architectural and development guidelines.

## Architecture

### Pipeline Stages
1. **Source Discovery** — Identify targets from Handelsregister, OpenRegister, OffeneRegister
2. **Extraction** — Parse HTML, JSON, PDF from official sources
3. **Enrichment** — Cross-reference with OpenRegister, Handelsregister.ai, Bundestag APIs
4. **Validation** — Verify data integrity, deduplicate, normalize
5. **Storage** — Persist to structured format (JSON, CSV, SQLite, PostgreSQL)
6. **Export** — Generate reports, feeds, API endpoints

### Data Models
- Company: HRB/HRA number, name, legal form, address, registration court
- Officers: Geschäftsführer, Vorstände, legal representatives
- Financials: Revenue, employees, balance sheet data (from Bundesanzeiger)
- Ownership: Shareholders, parent companies, UBO chains
- Events: Insolvency, mergers, address changes, capital measures

## Quick Start

```bash
# Clone and setup
git clone https://github.com/vladvinys-vv/German-Company-Scraper.git
cd German-Company-Scraper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add OPENREGISTER_API_KEY, HANDELSREGISTER_API_KEY

# Run scraper
python -m src.scraper --source openregister --limit 100
```

## License
Private - All rights reserved