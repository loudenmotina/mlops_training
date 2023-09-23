import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

# How To Get The HTML
website = 'https://data.snb.ch/api/cube/amarbma/data/csv/en'
result = requests.get(website)
content = result.text
#print(content)
#doc = BeautifulSoup(content, 'html.parser')
#print(doc.prettify())
#prices=doc.find_all(text="$")
#print(prices)
data_txt=str(content).split(';')
final_data= str(data_txt).replace('"',"")

print(final_data)
with open('finanacial.txt','w') as f:
    f.writelines(final_data)