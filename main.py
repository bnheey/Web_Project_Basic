'''
터미널에서 import 받은 라이브러리 설치

pip install request
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup

url = "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=129898191&siteId=soft&menuType=T&uId=9&sortChar=A&linkUrl=06-3.html&mainFrame=right"

r = requests.get(url)
print(r.content)