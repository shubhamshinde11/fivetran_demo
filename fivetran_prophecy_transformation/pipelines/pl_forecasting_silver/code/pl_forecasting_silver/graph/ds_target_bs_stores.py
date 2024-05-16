from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_forecasting_silver.config.ConfigStore import *
from pl_forecasting_silver.udfs.UDFs import *

def ds_target_bs_stores(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write.format("delta").mode("overwrite").save("dbfs:/mnt/fivetran/forecasting/forecasting_silver_dev/stores/")
