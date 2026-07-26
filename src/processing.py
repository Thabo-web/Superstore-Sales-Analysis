# name=src/processing.py
"""
Purpose: read cleaned data -> feature engineering & aggregations -> write processed parquet
This file intentionally contains comments and short suggested snippets only.
Run interactively in Codespaces (VSCode) using the interactive window or run as a script.
"""
from pathlib import Path
import pandas as pd

CLEAN_PATH = Path("data/cleaned/cleaned_superstore.parquet")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# 1) Load cleaned data
# df = pd.read_parquet(CLEAN_PATH)

# 2) Example aggregated tables (run interactively)
# Monthly revenue and profit
# monthly = (
#     df.assign(order_month=df['order_date'].dt.to_period('M').astype(str))
#       .groupby('order_month')
#       .agg(month_sales=('sales','sum'), month_profit=('profit','sum'))
#       .reset_index()
# )

# 3) Top products
# top_products = (
#     df.groupby(['category','sub_category','product_name'])
#       .agg(total_sales=('sales','sum'), total_profit=('profit','sum'), orders=('order_id','nunique'))
#       .reset_index()
# )

# 4) Customer-level features (approx LTV)
# customer = (
#     df.groupby('customer_id')
#       .agg(total_sales=('sales','sum'),
#            orders=('order_id','nunique'),
#            avg_order=('sales','mean'),
#            first_order=('order_date','min'),
#            last_order=('order_date','max'))
#       .reset_index()
# )
# customer['recency_days'] = (pd.Timestamp.today() - customer['last_order']).dt.days

# 5) Save processed outputs (parquet)
# monthly.to_parquet(PROCESSED_DIR / 'monthly.parquet', index=False)
# top_products.to_parquet(PROCESSED_DIR / 'top_products.parquet', index=False)
# customer.to_parquet(PROCESSED_DIR / 'customer.parquet', index=False)

# Notes:
# - Keep processed outputs small and focused. Use descriptive filenames.
# - Use these files for visualization and modeling to avoid re-running cleaning steps.
