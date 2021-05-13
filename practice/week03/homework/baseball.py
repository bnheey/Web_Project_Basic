import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(
    "https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo",
    headers=headers
)

# print(response.text)
# HTML 데이터 가공
soup = BeautifulSoup(response.text, 'html.parser')

trs = soup.select('#regularTeamRecordList_table > tr')

for tr in trs:
    rank = int(tr.select_one("th > strong").text)
    name = tr.select_one("td > div > span").text
    win = float(tr.select_one("td:nth-child(7) > strong").text)
    # print(rank, name, win)

    if win >= 0.5 :
        print(f"{rank}위 : {name} - {win}")