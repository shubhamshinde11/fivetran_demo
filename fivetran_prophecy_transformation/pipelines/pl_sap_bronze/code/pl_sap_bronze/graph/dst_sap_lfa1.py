from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def dst_sap_lfa1(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("append").saveAsTable("`sap_db`.`vendor_addr_tbl`")
