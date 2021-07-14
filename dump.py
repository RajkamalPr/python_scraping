# Read JSON data from file and pretty print it
# readfile = open('linkscrapper.json','r')
# data = readfile.read()
# obj = json.loads(data)
# link1 = (str(obj['Links1']))
# link2 = (str(obj['Links2']))
# link3 = (str(obj['Links3']))
# link4 = (str(obj['Links4']))
# link5 = (str(obj['Links5']))
# link6 = (str(obj['Links6']))
# link7 = (str(obj['Links7']))
# link8 = (str(obj['Links8']))
# link9 = (str(obj['Links9']))
# link10 = (str(obj['Links10']))
# link11 = (str(obj['Links1']))
# link12 = (str(obj['Links2']))
# link13 = (str(obj['Links3']))
# link14 = (str(obj['Links4']))
# link15 = (str(obj['Links5']))
# link16 = (str(obj['Links6']))

urlArray = ['link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'link8',
            'link9', 'link10', 'link11', 'link12', 'link13', 'link14', 'link15', 'link16' ]
# mainURL='https://www.amazon.in/s?i=stripbooks&rh=n%3A1318158031&fs=true&qid=1625725169&ref=sr_pg_1'

# urlArray=[

#             'https://www.amazon.in/Inventions-Discoveries-Collection-Knowledge-Encyclopedia/dp/9390391539/ref=sr_1_1_sspa?dchild=1&qid=1625824515&s=books&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMjlMSFZNRTkyMFdNJmVuY3J5cHRlZElkPUEwNDU2NTAyMzkyNUQ0RUE2WVY3RCZlbmNyeXB0ZWRBZElkPUEwMDgxMzczMTEwVVdSUFJPVllaNSZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl',

#             # 'https://www.amazon.in/Secrets-Zynpagua-Demons-Ilika-Ranjan/dp/1543707475/ref=sr_1_2_sspa?dchild=1&qid=1625824515&s=books&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMjlMSFZNRTkyMFdNJmVuY3J5cHRlZElkPUEwNDU2NTAyMzkyNUQ0RUE2WVY3RCZlbmNyeXB0ZWRBZElkPUEwNTQyMDE4VThNUUJRUUwwNU9XJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',

#             'https://www.amazon.in/Harry-Potter-Philosophers-Stone-Rowling-ebook/dp/B019PIOJYU/ref=sr_1_3?dchild=1&qid=1625824515&s=books&sr=1-3',

#             'https://www.amazon.in/Silent-Patient-Alex-Michaelides/dp/1409181634/ref=sr_1_4?dchild=1&qid=1625824515&s=books&sr=1-4',

#             'https://www.amazon.in/Secret-Garden-Frances-Hodgson-Burnett/dp/9386538997/ref=sr_1_5?dchild=1&qid=1625824515&s=books&sr=1-5',

#             'https://www.amazon.in/Harry-Potter-Chamber-Secrets-Rowling-ebook/dp/B019PIOJY0/ref=sr_1_6?dchild=1&qid=1625824515&s=books&sr=1-6',

#             'https://www.amazon.in/Harry-Potter-Cursed-Child-Playscript/dp/0751565369/ref=sr_1_7?dchild=1&qid=1625824515&s=books&sr=1-7',
# ]



def fetchData():
    pageSoup = soup(pageHTML, 'html.parser')
    # --- Scrapper Fields ---
    headers = pageSoup.findAll('h1',{"class":"a-spacing-none a-text-normal"})
    Author = pageSoup.findAll('a',{"class":"a-link-normal contributorNameID"})
    Price = pageSoup.findAll('span',{"a-size-medium a-color-base a-text-normal"})
    # Rating = pageSoup.find('i',{"class":"a-icon a-icon-star a-star-4"})
    Rating = pageSoup.find('span',{"class":"a-icon-alt"})
    # --- Range Calculation for Loop ---
    headerCount = range(len(headers))
    authorCount = range(len(Author))
    priceCount = range(len(Price))

    for header in headerCount:
      file.write("\n{\n")
      file.write(" \"Header\" : ")
      file.write("\"" + headers[header].span.text + "\"")
      # file.write()
      # file.write("\"")
      file.write(",\n")
      print("Titles : " + headers[header].span.text)

    for authorNo in authorCount:
      file.write(" \"Author\" : ")
      file.write("\"")
      file.write(Author[authorNo].text)
      file.write("\"")
      print("Authors : " + Author[authorNo].text)

    for priceNo in priceCount:
      print("Price : " + Price[priceNo].text)
      file.write(" \"Price\" : ")
      file.write("\"")
      file.write(Price[priceNo].text)
      file.write("\"")
    
    # print("Rating : " + Rating.span.text)
    print("Rating : " + Rating.text)
    file.write(",\n")
    file.write(" \"Rating\" : ")
    file.write("\"")
    file.write(Rating.text)
    file.write("\"")
    file.write("\n},")

    print("======= End ====== \n \n")
# function End Here

# --Calling Function here--
# --- Main Codes are get Called by for Loop
