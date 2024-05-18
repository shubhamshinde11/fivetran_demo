from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_spend_analytics.config.ConfigStore import *
from pl_spend_analytics.udfs.UDFs import *
from prophecy.utils import *
from pl_spend_analytics.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dst_sap_lfa1 = dst_sap_lfa1(spark)
    df_dst_sap_bseg1 = dst_sap_bseg1(spark)
    df_dst_sap_bkpf = dst_sap_bkpf(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_spend_analytics")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_spend_analytics")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_spend_analytics", config = Config)(pipeline)

if __name__ == "__main__":
    main()
