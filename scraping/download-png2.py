'''
방식 : GET
대상 : https://search.naver.com
추가적인 정보
 - 경로 : /search.naver
 - 데이터 
        sm=top_hty
        fbm=0
        ie=utf8
        query=초콜릿
'''

import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver?"
values = {
        "sm" : "top_hty" ,
        "fbm" : "0" ,
        "ie" : "utf8" ,
        "query" : "초콜릿" ,
}

params = urllib.parse.urlencode(values) # convert utf8 to unicode

url = api + params

data = urllib.request.urlopen(url).read() # Naver got blocked requests from non-browser

print(data) # expected result is binary data

text = data.decode('utf-8')

print(text) # expected result is encoded data via utf-8 