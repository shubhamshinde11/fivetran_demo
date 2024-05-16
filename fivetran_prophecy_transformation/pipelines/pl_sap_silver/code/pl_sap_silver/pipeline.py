from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_silver.config.ConfigStore import *
from pl_sap_silver.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_silver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_bs_bseg = dss_sap_bs_bseg(spark)
    df_vendor_spend_data = vendor_spend_data(spark, df_dss_sap_bs_bseg)
    dst_sap_bseg(spark, df_vendor_spend_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_silver", config = Config)(pipeline)

if __name__ == "__main__":
    main()
