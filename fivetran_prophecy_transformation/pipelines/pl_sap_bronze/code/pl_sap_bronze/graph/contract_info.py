from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def contract_info(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("zterm").alias("payment_terms"), 
        col("kdatb").alias("contract_start_date"), 
        col("kdate").alias("contract_end_date")
    )
