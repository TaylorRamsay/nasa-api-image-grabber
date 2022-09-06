import requests
import json

from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()

api_key  = '3AvahtwGwoLngcCHiVmHu8ZzukjJLlnk2kh3nUe7'

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2020-01-22'
  params = {
      'api_key':api_key,
      'date':date,
      'hd':'True'
  }
  #response = requests.get(URL_APOD,params=params).json()
  #pp.pprint(response)
  
#fetchAPOD()

#params = {
 #   'api_key':api_key
#}

#response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params).json()

#response = requests.get('https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png', params).json()

#pp.pprint(response)

#photo = requests.get('https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png', params)

epic = requests.get('https://api.nasa.gov/EPIC/api/natural/images?api_key=3AvahtwGwoLngcCHiVmHu8ZzukjJLlnk2kh3nUe7')
data = json.loads(epic.text)

for x in data:
  testPhoto = (x['image'])
  photo = requests.get('https://api.nasa.gov/EPIC/archive/natural/png/' + testPhoto + '?api_key=' + api_key)
