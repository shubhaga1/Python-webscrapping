import dryscrape
from bs4 import BeautifulSoup

session = dryscrape.Session()
session.visit('https://indiacovidresources.in/full')

response = session.body()
soup = BeautifulSoup(response)

result = soup.find(id="app-root")
print(result)
