from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def by_purchase_order_number_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.purchase_ord_no") == col("in1.po_number")), "inner")\
        .select(col("in0.payment_terms").alias("payment_terms"), col("in0.contract_start_date").alias("contract_start_date"), col("in0.contract_end_date").alias("contract_end_date"), col("in0.purchase_ord_no").alias("purchase_ord_no"), col("in0.doc_type").alias("purchase_doc_type"), col("in0.creation_date").alias("creation_date"), col("in0.purchase_org").alias("purchase_org"), col("in0.purchase_group").alias("purchase_group"), col("in0.currency").alias("currency"), col("in0.inco_terms1").alias("inco_terms1"), col("in0.inco_terms2").alias("inco_terms2"), col("in0.vendor_name").alias("vendor_name"), col("in0.country").alias("country"), col("in0.city").alias("city"), col("in0.address").alias("address"), col("in0.vendor_num").alias("vendor_num"), col("in0.vendor_group").alias("vendor_group"), col("in0.material_group").alias("material_group"), col("in0.spend_description").alias("spend_description"), col("in0.po_no").alias("po_no"), col("in0.po_item").alias("purchase_po_item"), col("in0.Material_no").alias("Material_no"), col("in0.net_price").alias("net_price"), col("in0.quantity").alias("purchase_quantity"), col("in0.gross_price").alias("gross_price"), col("in0.deletion_flag").alias("deletion_flag"), col("in0.completion_flag").alias("completion_flag"), col("in1.posting_date").alias("invoice_posting_date"), col("in1.invoice_date").alias("invoice_date"), col("in1.invoice_no").alias("invoice_no"), col("in1.doc_type").alias("invoice_doc_type"), col("in1.vendor_no").alias("vendor_no"), col("in1.invoice_line_description").alias("invoice_line_description"), col("in1.po_number").alias("invoice_po_number"), col("in1.po_item").alias("invoice_po_item"), col("in1.material").alias("invoice_material"), col("in1.amount").alias("invoice_amount"), col("in1.quantity").alias("invoice_quantity"))
