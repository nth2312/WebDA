import requests
from bs4 import BeautifulSoup

url = "https://webdulichdanang.com/"
r = requests.get(url)

# beautiful file hml
soup = BeautifulSoup(r.content,"html.parser")
with open("index.html", "w") as f:
    f.write(str(soup))
    
# print(soup)