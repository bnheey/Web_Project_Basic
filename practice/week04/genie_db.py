import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.test

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20210514', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

selector = '#body-content > div.newest-list > div > table > tbody > tr'
trs = soup.select(selector)

for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)
    rankdic = {
        'rank': int(rank),
        'title': title,
        'artist': artist  # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
    }
    db.music.insert_one(rankdic)

# top10 검색
top10 = list(db.music.find({'rank': {'$lte': 10}}, {'_id': False}))
print(top10)
db.music.update_one({'rank': 1}, {'$set': {'artist': 'IU'}})
