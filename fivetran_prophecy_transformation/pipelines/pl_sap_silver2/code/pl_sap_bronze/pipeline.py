from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_bronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_ekpo = dss_sap_ekpo(spark)
    df_reformat_material_group_spend_description = reformat_material_group_spend_description(spark, df_dss_sap_ekpo)
    df_ds_sap_ekko = ds_sap_ekko(spark)
    dst_sap_ekpo(spark, df_reformat_material_group_spend_description)
    df_contract_info = contract_info(spark, df_ds_sap_ekko)
    dst_sap_ekko(spark, df_contract_info)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_bronze")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_silver2")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_silver2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
