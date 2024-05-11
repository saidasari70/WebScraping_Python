
from bs4 import BeautifulSoup
import requests
import csv
'''
url=''
response=requests.get(url)
html_content=response.data

soup=BeautifulSoup(html_content,"html.parser")

links=soup.find_all("a")
images=soup.findall("img")

data=[]

for link in links:
      href=link.get("href")
      text=link.text.strip()
      data.append({"href":src,"text":text})
fro img in images:
      src=img.get("src)
      alt=img.get("alt","")
      data.append({"href":src,"text":alt})
with open("scrapeddata.csv",mode="w",newline="",encoding="utf-8) as file:
       writer=csv.dictWriter(file,fields=["href","src"])
       writer.writeheader()
       for row in data:
          writer.writerow(row)
 
'''
url = "http://127.0.0.1:5500/index.html"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

links = soup.find_all("a")
images = soup.find_all("img")
print(links)
print(images)

data = []

for link in links:
    href = link.get("href")
    text = link.text.strip()
    data.append({"href": href, "text": text})

for image in images:
    src = image.get("src")
    alt = image.get("alt", "")
    data.append({"href": src, "text": alt})

with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["href", "text"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("Web scraping completed. Data saved to scraped_data.csv")

