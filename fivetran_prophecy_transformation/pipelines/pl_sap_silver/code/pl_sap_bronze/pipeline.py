from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_bronze.graph import *

def pipeline(spark: SparkSession) -> None:

    if false:
        df_dss_sap_rbkp = dss_sap_rbkp(spark)
        df_select_budat_bldat = select_budat_bldat(spark, df_dss_sap_rbkp)
        dst_sap_rbkp(spark, df_select_budat_bldat)

    df_dss_sap_ekpo = dss_sap_ekpo(spark)
    df_dss_sap_bseg = dss_sap_bseg(spark)
    df_reformat_vendor_data = reformat_vendor_data(spark, df_dss_sap_bseg)
    df_dss_sap_lfa1 = dss_sap_lfa1(spark)
    df_dss_sap_mara = dss_sap_mara(spark)

    if false:
        df_dss_sap_bkpf = dss_sap_bkpf(spark)
        df_invoice_reformat = invoice_reformat(spark, df_dss_sap_bkpf)
        ds_sap_invoice(spark, df_invoice_reformat)

    ds_sap_vendorr(spark, df_reformat_vendor_data)
    df_reformat_material_group_spend_description = reformat_material_group_spend_description(spark, df_dss_sap_ekpo)
    df_ds_sap_ekko = ds_sap_ekko(spark)

    if false:
        df_dss_sap_rsegg = dss_sap_rsegg(spark)
        df_invoice_line_description = invoice_line_description(spark, df_dss_sap_rsegg)
        dst_sap_rseg(spark, df_invoice_line_description)

    df_reformat_material_data = reformat_material_data(spark, df_dss_sap_mara)
    dst_sap_ekpo(spark, df_reformat_material_group_spend_description)
    df_vendor_info_reformat = vendor_info_reformat(spark, df_dss_sap_lfa1)
    df_contract_info = contract_info(spark, df_ds_sap_ekko)
    dst_sap_ekko(spark, df_contract_info)
    dst_sap_lfa1(spark, df_vendor_info_reformat)
    dst_sap_mara(spark, df_reformat_material_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_bronze")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_silver", config = Config)(pipeline)

if __name__ == "__main__":
    main()
