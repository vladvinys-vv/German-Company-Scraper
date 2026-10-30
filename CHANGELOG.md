# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Handelsregister Open Data Scraper (`src/handelsregister_client.py`)**: Asynchronous `httpx` client querying German commercial register records with structured `CompanyRecord` dataclass mapping (court, register number, register type HRA/HRB/GnR/PR/VR, state, former names).
- **Automated Tests (`tests/test_handelsregister.py`)**: Unit and mocked integration tests verifying company search, detail retrieval, and error resilience.
- **MIT License**: Added official MIT license.

### Changed
- **Documentation**: Enhanced `README.md` with German register types (HRA, HRB, GnR, PR, VR) and Open Data API ecosystem.
