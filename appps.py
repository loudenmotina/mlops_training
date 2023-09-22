import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

#url = "https://airvisual1.p.rapidapi.com/v2/auto-complete"

# How To Get The HTML
website = 'https://www.walmart.com/cp/groceries-essentials/1735450'
result = requests.get(website)
content = result.text
#print(content)
doc = BeautifulSoup(content, 'html.parser')
#print(doc.prettify())
prices=doc.find_all(text="$")
print(prices)

# Locate the box that contains title and transcript
#box = soup.find('article', class_='/html/body/div[1]/div/div/div/main/div[3]/div')
# Locate title and transcript
#title = box.find('h1').get_text()
#transcript = box.find('soup').get_text(strip=True, separator=' ')
#print(transcript)
#export data in a text file with the "title" name
#with open(f'{title}.txt', 'w') as file:
    #file.writelines(transcript)
#with open('sports.txt', 'w') as file:
 #   file.write(transcript)
#csvFile = open('Text-Editor-Data.csv', 'w')
#writer = csvFile.writelines(soup)
#df=pd.DataFrame('soup')
#df.to_csv()