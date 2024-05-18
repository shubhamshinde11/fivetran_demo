from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def dst_sap_gold_BO_purchase(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/mnt/fivetran/sap_adls/gold/bo_purchase")\
        .mode("overwrite")\
        .saveAsTable("`sap_gold_db`.`bo_purchase`")
