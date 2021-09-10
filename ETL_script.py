import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


url_base = 'https://calendarific.com/api/v2/holidays'
key = os.getenv('API_KEY')
country = 'US'

params = {'api_key': key, 
        'country': country,
        'year': datetime.today().strftime('%Y'),
        'month': datetime.today().strftime('%m'),
        'day': datetime.today().strftime('%d')}


name=[]
description=[]
country=[]
type_=[]
date=[]


try:
        #extracting and transforming the data
        response = requests.get(url_base, params = params).json()

        for i in range(len(response['response']['holidays'])):
                nome = response['response']['holidays'][i]['name']
                descricao = response['response']['holidays'][i]['description']
                pais = response['response']['holidays'][i]['country']['name']
                tipo = response['response']['holidays'][i]['type']
                data = response['response']['holidays'][i]['date']

                name.append(nome)
                description.append(descricao)
                country.append(pais)
                type_.append(tipo)
                date.append(data)

except Exception:
    pass


Dados = {'Name':name, 
        'Description':description,
        'Country':country,
        'Type':type_,
        'Date':date}

print(Dados)

#Loading the data

#         import MySQLdb
# # connect
# conn = MySQLdb.connect("127.0.0.1","username","passwore","table")
# x = conn.cursor()

# # write
# x.execute('INSERT into table (row_date, sita, event) values ("%d", "%d", "%d")' % (row_date, sita, event))

# close
# conn.commit()
# conn.close()


#['response']['holidays'][0]['name'] = nome do feriado
#['response']['holidays'][0]['description'] = descrição do feriado
#['response']['holidays'][0]['country']['name'] = nome do país
#['response']['holidays'][0]['type'] = tipo de feriado
#['response']['holidays'][0]['date'] = data do feriado no formato yyyy-mm-dd
#['response']['holidays'][0]['datetime']['year|month|day'] = numero exato da data ano ou mês ou dia
