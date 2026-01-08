# SA Legal Prompting Elite - Copilot Instructions

## Project Overview

This is a **South African legal AI prompting platform** with two UI frontends:
- **Marimo app** (`app.py`): Run with `python -m marimo run app.py`
- **Streamlit app** (`streamlit_app.py`): Run with `streamlit run streamlit_app.py`

Both apps import from the `core/` module which contains domain knowledge for SA legal practice.

## Architecture

```
app.py              # Marimo reactive notebook interface
streamlit_app.py    # Streamlit web UI (primary, feature-rich)
core/
├── __init__.py                 # Re-exports all public APIs with aliases
├── advanced_frameworks.py      # Prompting frameworks (RICE, ABCDE, etc.)
├── specialist_courts.py        # SA court/tribunal definitions
├── sa_legislation.py           # Key SA legislation database
├── legal_ethics.py             # AI ethics guidelines & risk assessment
├── practice_area_prompts.py    # Practice-specific prompt templates
├── document_templates.py       # Legal document templates
└── workflow_pipelines.py       # Multi-step legal workflows
```

## Core Module Pattern

All `core/` modules follow identical patterns:

### 1. Data Classes with `@dataclass`
```python
@dataclass
class PromptingFramework:
    name: str
    acronym: str
    category: FrameworkCategory  # Always use Enum categories
    components: List[Dict[str, str]]
    # ... domain-specific fields
```

### 2. Category Enums
Every module defines Enums for categorization (e.g., `FrameworkCategory`, `CourtCategory`, `LegislationCategory`).

### 3. Module-Level Collections
Data is stored in uppercase module-level variables:
- `ALL_FRAMEWORKS`, `ALL_SPECIALIST_COURTS`, `ALL_LEGISLATION`, `ALL_GUIDELINES`, etc.

### 4. Generator Functions
Standard function naming: `generate_*_prompt()`, `get_*_by_category()`, `assess_*_risk()`

## Adding New Domain Content

When adding new legal frameworks, courts, or legislation:

1. **Create dataclass instance** following existing patterns in the relevant module
2. **Add to the `ALL_*` list** at module level
3. **Exports**: Update `core/__init__.py` if adding new public functions

Example - adding a new framework in `advanced_frameworks.py`:
```python
NEW_FRAMEWORK = PromptingFramework(
    name="...",
    acronym="...",
    category=FrameworkCategory.STRUCTURAL,  # Use existing enum
    # ... follow existing framework structure
)

# Add to collection:
ALL_FRAMEWORKS = [RICE_FRAMEWORK, ..., NEW_FRAMEWORK]
```

## Key Conventions

- **SA Legal Citations**: Use SAFLII neutral citation format `[Party] [Year] ZACC/ZASCA/ZALC [Number]`
- **Legislation References**: Always include Act number (e.g., "Labour Relations Act 66 of 1995")
- **Risk Levels**: Use `RiskLevel` enum: `HIGH`, `MEDIUM`, `LOW`, `PROHIBITED`
- **Practice Areas**: Use `PracticeArea` enum for categorization consistency

## Streamlit Session State

`streamlit_app.py` uses extensive session state initialized in `init_session_state()`:
- `prompt_history`, `favorites`, `analytics` for user tracking
- `chat_messages`, `chat_context` for AI chat assistant
- `builder_*` keys for Smart Prompt Builder feature

## Environment Variables

The AI chat assistant uses **OpenRouter AI**. Set your API key:
```bash
OPENROUTER_API_KEY=your_key_here
```

## Dependencies

- `streamlit` - Web UI framework (primary app)
- `marimo>=0.18.4` - Alternative reactive notebook interface
- Standard library only in `core/` (no external dependencies)

## Running the App

```bash
streamlit run streamlit_app.py
```

## Testing Changes

Validate imports after modifying `core/`:
```bash
python -c "from streamlit_app import *; print('✅ All imports successful!')"
```

## Data Maintenance

All legal content (frameworks, courts, legislation, cases) is **manually curated** in the `core/` modules. When updating:
- Verify SAFLII citations are current and accessible
- Cross-reference legislation against official Government Gazette
- Update `landmark_cases` and `key_cases` lists as new judgments are handed down
