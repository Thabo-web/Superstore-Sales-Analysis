# name=src/visualize.py
"""
Lightweight visualization scaffold.
This file intentionally contains runnable examples and comments, but it does not hard-code the whole analysis.
Use in Codespaces/VSCode: run sections in the Interactive Window or run the script to produce example PNGs from processed parquet files.
"""
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')

PROCESSED_DIR = Path("data/processed")
OUTPUTS = Path("outputs")
OUTPUTS.mkdir(parents=True, exist_ok=True)


def plot_monthly_sales(monthly_parquet: Path | str = PROCESSED_DIR / "monthly.parquet"):
    """Load monthly parquet and produce a line chart saved to outputs/monthly_sales.png
    The function is intentionally simple — adapt labels/styles in Codespaces.
    """
    if not Path(monthly_parquet).exists():
        print(f"Monthly data not found at {monthly_parquet}. Run src/processing.py to create it.")
        return
    monthly = pd.read_parquet(monthly_parquet)
    # Expect columns: order_month, month_sales, month_profit
    plt.figure(figsize=(10, 4))
    plt.plot(monthly['order_month'], monthly['month_sales'], marker='o')
    plt.xticks(rotation=45)
    plt.title('Monthly Sales')
    plt.ylabel('Sales')
    plt.tight_layout()
    out = OUTPUTS / 'monthly_sales.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print('Saved', out)


def plot_top_products(top_products_parquet: Path | str = PROCESSED_DIR / "top_products.parquet"):
    if not Path(top_products_parquet).exists():
        print(f"Top-products file not found at {top_products_parquet}. Run src/processing.py first.")
        return
    top = pd.read_parquet(top_products_parquet)
    # Expect columns: product_name, total_sales, total_profit
    top10 = top.sort_values('total_sales', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top10, x='total_sales', y='product_name')
    plt.title('Top 10 Products by Sales')
    plt.tight_layout()
    out = OUTPUTS / 'top_products.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print('Saved', out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Produce visualizations from processed data')
    parser.add_argument('--monthly', action='store_true', help='Plot monthly sales (monthly.parquet)')
    parser.add_argument('--top-products', action='store_true', help='Plot top products (top_products.parquet)')
    args = parser.parse_args()

    if not (args.monthly or args.top_products):
        print('No plots requested. Run with --monthly and/or --top-products')
    if args.monthly:
        plot_monthly_sales()
    if args.top_products:
        plot_top_products()
