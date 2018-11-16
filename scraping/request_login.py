import requests 
from bs4 import BeautifulSoup as bs

'''
session.get(url) : Retrieve information
session.post(url) : Request that the resource at the URI do something with the provided entity
session.put(url) : Store an entity at a URI
session.delete(url) : Update only the specified fields of an entity at a URI
'''

# Login
session = requests.session()

url = 'http://www.hanbit.co.kr/member/login_proc.php'

feed_data = {
    'retun_url': 'http://www.hanbit.co.kr/member/complete_register.html',
    'm_id': '<ID>',
    'm_passwd': '<PASSWORD>',
}

response = session.post(url, data = feed_data)
response.raise_for_status() # raise error if status code ain't 200

# Get mileage
url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'

response = session.get(url)
response.raise_for_status()
soup = bs(response.text, 'html.parser')
mileage = soup.select_one('.mileage_section1 span')
print('Total mileage is :',mileage.get_text())

'''
base = BeautifulSoup(reponse.text).select_one('tag')
base.contents : inner node in tag
base.string : inner string what belongs to itself
base.getText() : inner all string in tag
'''