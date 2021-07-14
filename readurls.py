import json
  
# Read JSON data from file and pretty print it
readfile = open('linkscrapper.json','r')
data = readfile.read()
obj = json.loads(data)
href = [ ]
# print(str(obj['Links1']))
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
#   print('https://www.amazon.com'+i+"\n")