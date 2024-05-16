from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def reformat_vendor_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("lifnr").alias("vendor_number"), 
        col("dmbtr").alias("spend"), 
        col("sgtxt").alias("line_item_desc"), 
        col("ebeln").alias("po_number"), 
        col("hkont").alias("gl"), 
        col("sgtxt").alias("prepay_doc"), 
        col("buzei").alias("line_item"), 
        col("aufnr").alias("internal_order")
    )
