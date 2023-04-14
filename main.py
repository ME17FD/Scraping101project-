from bs4 import BeautifulSoup
import pandas as pd
import requests
import xlsxwriter


products=[] #List to store name of the product
prices=[] #List to store price of the product
location=[] 
tim =[]

urls=[]
inn = input("what you wanna search : ")
while " " in inn:
    inn = input("what you wanna search(no spaces) : ")




urls.append("https://www.avito.ma/fr/maroc/"+str(inn)+"--à_vendre")
for i in range(2):
    urls.append(urls[0]+'?o='+str(i+1))

maxlenname=0
maxlenloc=0
maxlentime=0
maxlenprice=0

for urll in urls:
    try:
        content = requests.get(urll, headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'})
    except Exception as E:
        print(E)
        exit()
    soup = BeautifulSoup(content.content,features="lxml")
    for index, a in enumerate(soup.findAll('a',href=True,attrs={'class':'sc-jejop8-1 cYNgZe'})):
        print("==========================================================================")
        
        name = a.find('h3', attrs={'class':'sc-1x0vz2r-0 iXetrR sc-jejop8-19 fIpwiP'}).text
        price=a.find( attrs={'class':'sc-1x0vz2r-0 bpfcIG sc-jejop8-18 dfevBq'}).text
        
        timee = a.findAll(attrs={'class':'sc-1x0vz2r-0 hCOOjL'})[0].text
        loc = a.findAll(attrs={'class':'sc-1x0vz2r-0 hCOOjL'})[1].text
    
        if len(name)>maxlenname:
            maxlenname = len(name)
        
        if len(loc)>maxlenloc:
            maxlenloc = len(loc)
        
        if len(timee)>maxlentime:
            maxlentime = len(timee)

        if len(str(price))>maxlenprice:
            maxlenprice = len(str(price))
        

        products.append(name)
        prices.append(price)
        tim.append(timee)
        location.append(loc)
    
        print(index,price) 
        print("name : ",name)


"""
file = open("html.html","w",encoding="utf-8")
file.write(str(content.text))
file.close()
"""


df = pd.DataFrame({'Product Name':products,'Price':prices,'time':tim,'location':location}) 



# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('fiche.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=True, sheet_name='fiche')

# Get access to the workbook and sheet
workbook = writer.book
worksheet = writer.sheets['fiche']

# Reduce the zoom a little
worksheet.set_zoom(90)

worksheet.set_column('B:B', maxlenname)
worksheet.set_column('C:C', maxlenprice)
worksheet.set_column('D:D', maxlentime)
worksheet.set_column('E:E', maxlenloc)
writer._save()