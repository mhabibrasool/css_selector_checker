# CSS Selector Checker

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/css-selector-checker.svg)](https://pypi.org/project/css-selector-checker/)

A lightweight Python CLI tool that checks for the presence and count of CSS selectors on any public webpage. Powered by [Playwright](https://playwright.dev/python/).

---

## 📦 Features

- Accepts any public URL and list of CSS selectors.
- Launches a headless Chromium browser using Playwright.
- Logs which selectors are found and how many elements match.
- Output saved both to terminal and `scraper.log` file.
- Simple to install, run, and extend.

---

## 🚀 Installation

### Option 1: Install via `pip` (after publishing to PyPI)

```bash
pip install css-selector-checker
playwright install
```
### Option 2: Install manually
```bash
git clone https://github.com/your-username/css-selector-checker.git
cd css-selector-checker
```

# Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

# Install dependencies
```bash
pip install .
playwright install
```

### Usage
# Run from CLI
```bash
css_selector_checker
```

You will be prompted to:
```bash
Enter the URL to test.
Enter one or more CSS selectors (comma-separated).
```
like this:
```bash
Welcome to CSS selector checking. Please enter the url you wish to search selectors: https://example.com
Enter the selector you wish to find ( if more than one selector, separate it by comma) : h1, .container, #main
```

