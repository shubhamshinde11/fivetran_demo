from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def by_vendor_number(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.vendor_number") == col("in1.vendor_number")), "inner")\
        .select(col("in0.payment_terms").alias("payment_terms"), col("in0.contract_start_date").alias("contract_start_date"), col("in0.contract_end_date").alias("contract_end_date"), col("in0.purchase_ord_no").alias("purchase_ord_no"), col("in0.doc_type").alias("doc_type"), col("in0.creation_date").alias("creation_date"), col("in0.purchase_org").alias("purchase_org"), col("in0.purchase_group").alias("purchase_group"), col("in0.currency").alias("currency"), col("in0.inco_terms1").alias("inco_terms1"), col("in0.inco_terms2").alias("inco_terms2"), col("in1.vendor_name").alias("vendor_name"), col("in1.country").alias("country"), col("in1.city").alias("city"), col("in1.address").alias("address"), col("in1.vendor_number").alias("vendor_num"), col("in1.vendor_group").alias("vendor_group"))
