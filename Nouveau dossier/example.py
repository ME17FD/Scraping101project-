from bs4 import BeautifulSoup
import pandas as pd
import requests
import xml.etree.ElementTree 

products=[] #List to store name of the product
prices=[] #List to store price of the product
location=[] 
tim =[]

content = requests.get("https://www.avito.ma/fr/maroc/pc--à_vendre?o=2", headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'})
file = open("html.html","w",encoding="utf-8")
file.write(str(content.text))
file.close()


soup = BeautifulSoup(content.content,features="lxml")
print(len(soup.findAll('a',href=True)))

for index, a in enumerate(soup.findAll('a',href=True,attrs={'class':'sc-jejop8-1 cYNgZe'})):
    print("==========================================================================")
    
    b= a.find(attrs={'class':'sc-1x0vz2r-0 bpfcIG sc-jejop8-18 dfevBq'})
    print(index,b.text) 
    name = a.find('h3', attrs={'class':'sc-1x0vz2r-0 iXetrR sc-jejop8-19 fIpwiP'})
    price=a.find( attrs={'class':'sc-1x0vz2r-0 bpfcIG sc-jejop8-18 dfevBq'})
    loc=a.findAll( attrs={'class':'sc-jejop8-14 fcoIgW'})[0]
    tmp=a.findAll( attrs={'class':'sc-jejop8-14 fcoIgW'})[0]
    print("name : ",name.text)
    products.append(name.text)
    prices.append(price.text)
    location.append[loc.text]


df = pd.DataFrame({'Product Name':products,'Price':prices,'time':tmp,'location':loc}) 
df.to_excel("cordnts.xlsx")