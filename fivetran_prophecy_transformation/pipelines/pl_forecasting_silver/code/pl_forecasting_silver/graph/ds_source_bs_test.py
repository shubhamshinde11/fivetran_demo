from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_forecasting_silver.config.ConfigStore import *
from pl_forecasting_silver.udfs.UDFs import *

def ds_source_bs_test(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/mnt/fivetran/forecasting/forecasting_bronze_dev/test/")
