from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from fivetran_pipeline.config.ConfigStore import *
from fivetran_pipeline.udfs.UDFs import *
from prophecy.utils import *
from fivetran_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_fivetran = fivetran(spark)
    df_order_by_1 = order_by_1(spark, df_fivetran)
    df_by_city = by_city(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("fivetran_pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/fivetran_pipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/fivetran_pipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
