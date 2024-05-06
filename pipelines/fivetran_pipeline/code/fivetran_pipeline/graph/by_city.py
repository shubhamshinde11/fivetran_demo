from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from fivetran_pipeline.config.ConfigStore import *
from fivetran_pipeline.udfs.UDFs import *

def by_city(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.orderBy(col("city"))

    return out0
