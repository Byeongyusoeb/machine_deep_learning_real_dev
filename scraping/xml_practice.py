'''
XML is acronym of eXtensible Markup Language

    Element : <Tag> </Tag> or <Tag/>
    Text : <Tag> {{ String }} </Tag>
    Contents : <Tag> {{Content}} </Tag>
    Property : <Tag property = 'value'> {{Contents}} </Tag> or <Tag property = 'value'/>
    Root Tag : Must be just one
'''

from bs4 import BeautifulSoup as bs
import urllib.request 

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'

response = urllib.request.urlopen(url)

xml = response.read()

soup = bs(xml, 'html.parser')

location = soup.find('city').text
datas = soup.find_all('data')

for data in datas:
    day = data.find('tmef').text
    weather = data.find('wf').text
    min_temperature = data.find('tmn').text
    max_temperature = data.find('tmx').text
    
    print(
        '{} {}의 날씨는 {}이며, 최저 온도는 {} 최고 온도는 {} 입니다.'.format(location, day, weather, min_temperature, max_temperature)
    )

print(location)