# Superstore Sales Insights

Short description
- Exploratory data analysis and actionable insights from the Global Superstore dataset. Designed for learning data engineering, EDA, and basic modeling. Optimized to run inside GitHub Codespaces.

Dataset
- Included in repo: data/Global_Superstore.xlsx
- Source (download link): https://github.com/Christelle-Younan/The-Global-Superstore-Dataset-with-Excel/blob/main/Global%20Superstore.xlsx?raw=true

Repository structure
- README.md — this file
- data/ — contains Global_Superstore.xlsx (also stored as cleaned_parquet in workflow)
- notebooks/01-EDA.ipynb — starter exploratory notebook
- src/analysis.py — lightweight skeleton with comments and example snippets
- .devcontainer/ — Codespaces devcontainer configuration
- requirements.txt — suggested Python packages
- .gitignore

Quickstart (Codespaces)
1. Open this repo in Codespaces.
2. Start the container (Codespaces will auto-build the devcontainer).
3. Install dependencies (if not auto-installed): pip install -r requirements.txt
4. Ensure dataset exists at data/Global_Superstore.xlsx. If it is missing, run:
   wget -O data/Global_Superstore.xlsx "https://github.com/Christelle-Younan/The-Global-Superstore-Dataset-with-Excel/blob/main/Global%20Superstore.xlsx?raw=true"
5. Open notebooks/01-EDA.ipynb or src/analysis.py and follow the comments to explore.

Goals & example questions
- Monthly / regional revenue and profit trends
- Top product categories and sub-categories by profit margin
- Customer lifetime value approximation by segment
- Identify underperforming regions/products and suggest actions
- Basic next-quarter sales forecast (optional)

Running notes
- This repo intentionally provides a light Python skeleton in src/analysis.py — implement and run interactively in Codespaces notebook or editor.
- Use the notebook for exploratory plotting and iterative analysis.

Next steps & contributions
- Branch for each new analysis, add plots and a short insights.md summarizing 3–5 key findings.
- If you want, I can add automated tests, CI for basic linting, or an initial MLflow tracking example.

License
- Add a license of your choice (MIT suggested for learning projects).
