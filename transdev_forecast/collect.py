import os
import mysql.connector
import logging

def db_connect():
    host = os.environ.get("DB_HOST")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DB_DATABASE")

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conn

def requete():
    conn = db_connect()
    cursor = conn.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS `trigger` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            value TEXT
        )
    '''
    cursor.execute(create_table_query)

    insert_query = "INSERT INTO `trigger` (value) VALUES ('Injection')"
    cursor.execute(insert_query)
    conn.commit()

    logging.info("Donnée insérée avec succès !")