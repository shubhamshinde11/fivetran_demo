from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipe_raw_to_bronze_forecasting.config.ConfigStore import *
from pipe_raw_to_bronze_forecasting.udfs.UDFs import *

def ds_rb_dest_test(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write.format("delta").save("dbfs:/user/hive/warehouse/bronze/test")
