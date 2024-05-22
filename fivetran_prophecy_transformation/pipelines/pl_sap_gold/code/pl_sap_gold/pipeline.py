from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_gold.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_gold_document_header = dss_sap_gold_document_header(spark)
    df_dss_sap_gold_document_item = dss_sap_gold_document_item(spark)
    df_by_invoice_no = by_invoice_no(spark, df_dss_sap_gold_document_header, df_dss_sap_gold_document_item)
    df_dst_sap_gold_purchasing_document_header = dst_sap_gold_purchasing_document_header(spark)
    df_dst_sap_supplier_master12 = dst_sap_supplier_master12(spark)
    df_by_vendor_number = by_vendor_number(
        spark, 
        df_dst_sap_gold_purchasing_document_header, 
        df_dst_sap_supplier_master12
    )
    df_dst_sap_gold_purchasing_document_item = dst_sap_gold_purchasing_document_item(spark)
    df_by_purchase_order_number = by_purchase_order_number(
        spark, 
        df_by_vendor_number, 
        df_dst_sap_gold_purchasing_document_item
    )
    dst_sap_gold_BO_purchase(spark, df_by_purchase_order_number)
    df_dss_sap_gold_bo = dss_sap_gold_bo(spark)
    df_by_purchase_order_number_1 = by_purchase_order_number_1(spark, df_dss_sap_gold_bo, df_by_invoice_no)
    dst_sap_gold_bo_invoice(spark, df_by_purchase_order_number_1)
    df_dst_sap_supplier_master = dst_sap_supplier_master(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_gold")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_gold")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_gold", config = Config)(pipeline)

if __name__ == "__main__":
    main()
