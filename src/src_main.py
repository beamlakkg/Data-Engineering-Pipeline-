import pandas as pd
from google.cloud import bigquery
import os

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
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/Selected Topics/branden254-ETL-Data-Pipeline-fa6d44e/key.json"

        client = bigquery.Client()

        table_id = "selected-topics-495316.sales_data.sales_table"

        job = client.load_table_from_dataframe(df, table_id)
        job.result()

        print("✅ Loaded to BigQuery successfully!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()