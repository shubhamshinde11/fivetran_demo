from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def invoice_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("awkey").alias("invoice_number"), 
        col("belnr").alias("doc_no"), 
        col("waers").alias("local_currency"), 
        col("bukrs").alias("region"), 
        col("gjahr").alias("fiscal_year"), 
        col("blart").alias("doc_type"), 
        col("cpudt").alias("entered_on"), 
        col("monat").alias("period"), 
        col("budat").alias("posting_date"), 
        col("waers").alias("currency")
    )
