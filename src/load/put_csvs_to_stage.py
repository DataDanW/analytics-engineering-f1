import os
from pathlib import Path

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
    # path to your CSVs
    csv_dir = Path("data/raw/2025-12-17/files")

    conn = get_connection()
    cursor = conn.cursor()

    # make sure we're in the right place
    cursor.execute("USE DATABASE TIL_PLAYGROUND")
    cursor.execute('USE SCHEMA "F1_DAN_WADE"')

    # create stage if missing
    cursor.execute("CREATE STAGE IF NOT EXISTS f1_raw_stage")

    # PUT files
    for csv in csv_dir.glob("*.csv"):
        print(f"Uploading {csv.name}")
        cursor.execute(
            f"PUT 'file://{csv.resolve().as_posix()}' @f1_raw_stage AUTO_COMPRESS=FALSE"
        )

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()