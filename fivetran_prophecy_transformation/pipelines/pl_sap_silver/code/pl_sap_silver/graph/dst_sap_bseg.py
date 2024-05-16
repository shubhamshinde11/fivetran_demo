from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_silver.config.ConfigStore import *
from pl_sap_silver.udfs.UDFs import *

def dst_sap_bseg(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write.format("delta").mode("overwrite").save("dbfs:/mnt/fivetran/sap_adls/bronze/bseg/")
