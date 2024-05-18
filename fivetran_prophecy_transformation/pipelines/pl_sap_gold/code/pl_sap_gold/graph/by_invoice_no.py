from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_gold.config.ConfigStore import *
from pl_sap_gold.udfs.UDFs import *

def by_invoice_no(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.invoice_no") == col("in1.invoice_no")), "inner")\
        .select(col("in0.posting_date").alias("posting_date"), col("in0.invoice_date").alias("invoice_date"), col("in0.invoice_no").alias("invoice_no"), col("in0.doc_type").alias("doc_type"), col("in0.vendor_no").alias("vendor_no"), col("in1.invoice_line_description").alias("invoice_line_description"), col("in1.po_number").alias("po_number"), col("in1.invoice_no").alias("invoice_no1"), col("in1.po_item").alias("po_item"), col("in1.material").alias("material"), col("in1.amount").alias("amount"), col("in1.quantity").alias("quantity"))
