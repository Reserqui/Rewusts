import requests
from bs4 import BeautifulSoup
import lxml
number=10
for n in range(1,100):
    url=f"https://www.ivi.ru/watch/{number+n}"
    r=requests.get(url, timeout=3)
    print(r)