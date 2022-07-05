import requests
import json
import pandas as pd
import psycopg2

url = 'https//dadosabertos.camara.leg.br/api/v2/deputados'
parametros = {}
reposta = requests.request("GET", url, params=parametros)
objetos = json.loads(reposta.text)
dados = objetos['dados']

df = pd.DataFrame(dados)

for col in df.columns:
    df[col] = df[col].apply(str)

def conecta_db():
    con = psycopg2.connect(host='localhost',
                           database='db_deputados',
                           password='postgres')
    return con

def criar_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

sql = 'DROP TABLE IF EXISTS public.deputados'
criar_db(sql)

sql = '''CREATE TABLE public.deputados
    ( id character varying(10),
      uri character varying(100),
      nome character varying(500),
      siglaPartido character varying(50),
      uriPartido character varying(200),
      siglaUf character varying(10),
      idLegislatura character varying(10),
      urlFoto character varying(100),
      email character varying(100), 
    )'''
criar_db(sql)

def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

for i in df.index:
    sql = """
    INSERT into public.deputados(id, uri, nome, siglaPartido, uriPartido, siglaUf, idLegislatura, urlFoto, email)
    values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',);
    """ % (df['id'][i],
           df['uri'][i],
           df['nome'][i],
           df['siglaPartido'][i],
           df['uriPartido'][i],
           df['siglaUf'][i],
           df['idLegislatura'][i],
           df['urlFoto'][i],
           df['email'][i])
    inserir_db(sql)

def consultar_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros
reg = consultar_db('select * from public.deputados')

df_bd = pd.DataFrame(reg, columns=[
    'id', 'uri', 'nome', 'siglaPartido',
    'uriPartido', 'siglaUf', 'idLegislatura',
    'urlFoto', 'email'])
df_bd.head()
















