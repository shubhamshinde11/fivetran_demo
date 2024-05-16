from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *

def project_description_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("post1").alias("project_description"))
