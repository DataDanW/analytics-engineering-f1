flowchart LR
  A[Source data<br/>Kaggle API / CSVs / other connectors] --> B[Ingestion script<br/>Python + config]
  B --> C[Landing storage<br/>Cloud Storage / S3 (optional)]
  C --> D1[BigQuery<br/>raw / landing dataset]
  C --> D2[Snowflake<br/>RAW schema]

  D1 --> E[Transforms<br/>dbt / SQL models]
  D2 --> E

  E --> F[Analytics layer<br/>marts / curated tables]
  F --> G[Consumption<br/>Tableau / Looker / Power BI]
  F --> H[Reverse ETL / Activation<br/>CRM / Marketing tools (optional)]

  B --> I[Orchestration<br/>Scheduler / GitHub Actions / Airflow]
  I --> B
  I --> E

  B --> J[Logging + Monitoring<br/>row counts / failures / alerts]
  E --> J
