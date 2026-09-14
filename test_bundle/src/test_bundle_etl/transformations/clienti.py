from pyspark import pipelines as dp

@dp.table
def clienti():
    return spark.createDataFrame(
        [
            (1, "Mario", "Rossi", "mario.rossi@example.com"),
            (2, "Anna", "Bianchi", "anna.bianchi@example.com"),
            (3, "Luca", "Verdi", "luca.verdi@example.com")
        ],
        ["id_cliente", "nome", "cognome", "email"],
    )