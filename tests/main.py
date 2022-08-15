# run:  pytest main.py > results.txt
import pytest
import sqlalchemy
import urllib
import pyodbc

import queries as qur


def connection():
#     server = r'EPUAKYIW0E87\SQLEXPRESS'
#     database = 'TRN1'
#     login = 'loginfortest'
#     pwd = 'test123'

#     # if you have trouble with new user credentials, you can connect using Trusted_Connection.
#     # Just uncomment params below(row 18-21) and comment row 23-28

#     # params = urllib.parse.quote_plus(' DRIVER={ODBC Driver 17 for SQL Server}; \
#     #                             SERVER=' + server + '; \
#     #                             DATABASE=' + database + '; \
#     #                             Trusted_Connection=yes;')

#     params = urllib.parse.quote_plus(' DRIVER={ODBC Driver 17 for SQL Server}; \
#                                     SERVER=' + server + '; \
#                                     DATABASE=' + database + '; \
#                                     UID=' + login + '; \
#                                     PWD=' + pwd + ';'
#                                     )

#     engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    
    from sqlalchemy import create_engine
    database = 'TRN1'
    login = 'loginfortest'
    password = 'test123'
    db_config = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.31.161:1433;DATABASE=%(database)s;UID=%(login)s;PWD=%(password)s;TrustServerCertificate=yes;' % {'database': database, 'login': login, 'password': password}
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % db_config)
  
        
    return engine.connect()


conn = connection()


class TestDB:
    @pytest.mark.exluded_spends_info
    def test_duplicates(self):
        '''Check [hr].[jobs] job_title column on duplicates'''
        res = conn.execute(qur.dbo_exluded_spends_info_duplicates)
        for row in res:
            assert row[0] == 0, f'{row[0]} duplicates founded in job_title column!'

    def test_total_cnt(self):
        res = conn.execute(qur.dbo_exluded_spends_info_cnt)
        for row in res:
            assert row[1] <= 40, f'List of employees is not correct!'

    def test_data_validation(self):
        res = conn.execute(qur.dbo_exluded_spends_info_validation)
        for row in res:
            assert row[0] == 0, f'{row[0]} bad format rows!'

    @pytest.mark.spends_by_country
    def test_null_rows_check(self):
        res = conn.execute(qur.spends_by_country_count_validation)
        for row in res:
            assert row[0] <= 4, f'Issue with data completeness! {row[0]} New bad rows founded!'

