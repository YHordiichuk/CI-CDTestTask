import sqlalchemy
import pyodbc
from sqlalchemy import create_engine


def connection():
    database = 'TRN1'
    login = 'loginfortest'
    password = 'test123'
    db_config = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.31.161;DATABASE=%(database)s;UID=%(login)s;PWD=%(password)s;TrustServerCertificate=yes;' % {'database': database, 'login': login, 'password': password}
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % db_config)
    
    return engine


engine = connection()

query = ''

with engine.connect() as con:
    with open("./views/exluded_spends_info.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./views/exluded_spends_info.sql") as file:
        query = text(file.read())
        con.execute(query)

    con.close()

