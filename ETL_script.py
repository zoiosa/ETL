import requests
from datetime import datetime

url_base = 'https://calendarific.com/api/v2/holidays'

key = 'b80154543e8d9c306e3c18d2e4888adac88a39da'
country = 'US'

params = {'api_key': key, 
        'country': country,
        'year': datetime.today().strftime('%Y'),
        'month': datetime.today().strftime('%m'),
        'day': datetime.today().strftime('%d')}


response = requests.get(url_base, params = params).json()

print(response['response']['holidays'][0]['name'])


def Crawler():


#['response']['holidays'][0]['name'] = nome do feriado
#['response']['holidays'][0]['description'] = descrição do feriado
#['response']['holidays'][0]['country']['name'] = nome do país
#['response']['holidays'][0]['type'] = tipo de feriado
#['response']['holidays'][0]['date'] = data do feriado no formato yyyy-mm-dd
#['response']['holidays'][0]['datetime']['year|month|day'] = numero exato da data ano ou mês ou dia
