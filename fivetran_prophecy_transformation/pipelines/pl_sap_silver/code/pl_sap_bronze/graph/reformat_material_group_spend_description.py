from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def reformat_material_group_spend_description(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("matkl").alias("material_group"), 
        col("txz01").alias("spend_description"), 
        col("ebeln").alias("po_no"), 
        col("ebelp").alias("po_item"), 
        col("matnr").alias("Material_no"), 
        col("netpr").alias("net_price"), 
        col("menge").alias("quantity"), 
        col("netwr").alias("gross_price"), 
        col("loekz").alias("deletion_flag"), 
        col("elikz").alias("completion_flag")
    )
