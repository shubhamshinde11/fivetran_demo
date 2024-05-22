from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def dss_sap_lfa1(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/mnt/fivetran/sap_adls/sap_adls_data_21may_saphanadb/lfa1/")
