from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp
import logging 


# logging set
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ingest.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# building spark session 
try:
    spark = SparkSession.builder.appName('ingest').getOrCreate()
    logger.info("spark session successfuly created")
except Exception:
    logger.error("fail to create a session")


# reading raw data
try:
    data = spark.read.csv("/app/data/raw/weather.csv", header = True , inferschema = True)
    logger.info("data successfuly read")
except Exception:
    logger.error("error while reading")

# showing schema & changing formatted date to timestamp
data.printSchema()
schema = dict(data.dtypes)
if schema.get('Formatted Date') == 'string':
    data = data.withColumn('Formatted Date', to_timestamp('Formatted Date'))
    logger.info("Converting 'Formatted Date' from string to timestamp")
else:
    logger.info("'Formatted Date' is already timestamp")

# showing data columns & first rows
logger.info(data.columns)
data.show(5)
# as you we have 517 null data only in 'Precip Type' from 96453 rows so i decide to drop the null rows
data = data.na.drop(subset = 'Precip Type')

# droping useless columns
drop_list = ['Summary','Apparent Temperature (C)','Wind Bearing (degrees)', 'Visibility (km)','Loud Cover','Daily Summary']
data = data.drop(drop_list)

# saving data
data.write.mode("overwrite").parquet("/app/data/processed/weather_clean.parquet")

spark.stop()
