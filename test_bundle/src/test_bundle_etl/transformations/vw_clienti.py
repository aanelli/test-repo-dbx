from pyspark import pipelines as dp
from pyspark.sql.functions import concat_ws, lower

@dp.materialized_view
def vw_clienti():
    clienti = spark.read.table("clienti")

    return clienti.select(
        "id_cliente",
        "nome",
        "cognome",
        "email",
        concat_ws(" ", "nome", "cognome").alias("nome_completo"),
        lower("email").alias("email_normalizzata"),
    )