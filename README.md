## Python Data Science Project Template

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/joseparreiras/python-project?style=social)](https://github.com/joseparreiras/python-project/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/joseparreiras/python-project?style=social)](https://github.com/joseparreiras/python-project/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/joseparreiras/python-project)](https://github.com/joseparreiras/python-project/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/joseparreiras/python-project)](https://github.com/joseparreiras/python-project/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/joseparreiras/python-project)](https://github.com/joseparreiras/python-project/pulls)

Opinionated template for Python data science projects with clean structure, testing, logging, and documentation conventions.

### Features
- **Structured layout** for code, data, tests, images, and logs
- **PEP 8** style enforced with Black (88 chars) and isort
- **Type hints** and docstrings everywhere
- **pytest** for unit tests and fixtures
- **Config-first** design (`src/config/`)
- **Utilities** in `src/utils/` (e.g., logger setup)
- **Reproducible environment** (Conda; helper script in `scripts/`)
- **Data outputs** organized under `data/` and plots under `images/`
- VSCode **Tasks** for easy implementation

---

## Project Structure
```text
python-project/
├─ data/
│  ├─ raw/            # Raw, immutable data dumps
│  └─ out/            # Cleaned/processed data, features, intermediate outputs
├─ images/            # Generated plots and figures
├─ logs/              # Log files
├─ scripts/
│  └─ create_python_environment.sh  # Optional environment bootstrap
├─ src/
│  ├─ config/         # Settings, plotting config, configuration utilities
│  ├─ utils/          # Reusable helpers (e.g., logging)
│  └─ __init__.py
├─ tests/             # pytest-based unit tests
├─ .gitignore
├─ .pytest.ini        # pytest configuration 
├─ requirements.txt  
└─ README.md
```

---

## Quickstart

### 1) Clone the current repo onto the active directory
```bash
git clone https://github.com/joseparreiras/python-project
```

### 2) Create and activate environment (Conda recommended)

Run VSCode task "Setup Python Environment" using the Command Palette or:

```bash
# Option A: use the provided helper script
bash scripts/create_python_environment.sh <env_name> <python_version> 

# Option B: manual setup (example)
conda create -y -n <env_name> python=<python_version> 
conda activate <env_name>

# If you maintain environment.yml, install here
```

### 3) Install dependencies
```bash
# Install development tools and dependencies
pip install -r requirements.txt

# If using a pyproject.toml/setup.cfg later, you can switch to:
# pip install -e .
```

---

## Development Workflow

### Code style and quality
- Format with Black (88-char line length)
- Sort imports with isort
- Use type hints throughout and run mypy when applicable
- Prefer absolute imports; avoid wildcard imports

Run "Python: All Qualiy Checks" from VSCode Tasks menu (using the Command Pallete) or execute

```bash
# Format
black .
isort .

# Lint (examples)
ruff check .

# Type check (if configured)
mypy src
```

### Testing
- Place tests under `tests/` with descriptive names
- Use fixtures for test data
- Aim for high coverage and cover edge cases
- pytest is configured to only discover tests in `tests/` directory (see `pytest.ini` or `pyproject.toml`)

```bash
pytest -q                                      # Run all tests quietly
pytest -q --maxfail=1                         # Stop on first failure
pytest -q -k "test_name"                      # Run specific test pattern
pytest -q tests/test_specific.py              # Run specific test file
pytest -q -m "not slow"                       # Skip tests marked as slow
pytest -q --cov=src --cov-report=term-missing # With coverage (requires pytest-cov)
```

### Logging
- Use the shared logger from `src/utils/setup_logger.py`
- Store log files under `logs/`

Minimal example:
```python
from src.utils.setup_logger import get_logger

logger = get_logger(__name__)
logger.info("Hello from the template!")
```

---

## Configuration
- Keep configuration in `src/config/` (e.g., `settings.py`, `plot_config.py`)
- Prefer reading settings from a single place and passing them into functions explicitly
- Add docstrings for all public functions/classes and document any data transformations

---

## Data and Artifacts
- Place raw, immutable data in `data/raw/`
- Write processed data, features, and outputs to `data/out/`
- Save generated plots and figures to `images/`

When saving artifacts, include metadata in filenames where helpful (date, version, parameters) and log the steps using the shared logger.

---

## Documentation
- Use Sphinx for documentation (recommended)
- Ensure public APIs include docstrings with types and examples
- Keep the README up to date with setup and usage

---

## Suggested Project Conventions
- Small, focused functions with single responsibility
- Meaningful names for variables and functions
- Validate inputs/outputs and handle errors with actionable messages
- Keep plotting code separate from data processing

---

## Common Commands (cheatsheet)
```bash
# Format & lint
black . && isort . && ruff check .

# Tests
pytest -q

# Type checking
mypy src
```

---

## License
Add your chosen license here (e.g., MIT, Apache-2.0).

