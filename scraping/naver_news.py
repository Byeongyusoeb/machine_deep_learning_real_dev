import urllib.request
import time
from bs4 import BeautifulSoup as bs

url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"

response = urllib.request.urlopen(url)

soup = bs(response, 'html.parser')

results = soup.select(".cluster_body a") # Find subject

for result in results:
    print('Subject : ',result.string)
    
    url_article = result.attrs["href"] # Find URL 
    
    response = urllib.request.urlopen(url_article)
    
    soup_article = bs(response, 'html.parser')

    content = soup_article.select_one('#articleBodyContents') # Find main content

    print('Content')

    output =""

    for item in content.contents: # Contents attr for string in tag
        stripped = str(item).strip()

        if stripped == "" : 
            continue
        if stripped[0] not in ["<", "/"]:
            output += stripped
    
    print(output.replace(
        '본문 내용TV플레이어',
        '')
        )


    time.sleep(1) # To sleep not to be banned from naver throw multiple requests in a short-time