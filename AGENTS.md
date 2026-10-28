# German-Company-Scraper - Agent Guidelines

## 1. Overview
German-Company-Scraper is a repository managed by vladvinys-vv.
Standardized on default branch main.
Web scraping and directory extraction pipeline for German company registries and corporate registers.

## 2. Directory Layout
- README.md: Project description.
- .gitignore: Standard exclusion rules.
- AGENTS.md: Guidelines for AI agents and automated tools.
- HANDOFF.md: Project status and handoff notes.

## 3. Workflow Rules
- Target branch is main.
- Ensure clean commits and avoid committing sensitive credentials or temporary files.

## AI Agent Skills & MCP Integration (2026)

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
Configure in agent settings (`.claude/settings.json`, `kilo.jsonc`):
```json
{
  "mcpServers": {
    "openregister": "openregister/openregister-sdk",
    "browser": "browser-use/browser-use",
    "bundestag": "local-bundestag-api"
  }
}
```

### German API Integration Points
| API | MCP/REST | Use Case | Config |
|---|---|---|---|
| OpenRegister | REST + SDK | Primary data source for company enrichment | `OPENREGISTER_API_KEY` |
| Handelsregister.ai | REST | Enriched company verification | `HANDELSREGISTER_API_KEY` |
| OffeneRegister | Bulk download | Initial dataset seeding | No auth |
| Bundestag DIP | REST | Legal compliance tracking | No auth |
| OpenPlz | REST | Address validation | No auth |
| Feiertage | REST | Scheduling optimizations | No auth |

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