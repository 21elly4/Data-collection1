from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/"
results = requests.get(url)
scrape = BeautifulSoup(results.text, 'html.parser')
grid = scrape.find('product-card-grid narrow')
print(grid)
