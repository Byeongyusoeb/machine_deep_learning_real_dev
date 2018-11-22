'''
JSON is acronym of JavaScript Object notation 

JSON is consist of Numeric, String, Boolean, Null, Array, Onject
'''

from bs4 import BeautifulSoup as bs
import urllib.request
import json
'''
json.dumps : Encoding the data.
json.loads : Decoding the data.
'''

url = 'https://api.github.com/repositories'

response = urllib.request.urlopen(url).read()

json_response = json.loads(response)

for json_data in json_response:
    number = json_data['id']
    name = json_data['name']
    owner = json_data['owner']['login']
    url = json_data['owner']['url']

    print(
        """{}. {}'s {} repo
        url : {}""".format(number, name, owner, url)
    )