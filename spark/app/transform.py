from pyspark.sql import SparkSession
from pyspark.sql.functions import month , year ,dayofmonth, avg
import logging


# logging set
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('transform.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# 
try:
    spark = SparkSession.builder.appName("transform").getOrCreate()
    logger.info("spark session successfuly created")
except:
    logger.error("fail to create a session")

# reading data
try:
    data = spark.read.parquet('/app/data/processed/weather_clean.parquet')
    logger.info("data successfuly read")
except:
    logger.error("error while reading")
# day and month and year of our data
data = data.withColumn('Year', year('Formatted Date'))
data = data.withColumn('Month', month('Formatted Date'))
data = data.withColumn('Day', dayofmonth('Formatted Date'))
# mean of Humidity each month
df = data.groupBy('Month').agg(avg('Humidity').alias('avg_Humidity'))
df.show()

data = data.join(df, on= 'Month', how='left')

# saving data
data.write.mode("overwrite").parquet("/app/data/processed/weather_transformed.parquet")

spark.stop()
