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
        col("buzei").alias("line_item"), 
        col("aufnr").alias("internal_order"), 
        col("bukrs").alias("region"), 
        col("gjahr").alias("fiscal_year"), 
        col("belnr").alias("acc_doc_no"), 
        col("augbl").alias("clearing_doc_no"), 
        col("shkzg").alias("debit_credit"), 
        col("rfccur").alias("reference_currency"), 
        col("zuonr").alias("assignment_no"), 
        col("werks").alias("plant"), 
        col("matnr").alias("material"), 
        col("awkey").alias("ref_key")
    )
