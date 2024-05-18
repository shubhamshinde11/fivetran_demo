from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def ds_sap_invoice(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/mnt/fivetran/sap_adls/silver/accounting_document_header")\
        .mode("overwrite")\
        .saveAsTable("`sap_silver_db`.`accounting_document_header`")
