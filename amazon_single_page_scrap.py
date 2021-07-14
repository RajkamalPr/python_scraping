import json
from urllib.request import urlopen as userReq
from bs4 import BeautifulSoup as soup
from selectorlib import Extractor
import requests
from time import sleep, time
import scraplinks
# import readurls

# Read JSON data from file and pretty print it
readfile = open('linkscrapper.json','r')
data = readfile.read()
obj = json.loads(data)
href = []
href.append(str(obj['Links1']))
href.append(str(obj['Links2']))
href.append(str(obj['Links3']))
href.append(str(obj['Links4']))
href.append(str(obj['Links5']))
href.append(str(obj['Links6']))
href.append(str(obj['Links7']))
href.append(str(obj['Links8']))
href.append(str(obj['Links9']))
href.append(str(obj['Links10']))
href.append(str(obj['Links11']))
href.append(str(obj['Links12']))
href.append(str(obj['Links13']))
href.append(str(obj['Links14']))
href.append(str(obj['Links15']))
href.append(str(obj['Links16']))

# for i in href:
#   print(i+"\n")


# file = open("amazonScrapper.json","a")
# file.write("{ \n \"scrapedData\" : ")
# file.write("[")

# function to run multiple URL


e = Extractor.from_yaml_file('product.yml')

def scrap(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    # Download the page using requests
    # print("Downloading %s"%url)
    print("Data Downloading... \n %s \n"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500: 
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

with open('productData.json','w') as outfile:
  outfile.write("[")
  for fetchURL in href:
    if(fetchURL != 'None'):
      url='https://www.amazon.com'+fetchURL
      data = scrap(url) 
        # if data:
      
      json.dump(data,outfile)
      outfile.write(",\n")
    else:
      print('page not found !, network error or may be session timeout wait for few minutes then try again...')
  
  outfile.write("]")

# file.write("]\n")
# file.write("}")
# file.close()
print("Happy Scrapping...")