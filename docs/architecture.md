# Documentation Agent Architecture

Automated documentation generator that produces API references, architecture diagrams, onboarding guides, changelogs, and inline documentation from source code analysis with automatic staleness detection and update suggestions.

## Domain Tools

- **generate_api_docs**: Generate OpenAPI/Swagger documentation from source code
- **generate_architecture_diagram**: Generate architecture diagram from codebase analysis
- **generate_changelog**: Generate changelog from git commit history
- **detect_stale_docs**: Find documentation that is out of sync with code
- **generate_onboarding_guide**: Generate developer onboarding documentation
- **generate_docstrings**: Generate docstrings for undocumented functions