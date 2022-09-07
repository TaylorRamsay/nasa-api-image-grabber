import requests
import json
import shutil

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()

api_key  = '3AvahtwGwoLngcCHiVmHu8ZzukjJLlnk2kh3nUe7'

epic = requests.get('https://api.nasa.gov/EPIC/api/natural/images?api_key=3AvahtwGwoLngcCHiVmHu8ZzukjJLlnk2kh3nUe7')
data = json.loads(epic.text)

for x in data:
  testPhoto = (x['image'])
  testPhotoDate = (x['date'])
  formattedDate = testPhotoDate.replace('-', '/')
  dateList = formattedDate.split()
  print(testPhoto + ', ' + dateList[0])

  photo = requests.get('https://api.nasa.gov/EPIC/archive/natural/' + dateList[0] + '/png/' + testPhoto + '.png?api_key=' + api_key, stream = True)
  
  file_name = input('Save image as (string):')

  if photo.status_code == 200:
    with open(file_name, 'wb') as f:
      shutil.copyfileobj(photo.raw, f)
    print('Image sucessfully downloaded: ', file_name)
  else:
    print('Image could not be retreived')
  
  #print(photo)
  #print(type(photo))
  #img = mpimg.imread(photo)
  #imgplot = plt.imshow(img)
  #plt.show()
