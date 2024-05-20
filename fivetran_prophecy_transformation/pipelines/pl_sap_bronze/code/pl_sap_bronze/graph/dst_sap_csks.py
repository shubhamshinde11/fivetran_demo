from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def dst_sap_csks(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`sap_db`.`costcentre_tbl`")
