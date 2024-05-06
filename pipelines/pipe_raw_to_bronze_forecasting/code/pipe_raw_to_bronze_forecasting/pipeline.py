from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipe_raw_to_bronze_forecasting.config.ConfigStore import *
from pipe_raw_to_bronze_forecasting.udfs.UDFs import *
from prophecy.utils import *
from pipe_raw_to_bronze_forecasting.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_raw_bronze_store = ds_raw_bronze_store(spark)
    df_deduplicate = deduplicate(spark, df_ds_raw_bronze_store)
    df_ds_raw_bronze_test = ds_raw_bronze_test(spark)
    df_deduplicate_data = deduplicate_data(spark, df_ds_raw_bronze_test)
    df_ds_raw_bronze_transactions = ds_raw_bronze_transactions(spark)
    df_deduplicate_1 = deduplicate_1(spark, df_ds_raw_bronze_transactions)
    ds_rb_dest_test(spark, df_deduplicate_data)
    ds_rb_dest_store(spark, df_deduplicate)
    df_ds_raw_bronze_train = ds_raw_bronze_train(spark)
    df_deduplicated_data = deduplicated_data(spark, df_ds_raw_bronze_train)
    ds_rb_dest_transactions(spark, df_deduplicate_1)
    ds_rb_dest_data(spark, df_deduplicated_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipe_raw_to_bronze_forecasting")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipe_raw_to_bronze_forecasting")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipe_raw_to_bronze_forecasting", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
