import requests
import pandas as pd 
from bs4 import BeautifulSoup
import pdb

url = "https://ticker.finology.in/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

test= soup.find("table", class_="table table-sm table-hover screenertable")
display=test.find_all("th")
hd=[]
for i in display:
    header = i.text
    hd.append(header)
# print(hd)

df = pd.DataFrame(columns=hd)
# print(data)

dtr = test.find_all("tr")
# print(rdata)
for i in dtr[1:]:
    data1= i.find_all('td')
    rows = [tr.text.strip() for tr in data1]  
    # print(rows)
    l= len(df)
    print(l)
    df.loc[l]=rows
    print(df)
data= df.to_csv('stocks_data.csv')
print(data)