from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def reformat_material_group_spend_description(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("matkl").alias("material_group"), col("txz01").alias("spend_description"))
