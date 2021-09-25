import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import mysql.connector
import sqlalchemy
import pandas as pd

load_dotenv()


url_base = 'https://calendarific.com/api/v2/holidays'
key = os.getenv('API_KEY')
country = 'US'

params = {'api_key': key, 
        'country': country,
        'year': datetime.today().strftime('%Y'),
        'month': datetime.today().strftime('%m'),
        'day': datetime.today().strftime('%d')}


DataFrame = {'name':[],'description':[], 'country':[], 'type':[], 'date':[]}

#extracting and transforming the data
try:
       
        response = requests.get(url_base, params = params).json()

        for i in range(len(response['response']['holidays'])):
                nome = response['response']['holidays'][i]['name']
                descricao = response['response']['holidays'][i]['description']
                pais = response['response']['holidays'][i]['country']['name']
                tipo = response['response']['holidays'][i]['type']
                data = response['response']['holidays'][i]['date']

                DataFrame['name'] = nome
                DataFrame['description'] = descricao
                DataFrame['country'] = pais
                DataFrame['type']= tipo
                DataFrame['date'] = data

except Exception:
    pass


#Loading the data
     
# connect

PASSWD = os.getenv('PASSWD')

conn = mysql.connector.connect(host='localhost', user='root' , password=PASSWD ,port='3350', database='holidays')
x = conn.cursor()
x.execute("""CREATE TABLE IF NOT EXISTS holidays.feriados (
        name VARCHAR(45),
        description VARCHAR(200),
        country VARCHAR(20),
        type VARCHAR(20),
        date VARCHAR(15),  
        PRIMARY KEY (name))""")

print('aberto database com sucesso')

#usando pandas para injetar os dados
engine = sqlalchemy.create_engine('mysql://root:{}@localhost:3350/holidays'.format(PASSWD))

df = pd.DataFrame(DataFrame)

try:
        df.to_sql('feriados', engine, index=False, if_exists='append')
except:
        print('Dados ja existem na Base de dados')

conn.close()

#['response']['holidays'][0]['name'] = nome do feriado
#['response']['holidays'][0]['description'] = descrição do feriado
#['response']['holidays'][0]['country']['name'] = nome do país
#['response']['holidays'][0]['type'] = tipo de feriado
#['response']['holidays'][0]['date'] = data do feriado no formato yyyy-mm-dd
#['response']['holidays'][0]['datetime']['year|month|day'] = numero exato da data ano ou mês ou dia
