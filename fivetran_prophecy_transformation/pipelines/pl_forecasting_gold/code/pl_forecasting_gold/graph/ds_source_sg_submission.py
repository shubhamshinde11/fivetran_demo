from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_forecasting_gold.config.ConfigStore import *
from pl_forecasting_gold.udfs.UDFs import *

def ds_source_sg_submission(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/mnt/fivetran/forecasting/forecasting_silver_dev/sample_submission/")
