
import pandas as pd
import os

# File paths
INPUT_FILE = r"C:\Users\Admin\Downloads\sales_data.csv"
OUTPUT_FILE = "output/cleaned_sales.csv"


# EXTRACT
def extract_data():
    print("Starting data extraction...")

    df = pd.read_csv(INPUT_FILE)

    print("Data extracted successfully!")
    print("Total records:", len(df))

    return df


# TRANSFORM
def transform_data(df):
    print("Starting data transformation...")

    df = df.drop_duplicates()
    df = df.dropna()

    df["TotalSales"] = df["Quantity"] * df["Price"]

    print("Data cleaning completed!")
    print("Cleaned records:", len(df))

    return df


# LOAD
def load_data(df):
    print("Loading cleaned data...")

    os.makedirs("output", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("Data loaded successfully!")
    print("Output file:", OUTPUT_FILE)


# MAIN ETL PIPELINE
def run_etl():
    df = extract_data()
    cleaned_df = transform_data(df)
    load_data(cleaned_df)

    print("ETL Pipeline completed successfully!")


if __name__ == "__main__":
    run_etl()
