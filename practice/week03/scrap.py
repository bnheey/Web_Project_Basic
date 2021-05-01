import requests
import pprint
import secret

# HTTP GET request
import secret

response = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'
)

result = response.json()
# print(result)
pprint.pprint(result)

data = result['RealtimeCityAir']['row']

for datum in data:
    state = datum['MSRSTE_NM']
    pm10 = datum['PM10']
    if pm10 > 25.0:
        print(f'{state} - {pm10}')

book_name = '프리워커스'
naver_url = f'https://openapi.naver.com/v1/search/book.json?query={book_name}'

headers = {
    'X-Naver-Client-Id': secret.client_id,
    'X-Naver-Client-Secret': secret.client_secret,
}

response = requests.get(
    naver_url,
    headers = headers,
)

pprint.pprint(response.json())
