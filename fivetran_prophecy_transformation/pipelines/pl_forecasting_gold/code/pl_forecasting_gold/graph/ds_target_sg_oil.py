from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_forecasting_gold.config.ConfigStore import *
from pl_forecasting_gold.udfs.UDFs import *

def ds_target_sg_oil(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write\
        .format("delta")\
        .option("overwriteSchema", False)\
        .mode("overwrite")\
        .save("dbfs:/mnt/fivetran/forecasting/forecasting_gold_dev/oil")
