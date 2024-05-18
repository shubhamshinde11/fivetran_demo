from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def dst_sap_gold_purchasing_document_header(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sap_silver_db`.`purchasing_document_header`")
