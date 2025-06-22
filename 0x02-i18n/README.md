# 0x02. i18n

## Project Overview
This project introduces internationalization (i18n) concepts and demonstrates how to build a multilingual backend application. You will implement language selection, translation management, and locale-aware responses using Python and Flask.

## Learning Objectives
- Understand the principles of internationalization and localization.
- Implement language selection and translation in a web application.
- Manage translation files and message catalogs.
- Design endpoints that respond to user language preferences.

## Requirements
- Python 3.x
- Flask
- Babel (for message extraction and translation)
- Any additional dependencies listed in `requirements.txt`

## Project Structure
- `app.py` / `*-app.py` – Flask applications demonstrating i18n features.
- `babel.cfg` – Babel configuration for message extraction.
- `messages.pot` – Template for translation messages.
- `translations/` – Directory containing language-specific message catalogs.
- `templates/` – Jinja2 HTML templates for different locales.
- `README.md` – Project documentation.

## Usage
1. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```
2. Extract messages and compile translations:
   ```zsh
   pybabel extract -F babel.cfg -o messages.pot .
   pybabel init -i messages.pot -d translations -l fr
   pybabel compile -d translations
   ```
3. Run the application:
   ```zsh
   python 0-app.py
   ```
4. Access the app and test language switching via query parameters or headers.

## Example
```
GET /?locale=fr
```
Returns the homepage in French if translations are available.
