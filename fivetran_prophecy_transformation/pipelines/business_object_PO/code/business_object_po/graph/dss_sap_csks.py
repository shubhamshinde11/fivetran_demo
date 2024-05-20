from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from business_object_po.config.ConfigStore import *
from business_object_po.udfs.UDFs import *

def dss_sap_csks(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/mnt/fivetran/sap_adls/sap_adls_data_saphanadb/csks/")
