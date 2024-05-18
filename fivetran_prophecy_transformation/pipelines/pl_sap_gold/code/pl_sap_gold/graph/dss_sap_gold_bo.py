from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def dss_sap_gold_bo(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sap_gold_db`.`bo_purchase`")
