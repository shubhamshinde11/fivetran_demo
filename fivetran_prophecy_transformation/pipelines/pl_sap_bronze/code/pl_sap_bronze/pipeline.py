from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_bronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_bask = dss_sap_bask(spark)
    df_dss_sap_bseg = dss_sap_bseg(spark)
    df_reformat_vendor_data = reformat_vendor_data(spark, df_dss_sap_bseg)
    df_reformatted_data = reformatted_data(spark, df_dss_sap_bask)
    df_dss_sap_bkpf = dss_sap_bkpf(spark)
    df_invoice_reformat = invoice_reformat(spark, df_dss_sap_bkpf)
    dst_sap_invoice(spark, df_invoice_reformat)
    dst_sap_vendor(spark, df_reformat_vendor_data)
    df_Reformat_2 = Reformat_2(spark)
    df_Reformat_1 = Reformat_1(spark)
    df_dss_sap_csks = dss_sap_csks(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_bronze")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_bronze")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_bronze", config = Config)(pipeline)

if __name__ == "__main__":
    main()
