from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from business_object_po.config.ConfigStore import *
from business_object_po.udfs.UDFs import *
from prophecy.utils import *
from business_object_po.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_csks = dss_sap_csks(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("business_object_PO")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/business_object_PO")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/business_object_PO", config = Config)(pipeline)

if __name__ == "__main__":
    main()
