import os
from pathlib import Path

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv


def get_connection():
    load_dotenv()
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        authenticator="externalbrowser",
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema=os.environ["SNOWFLAKE_SCHEMA"],
    )


def main():
    raw_root = Path("data/raw")
    latest_run = sorted(raw_root.iterdir())[-1]
    files_dir = latest_run / "files"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("USE SCHEMA F1_DAN_WADE")

    for csv_file in files_dir.glob("*.csv"):
        table_name = csv_file.stem.upper()
        print(f"Loading {table_name}")

        df = pd.read_csv(csv_file)

        columns = ", ".join([f'"{col}" VARCHAR' for col in df.columns])
        cursor.execute(f"""
            CREATE OR REPLACE TABLE {table_name} (
                {columns}
            )
        """)

        success, nchunks, nrows, _ = snowflake.connector.pandas_tools.write_pandas(
            conn,
            df,
            table_name,
            overwrite=True
        )

        print(f"  Rows loaded: {nrows}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
