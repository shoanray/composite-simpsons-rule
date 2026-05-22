# Composite Simpson's 1/3 Rule
### PIT Project — Numerical Methods Online Calculator

A Flask web application implementing the **Composite Simpson's 1/3 Rule** for numerical integration.

## Features
- Mathematical discussion with full derivation
- Two complete step-by-step worked examples
- Interactive calculator with step table and CSV export
- Safe expression evaluator (no arbitrary code execution)

## Tech Stack
- Python 3.8+ / Flask
- HTML + CSS + Vanilla JS
- MathJax (LaTeX rendering)

## Run Locally
```bash
pip install flask
python app.py
```
Then open http://127.0.0.1:5000

## Deploy to Vercel
```bash
npm install -g vercel
vercel
```

## Project Structure
```
├── app.py              # Flask backend + Simpson's algorithm
├── requirements.txt    # Dependencies
├── vercel.json         # Vercel deployment config
└── templates/
    └── index.html      # Full UI (discussion, examples, calculator)
```
