from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_bronze.config.ConfigStore import *
from pl_sap_bronze.udfs.UDFs import *
from prophecy.utils import *
from pl_sap_bronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dss_sap_prps = dss_sap_prps(spark)
    df_dss_sap_rbkp = dss_sap_rbkp(spark)
    df_select_budat_bldat = select_budat_bldat(spark, df_dss_sap_rbkp)
    dst_sap_rbkp(spark, df_select_budat_bldat)
    df_dss_sap_ekpo = dss_sap_ekpo(spark)
    df_project_description_reformat = project_description_reformat(spark, df_dss_sap_prps)
    df_dss_sap_bask = dss_sap_bask(spark)
    df_reformatted_data = reformatted_data(spark, df_dss_sap_bask)
    ds_sap_paiddate_tbl(spark, df_reformatted_data)
    df_dss_sap_bseg = dss_sap_bseg(spark)
    df_reformat_vendor_data = reformat_vendor_data(spark, df_dss_sap_bseg)
    df_dss_sap_lfa1 = dss_sap_lfa1(spark)
    df_dss_sap_bkpf = dss_sap_bkpf(spark)
    df_invoice_reformat = invoice_reformat(spark, df_dss_sap_bkpf)
    ds_sap_invoice(spark, df_invoice_reformat)
    ds_sap_vendorr(spark, df_reformat_vendor_data)
    df_dss_sap_ekkn = dss_sap_ekkn(spark)
    df_cost_po_mapping = cost_po_mapping(spark, df_dss_sap_ekkn)
    dst_sap_ekkn(spark, df_cost_po_mapping)
    df_reformat_material_group_spend_description = reformat_material_group_spend_description(spark, df_dss_sap_ekpo)
    df_dss_sap_ekab = dss_sap_ekab(spark)
    df_format_po_contract_numbers = format_po_contract_numbers(spark, df_dss_sap_ekab)
    ds_sap_contract_no(spark, df_format_po_contract_numbers)
    df_ds_sap_ekko = ds_sap_ekko(spark)
    df_dss_sap_rsegg = dss_sap_rsegg(spark)
    df_invoice_line_description = invoice_line_description(spark, df_dss_sap_rsegg)
    dst_sap_prps(spark, df_project_description_reformat)
    dst_sap_ekpo(spark, df_reformat_material_group_spend_description)
    df_dss_sap_csks = dss_sap_csks(spark)
    df_financial_data_reformat = financial_data_reformat(spark, df_dss_sap_csks)
    df_vendor_info_reformat = vendor_info_reformat(spark, df_dss_sap_lfa1)
    df_contract_info = contract_info(spark, df_ds_sap_ekko)
    dst_sap_ekko(spark, df_contract_info)
    dst_sap_csks(spark, df_financial_data_reformat)
    dst_sap_lfa1(spark, df_vendor_info_reformat)
    dst_sap_rseg(spark, df_invoice_line_description)

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
