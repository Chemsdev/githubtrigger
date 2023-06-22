import mysql.connector
import logging

def db_connect(host: str, user: str, password: str, database: str):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return db

def requete():
    conn = db_connect(
        host="chemsdineserver.mysql.database.azure.com",
        user="chemsdine",
        password="Ounissi69800",
        database="bdd_trigger"
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS `trigger`
        (id INT AUTO_INCREMENT PRIMARY KEY,
        value TEXT)
    ''')

    cursor.execute("INSERT INTO `trigger` (value) VALUES ('fonctionne biennnn !')")
    conn.commit()
    logging.info("Donnée insérée avec succès !")
