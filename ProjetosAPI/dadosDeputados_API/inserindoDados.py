from pandas.io.sql import execute
from sqlalchemy import create_engine
import psycopg2

cs_postgres = "postgresql://postgres:PRW1633sa#@10.0.0.71:5432/pgWarehouse"

#engine.execute("insert into powerbi.refreshes (requestid, id, starttime, endtime, serviceexceptionjson, status) values('{}', '{}', '{}', '{}', '{}', '{}')");

def inserir(refreshes:dict):
    engine = create_engine(cs_postgres)

    for i in refreshes:

        sql = """
        INSERT into powerbi.refreshes(requestid, id, starttime, endtime, serviceexceptionjson, status)
        values('{}', '{}', '{}', '{}', '{}', '{}');
        """ (['requestid'][i], ['id'][i], ['starttime'][i], ['endtime'][i], ['serviceexceptionjson'][i], ['status'][i])
        engine.execute(sql)



















