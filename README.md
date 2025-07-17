# 🌦️ Weather Data Engineering Project with PySpark

This project showcases a complete data engineering pipeline built around real-world weather data. The core focus of this project is on **PySpark**, which I recently learned and aimed to apply in a practical, production-style setup. The pipeline covers data ingestion, transformation, storage, and analytical querying — all aligned with common industry practices.

---

## 🚀 Project Goals

- Build a modular and scalable ETL pipeline using **PySpark**
- Apply data cleaning and transformation techniques on a real dataset
- Store clean data efficiently using **Parquet**
- Perform meaningful analytical queries using **SQL**
- Strengthen data engineering skills with a focus on distributed processing

---

## 🧰 Tools & Technologies

| Tool / Tech       | Purpose                                      |
|-------------------|----------------------------------------------|
| `Python`          | Core scripting language                      |
| `PySpark`         | Distributed data processing (ETL)            |
| `SQL` (PostgreSQL)| Analytical querying                          |
| `Parquet`         | Efficient columnar storage                   |
| `Logging`         | Monitoring and debugging                     |
| `Git & GitHub`    | Version control and project sharing          |

---

## 📁 Project Structure

weather-data-pipeline/
│
├── data/
│ ├── raw/ # Raw CSV input
│ └── processed/ # Cleaned & transformed Parquet files
│
├──spark/
| ├── extract.py # Ingest and clean raw data
| ├── transform.py # Transform and enrich data using PySpark
| ├── load.py # (Optional) Load into a SQL database
| └── main.py # Run pipeline end-to-end
│
├── analysis/
│ └── analysis.ipynb
│
├── postgre/
| ├── schema.sql # PostgreSQL table definition
| └── analysis.sql
├── README.md
└── requirements.txt

---

## 📊 Dataset

- **Source**: [Kaggle - Weather History](https://www.kaggle.com/datasets/muthuj7/weather-dataset)
- **Size**: ~96,000 records
- **Fields**: Temperature, Humidity, Pressure, Wind, Precipitation, Date, etc.

---

## ⚙️ ETL Pipeline Overview

### 1. Extract

- Load raw CSV using PySpark
- Drop irrelevant or highly missing fields
- Convert date/time formats
- Handle missing values (e.g., drop 517 nulls in `Precip Type`)

### 2. Transform

- Extract `year`, `month`, `day` from timestamps
- Calculate monthly average humidity
- Join transformed fields
- Store output as **Parquet** for efficient access

### 3. Load (Optional)

- Prepared a PostgreSQL schema
- Ready to load data using **SQLAlchemy** or Spark’s JDBC writer

---

## 📈 SQL-Based Analysis

A series of SQL queries were used to extract insights, including:

- Average monthly temperature
- Highest humidity months
- Snowy days per year
- Max/min air pressure by month
- Days with above-average humidity
- Seasonal temperature comparison
- Wind speed trends
- Precipitation type breakdown

---

## 💡 What Makes This Project Stand Out?

- Practical use of **PySpark** for full data processing
- Clean, modular Python scripting with proper logging
- Real-world dataset (not e-commerce or synthetic)
- Analytical thinking through insightful SQL queries
- Designed with production-readiness in mind (e.g., directory structure, file separation)

---

## 📌 Next Steps

- Integrate **Apache Airflow** for orchestration
- Containerize pipeline with **Docker** (optional)
- Add data quality checks / unit tests
- Visualize results with a dashboard (e.g., Streamlit)

---

## 👤 Author

**Parsa Kamali Shahry**
Aspiring Data Engineer
GitHub: https://github.com/parsakamali-tech
Email: parsakamlibsns@outlook.com
LinkedIn: https://www.linkedin.com/in/parsa-kamali-243934305/
