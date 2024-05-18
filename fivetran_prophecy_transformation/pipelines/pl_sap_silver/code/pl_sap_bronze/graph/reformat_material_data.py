from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def reformat_material_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("matnr").alias("material_no"), col("matkl").alias("material_grp"))
