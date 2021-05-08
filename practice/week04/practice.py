from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.get_database('test')

# 몽고디비에 데이터 올려보기
# db.person.insert_one(
#     {'name':'kim', 'age':30}
# )
#

# -----------------------------------------------
# 몽고디비에 영화 순위 올리기
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# response = requests.get(
#     'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
#     headers=headers
# )
#
# # print(response.text)
# # HTML 데이터 가공
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')
#
# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
#         title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
#         # print(rank, title, star)
#
#         document = {
#             'rank': int(rank),
#             'title': title,
#             'point': float(star),
#         }
#
#         db.movies.insert_one(document)
#         print('DB 적재 완료', document)

# ------------------------------------------------------------

# CRUD



# 아래와 같이 하면 도큐먼트가 바로 나오지 않음
# 도큐먼트가 바로 나오지 않음
# <pymongo.cursor.Cursor object at 0x000001E66BDB8190>
# 지연된 평가
# 만약 movies_documents 선언하고 한참 나중에 사용한다면?
# print(movies_documents)

movies = list(movies_documents) # 바로 DB 접속해서 가져오도록 list() 사용
print(movies)

