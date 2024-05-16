from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_forecasting_silver.config.ConfigStore import *
from pl_forecasting_silver.udfs.UDFs import *
from prophecy.utils import *
from pl_forecasting_silver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_source_bs_train = ds_source_bs_train(spark)
    df_ds_source_bs_submission = ds_source_bs_submission(spark)
    df_deduplicated_data = deduplicated_data(spark, df_ds_source_bs_submission)
    ds_target_bs_submission(spark, df_deduplicated_data)
    df_ds_source_bs_stores = ds_source_bs_stores(spark)
    df_ds_source_bs_test = ds_source_bs_test(spark)
    df_deduplicated_data_1_1 = deduplicated_data_1_1(spark, df_ds_source_bs_test)
    ds_target_bs_test(spark, df_deduplicated_data_1_1)
    df_deduplicated_data_1_3 = deduplicated_data_1_3(spark, df_ds_source_bs_train)
    ds_target_bs_train(spark, df_deduplicated_data_1_3)
    df_ds_bronze_silver_oil = ds_bronze_silver_oil(spark)
    df_deduplicate = deduplicate(spark, df_ds_bronze_silver_oil)
    df_ds_source_bs_transactions = ds_source_bs_transactions(spark)
    df_deduplicated_data_1_2 = deduplicated_data_1_2(spark, df_ds_source_bs_transactions)
    df_ds_source_bs_hoilday_ev = ds_source_bs_hoilday_ev(spark)
    df_deduplicate_data = deduplicate_data(spark, df_ds_source_bs_hoilday_ev)
    ds_target_bs_holiday_ev(spark, df_deduplicate_data)
    ds_target_bs_oil(spark, df_deduplicate)
    ds_target_bs_transactions(spark, df_deduplicated_data_1_2)
    df_deduplicated_data_1 = deduplicated_data_1(spark, df_ds_source_bs_stores)
    ds_target_bs_stores(spark, df_deduplicated_data_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_forecasting_silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_forecasting_silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_forecasting_silver", config = Config)(pipeline)

if __name__ == "__main__":
    main()
