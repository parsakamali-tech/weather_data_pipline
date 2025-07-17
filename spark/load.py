from pyspark.sql import SparkSession
import logging

# logging config
# logging set
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('load.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Spark session
spark = SparkSession.builder \
    .appName("load_parquet_to_postgres") \
    .getOrCreate()

# Read from parquet
try:
    df = spark.read.parquet("data/processed/weather_transformed.parquet")
    logger.info("Parquet file successfully read.")
except Exception:
    logger.error("Failed to read parquet")

# JDBC config
jdbc_url = "jdbc:postgresql://localhost:5432/weather"
properties = {
    "user": "parsa",
    "password": "Parsa12345",
    "driver": "org.postgresql.Driver"
}

# Write to PostgreSQL
try:
    df.write.mode("overwrite").jdbc(url=jdbc_url, table="weather_data", properties=properties)
    logger.info("Data successfully written to PostgreSQL.")
except Exception:
    logger.error("Failed to write to PostgreSQL")

spark.stop()