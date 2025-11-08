import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", class_="ih-td-tab w-100 auction-tbl", id="t1")

# Extract headers
headers = table.find_all("th")
titles = [header.text.strip() for header in headers]
print("Headers:", titles)

df = pd.DataFrame(columns=titles)

# Extract rows
rows = table.find_all("tr")

for item in rows[1:]:  # Skip header row
    # Get special data from first column
    first_td = item.find_all("td")[0].find("div", class_="ih-pt-img").text.strip()
    
    # Get all other columns
    row_data = item.find_all("td")[1:]
    rdt = [tr.text.strip() for tr in row_data]
    
    # ✅ CORRECT: Insert the special data at the beginning of THIS row
    rdt.insert(0, first_td)
    
    print("Row data:", rdt)
    
    # Add to DataFrame
    l = len(df)
    df.loc[l] = rdt

df.to_csv("mydata.csv")
print(df)