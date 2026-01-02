# 📕Chapter 2 - Data Ingestion: Local

In this chapter we begin to ingest our data, firstly we will do this locally, to practise saving to a local enviroment but future chapters will run through extracting and loading our data into cloud enviroments like Snowflake and GCP.

---

#### Data Ingestion from Kaggle
I connected my project to Kaggle using an API key and built a small script that automatically downloads Formula 1 data and stores it as raw input for future analysis.

**What I did?**
- Created an API token in Kaggle to allow access to datasets from my account
- Configure the Kaggle Command line interface so it could authenticate from my machine
- Searched for Formula 1 datasets to use and selected my chosen project
- Wrote a Python ingestion script to download the dataset and store locally in a dated raw folder on my machine



### Snippet examples
> kaggle datasets files jtrotman/formula-1-race-data
* Asked Kaggle: “What files are inside this dataset?”
* Returned a list of CSVs, their sizes, and creation dates


> python src/ingest/pull_kaggle_f1.py
* Asked Kaggle: “Run the ingestion script and download”
* Unzipped it,Saved it into a dated data/raw/YYYY-MM-DD/ folder and Printed a summary of what was downloaded

## Result?
14 tables showing Formula 1 data from 1950 to 2025

<img width="617" height="417" alt="image" src="https://github.com/user-attachments/assets/785ffe6a-83df-4e26-823b-19a2d952a153" />
