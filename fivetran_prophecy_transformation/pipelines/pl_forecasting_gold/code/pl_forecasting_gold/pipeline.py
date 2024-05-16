from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_forecasting_gold.config.ConfigStore import *
from pl_forecasting_gold.udfs.UDFs import *
from prophecy.utils import *
from pl_forecasting_gold.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_source_sg_train = ds_source_sg_train(spark)
    df_ds_source_sg_transactions = ds_source_sg_transactions(spark)
    df_deduplicated_data_4 = deduplicated_data_4(spark, df_ds_source_sg_transactions)
    df_ds_source_sg_test = ds_source_sg_test(spark)
    df_deduplicated_data_3 = deduplicated_data_3(spark, df_ds_source_sg_test)
    df_ds_source_sg_stores = ds_source_sg_stores(spark)
    df_deduplicated_data_2 = deduplicated_data_2(spark, df_ds_source_sg_stores)
    df_ds_source_sg_submission = ds_source_sg_submission(spark)
    df_deduplicated_data_6 = deduplicated_data_6(spark, df_ds_source_sg_submission)
    ds_target_sg_test(spark, df_deduplicated_data_3)
    df_deduplicated_data_5 = deduplicated_data_5(spark, df_ds_source_sg_train)
    df_ds_source_sg_oil = ds_source_sg_oil(spark)
    df_deduplicated_data = deduplicated_data(spark, df_ds_source_sg_oil)
    ds_target_sg_oil(spark, df_deduplicated_data)
    ds_target_sg_train(spark, df_deduplicated_data_5)
    df_ds_source_sg_holiday_ev = ds_source_sg_holiday_ev(spark)
    ds_target_sg_submission(spark, df_deduplicated_data_6)
    df_deduplicated_data_1 = deduplicated_data_1(spark, df_ds_source_sg_holiday_ev)
    ds_target_sg_stores(spark, df_deduplicated_data_2)
    ds_target_sg_transactions(spark, df_deduplicated_data_4)
    ds_target_sg_holiday_ev(spark, df_deduplicated_data_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_forecasting_gold")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_forecasting_gold")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_forecasting_gold", config = Config)(pipeline)

if __name__ == "__main__":
    main()
