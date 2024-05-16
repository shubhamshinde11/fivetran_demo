from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_forecasting_gold.config.ConfigStore import *
from pl_forecasting_gold.udfs.UDFs import *

def deduplicated_data_6(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.distinct()
