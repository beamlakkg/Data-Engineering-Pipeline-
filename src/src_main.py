import pandas as pd
from google.cloud import bigquery
import os
from pathlib import Path


def configure_google_credentials():
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        return

    project_root = Path(__file__).resolve().parents[1]
    key_path = project_root / "key.json"

    if key_path.exists():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(key_path)
        return

    raise FileNotFoundError(
        "Set GOOGLE_APPLICATION_CREDENTIALS or place key.json in the project root."
    )


def main():
    try:
        print("✅ Step 1: Reading data from CSV...")
        df = pd.read_csv("data/input/sales_data_sample.csv", encoding='latin1')

        print("✅ Step 2: Transforming data...")
        df['Revenue'] = df['PRICEEACH'] * df['QUANTITYORDERED']

        print("✅ Step 3: Saving cleaned data...")
        df.to_csv("data/output/cleaned_sales.csv", index=False)

        print("✅ Step 4: Loading to BigQuery...")

        # 🔑 Authenticate
        configure_google_credentials()
        print(f"✅ Using Google credentials from: {os.environ['GOOGLE_APPLICATION_CREDENTIALS']}")

        client = bigquery.Client()

        table_id = "selected-topics-495316.sales_data.sales_table"

        job = client.load_table_from_dataframe(df, table_id)
        job.result()

        print("✅ Loaded to BigQuery successfully!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()