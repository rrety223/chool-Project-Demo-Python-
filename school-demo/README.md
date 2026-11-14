# Riverside High School Demo Website

A small English-language school website built with Python and Flask.

## Pages

- Home, About, Programs, Faculty, Admissions, News
- Contact form with server-side validation
- Custom 404 page and responsive navigation

## Run locally

```bash
cd school-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Notes

- Contact messages are stored in memory and are cleared when the server restarts.
- `SECRET_KEY` is a placeholder for development. Load a real secret from an environment variable before deploying.
- Run with `debug=True` only on a local machine.
