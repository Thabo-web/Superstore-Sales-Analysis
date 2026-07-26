# name=src/cleaning.py
"""
Cleaning CLI for Superstore Sales Analysis
Run: python src/cleaning.py --in data/raw/Global_Superstore.xlsx --out data/cleaned/cleaned_superstore.parquet

This script performs lightweight, safe cleaning steps so you can run the pipeline from the terminal in Codespaces.
It intentionally keeps things simple and reversible. Expand interactively in VS Code as needed.
"""
from pathlib import Path
import pandas as pd
import argparse


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace('[^0-9a-z_]', '', regex=True)
    )
    return df


def basic_type_coercion(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Common date columns in Global Superstore
    for col in ['order_date', 'order_date', 'ship_date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Numeric columns
    for col in ['sales', 'quantity', 'discount', 'profit']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def compute_derived(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'order_date' in df.columns:
        df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    if 'sales' in df.columns and 'profit' in df.columns:
        # avoid division by zero
        df['profit_margin'] = df.apply(lambda r: (r['profit'] / r['sales']) if r['sales'] else 0.0, axis=1)
    return df


def run_cleaning(input_path: Path, output_path: Path, force: bool = False):
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists() and not force:
        print(f"Output already exists at {output_path}. Use --force to overwrite.")
        return

    print(f"Loading raw data from {input_path}...")
    df = pd.read_excel(input_path, engine='openpyxl')
    print(f"Loaded {len(df)} rows. Standardizing columns...")

    df = standardize_columns(df)
    df = basic_type_coercion(df)

    # Basic cleaning actions
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Dropped {before - after} duplicate rows.")

    # Compute derived features
    df = compute_derived(df)

    # Basic validations (non-fatal)
    if 'order_id' in df.columns:
        if df['order_id'].isnull().any():
            print('Warning: some order_id values are null')
    if 'sales' in df.columns:
        if (df['sales'] < 0).any():
            print('Warning: negative sales present')

    print(f"Saving cleaned data to {output_path}...")
    df.to_parquet(output_path, index=False)
    print("Cleaning complete.")


def cli():
    parser = argparse.ArgumentParser(description='Cleaning stage: raw Excel -> cleaned Parquet')
    parser.add_argument('--in', dest='input', default='data/raw/Global_Superstore.xlsx', help='Path to raw Excel')
    parser.add_argument('--out', dest='output', default='data/cleaned/cleaned_superstore.parquet', help='Output parquet path')
    parser.add_argument('--force', action='store_true', help='Overwrite output if exists')
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    run_cleaning(input_path, output_path, force=args.force)


if __name__ == '__main__':
    cli()
