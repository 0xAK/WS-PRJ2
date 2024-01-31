import requests as Nug
from bs4 import BeautifulSoup
import pandas as pd

url = "https://archiexpo.ie/a-z-listing/"
resp = Nug.get(url)
html_content = resp.content

soup = BeautifulSoup(html_content, 'html.parser')
elements = soup.find_all('td', class_="xl63")
x=[]
y=[]
for i in elements:
    a=i.a.text if i.a and i.a.text else ''
    b=i.a['href'] if i.a and i.a['href'] else ''
    x.append(a)
    y.append(b)

df = pd.DataFrame({
    'Name' : x,
    'link' : y
})

print (df)

df.to_csv("comp.csv", index=False)
