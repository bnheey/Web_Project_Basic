import requests
import pprint
import secret
import urllib.request
import sys

# HTTP GET request
import secret
# 미세먼지 25 이상인 지역 이름, 미세먼지 수치를 출력

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

# -----------------------------------------------------------------------------
# 책 정보 검색하기
book_name = '프리워커스'
naver_url = f'https://openapi.naver.com/v1/search/book.json?query={book_name}'

headers = {
    'X-Naver-Client-Id': secret.client_id,
    'X-Naver-Client-Secret': secret.client_secret,
}

response = requests.get(
    naver_url,
    headers=headers,
)

pprint.pprint(response.json())

# -----------------------------------------------------------------------------
# 파파고 API 이용하여 한국어 -> 영어 번역기 만들기

papago_url = 'https://openapi.naver.com/v1/papago/n2mt'

headers = {
    'X-Naver-Client-Id': secret.client_id,
    'X-Naver-Client-Secret': secret.client_secret,
}
ko_input = input("번역할 문장을 입력해주세요(한국어) : ")
data = {
    'source': 'ko',
    'target': 'en',
    'text': ko_input,
}

response = requests.post(
    papago_url,
    headers=headers,
    data=data
)

result = response.json()

print(result['message']['result']['translatedText'])

