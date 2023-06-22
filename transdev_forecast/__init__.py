import datetime
import logging

import azure.functions as func
import mysql.connector

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
    print("Donnée insérée avec succès !")


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    requete()