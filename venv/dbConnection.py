# import os
import config
import psycopg2

# os.environ['POSTGRES_HOST'] = 'nro.h.filess.io'
# os.environ['POSTGRES_PORT'] = '5432'
# os.environ['POSTGRES_USER'] = 'postgre_realizepot'
# os.environ['POSTGRES_PASSWORD'] = '35bbda66d62da972ed56b283d7fd211ba759e8ae'
# os.environ['POSTGRES_DB'] = 'postgre_realizepot'
#
# host = os.getenv('POSTGRES_HOST')
# port = os.getenv('POSTGRES_PORT')
# user = os.getenv('POSTGRES_USER')
# password = os.getenv('POSTGRES_PASSWORD')
# database = os.getenv('POSTGRES_DB')

host = config.POSTGRES_HOST
port = config.POSTGRES_PORT
user = config.POSTGRES_USER
password = config.POSTGRES_PASSWORD
database = config.POSTGRES_DB


# Establishes a connection to a PostgreSQL database using the given credentials.
def setupConnection() -> tuple:
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=database)
    cur = conn.cursor()
    return cur, conn


# close db connection
def closeConnection(cur: object, conn: object) -> None:
    cur.close()
    conn.close()
    print('closed')
