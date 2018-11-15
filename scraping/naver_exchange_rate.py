import urllib.request
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/marketindex/"

response = urllib.request.urlopen(url)

soup = bs(response, 'html.parser')

results = soup.select("span.value")

print('KRW-USD : ', results[0].string) # KRW-USD
print('KRW-JPY : ', results[1].string) # KRW-JPY
print('KRW-EUR : ', results[2].string) # KRW-EUR
