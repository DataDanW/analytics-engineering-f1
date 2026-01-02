# RAW layer summary
## What the RAW layer is

The RAW layer is the first landing zone inside Snowflake. It holds data in a form that is as close to the source as possible, with minimal assumptions and no business logic.

## What I built (TLDR)

* Source: Kaggle Formula 1 dataset (14 CSV tables)
* Landing method: Uploaded CSVs into a Snowflake internal stage (@f1_raw_stage) using Python
* Load method: Used a reusable Snowflake file format (f1_csv_format) and COPY INTO to populate RAW tables
* Design choice: All RAW columns are loaded as VARCHAR to avoid type conflicts and preserve fidelity
* Error handling: ON_ERROR='CONTINUE' so ingestion does not fail on a small number of malformed historical rows

<img width="290" height="305" alt="image" src="https://github.com/user-attachments/assets/eae9368e-8173-40f4-90ac-6768377bf153" />

## The Process

The first step was to create a landing area for the files to land in. 

    CREATE STAGE IF NOT EXISTS f1_raw_stage;


Next, we load the files via python. 
To do this, we create a new file 'src\load\put_csvs_to_stage.py' and created a script which you can find in this repo. This script connects to snowflake using our saved credentials, and places the file in the staging area. This is a preperation step before we copy the data from the tables.

Once complete, we can check the list of csv's in snowflake using the following: 

    LIST @f1_raw_stage;

<img width="1446" height="700" alt="image" src="https://github.com/user-attachments/assets/353ff216-e484-4b5f-89f8-939e5d600096" />

  

We then tell Snowflake how to read the csv's, by creating a file format.
  Note: here we say define the file type, to skip headers, allow speech marks, detect nulls, add nulls and trim whitespace. If columns counts dont match, allow them anyway (snowflake is a little funny so it requires this setting or it will fail the load.

```
CREATE OR REPLACE FILE FORMAT f1_csv_format_lenient
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  TRIM_SPACE = TRUE

  -- Treat both \N and NULL as NULL
  NULL_IF = ('\\N', 'NULL')

  -- Keep empty fields as empty strings (fine for VARCHAR RAW)
  EMPTY_FIELD_AS_NULL = FALSE

  -- Key setting: allow rows with fewer/more columns
  ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE;

```

Now we want to begin creating our table structure. You can do this manually by writing out the column name and data type (like below), but we have 14 tables. This will take some time plus we want to learn how to automate this step. So it requires jumping back to python.
```
// manually create circuits 
CREATE OR REPLACE Table circuits (
circuitId	varchar,
circuitRef	varchar,
name	varchar,
location	varchar,
country	varchar,
lat	varchar,
lng	varchar,
alt varchar,
url varchar
);
```

Back in Python, we create a new file called "src/utils/generate_copy_sql.py" (see in repo), in this file we write the code that creates the reads lists the field names for each table. Here we're assigning varchar datatypes for now but will update these later in the staging layer. 

We then tell snowflake to read each file from the stage (@f1_raw_stage), and add the rows of data. This is a bulk ingestion method. By running this code in Python, we generate the SQL which we can copy and paste into Snowlflake (see repo docs/load_raw.sql), which will looks something like this:

```
CREATE OR REPLACE TABLE circuits (
  "circuitId" VARCHAR,
  "circuitRef" VARCHAR,
  "name" VARCHAR,
  "location" VARCHAR,
  "country" VARCHAR,
  "lat" VARCHAR,
  "lng" VARCHAR,
  "alt" VARCHAR,
  "url" VARCHAR
);

COPY INTO circuits
FROM @f1_raw_stage/circuits.csv
FILE_FORMAT = f1_csv_format
ON_ERROR = 'CONTINUE';
```


We can check the tables using the following:
```
SHOW TABLES IN SCHEMA TIL_PLAYGROUND."F1_DAN_WADE";
```
<img width="1449" height="741" alt="image" src="https://github.com/user-attachments/assets/a29c96b9-6610-49f4-82e8-8faa9fd33291" />





