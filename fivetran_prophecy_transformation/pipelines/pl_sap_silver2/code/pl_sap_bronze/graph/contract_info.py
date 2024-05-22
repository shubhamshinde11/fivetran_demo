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
        col("kdate").alias("contract_end_date"), 
        col("ebeln").alias("purchase_ord_no"), 
        col("bsart").alias("doc_type"), 
        col("aedat").alias("creation_date"), 
        col("ekorg").alias("purchase_org"), 
        col("ekgrp").alias("purchase_group"), 
        col("waers").alias("currency"), 
        col("inco1").alias("inco_terms1"), 
        col("inco2").alias("inco_terms2"), 
        col("lifnr").alias("vendor_number")
    )
