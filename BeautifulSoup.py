import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


#loading html code from a url into a variable
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page)

#print(soup)
#dt tag elements selected
names = soup.body.findAll('dt')

#regix
function_names = re.findall('id="random.\w+', str(names))

#sliceing the first 4 alphabets 
function_names = [item[4:] for item in function_names]

#defind all function description
description = soup.body.findAll('dd') 

function_usage= []

for item in description:
    item = item.text
    item = item.replace('\n',' ')
    function_usage.append(item)


print(function_names)
print(function_usage)
print(len(function_names))
print(len(function_usage))





data = pd.DataFrame({'function name': function_names, 'Function Usage': function_usage})
data

print(data)
