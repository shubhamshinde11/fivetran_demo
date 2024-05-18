from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def financial_data_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("kostl").alias("cost_center"), 
        col("bukrs").alias("region"), 
        col("land1").alias("country_key"), 
        col("verak").alias("cc_owner")
    )
