from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_spend_analytics.config.ConfigStore import *
from pl_spend_analytics.udfs.UDFs import *

def dst_sap_lfa1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sap_silver_db`.`supplier_master`")
