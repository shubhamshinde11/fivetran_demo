from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from fivetran_pipeline.config.ConfigStore import *
from fivetran_pipeline.udfs.UDFs import *

def fivetran(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/user/hive/warehouse/all_in_one.db/all/")
