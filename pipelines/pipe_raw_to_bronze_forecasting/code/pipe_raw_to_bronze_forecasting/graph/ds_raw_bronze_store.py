from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipe_raw_to_bronze_forecasting.config.ConfigStore import *
from pipe_raw_to_bronze_forecasting.udfs.UDFs import *

def ds_raw_bronze_store(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/user/hive/warehouse/store_sales_forecast.db/stores/")
