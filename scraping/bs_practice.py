'''
Tag selector

ID : #name
CLASS : .name
TAS : name
DESCENDENT : name li 
CHILD : name > li
'''

from bs4 import BeautifulSoup as bs

html = """
<html>
    <body>
        <div id='meigne'>
        <h1> 위키북스 도서 </h1>
            <ul class = 'items art it book'>
                <li> 유니티 게임 이펙트 입문 </li>
                <li> 스위프트로 시작하는 아이폰 앱 개발 교과서 </li>
                <li> 모던 웹사이트 디자인의 정석 </li>
            </ul>
        </div>
    </body>
</html>
"""

soup = bs(html, 'html.parser')

selcet_one = soup.select_one('body > div > h1') # select a property

select = soup.select('ul.items li') # select perperties

print(selcet_one.string)

print(soup.select_one('ul').attrs)

print([li.string for li in select])