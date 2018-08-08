import urllib.request
from bs4 import BeautifulSoup
with  urllib.request.urlopen("https://my-eoffice.com/index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    namebox = soup.find_all('li', attrs={'class':'highlighted'})
    for x in namebox:
        name = x.text.strip()
        print(name)
