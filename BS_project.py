import requests
from bs4 import BeautifulSoup
# import re
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
product_name= soup.find_all("a", class_="title")
product_ls=[]
for item in product_name:
    name = item.text.strip()
    product_ls.append(name)
# print(product_ls)

price = soup.find_all("h4", class_="price")
price_ls=[]
for item in price:
    cost= item.text.strip()
    price_ls.append(cost)
# print(price_ls)

description= soup.find_all("p", class_="description card-text")
desc_ls= []
for item in description:
    desc = item.text.strip()
    desc_ls.append(desc)
# print(desc_ls)

reviews = soup.find_all("p", class_="review-count float-end")
reviews_ls=[]
for item in reviews:
    rev= item.text.strip()
    reviews_ls.append(rev)
# print(reviews_ls)

df = pd.DataFrame({
    "product_name": product_ls,
    "price": price_ls,
    "description": desc_ls,
    "reviews": reviews_ls})
data=df.to_csv("collected_data.csv")
print(data)