import requests

#res = requests.get('https://codedamn.com')
res = requests.get()

print(res.text)
print(res.status_code)


from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://indiacovidresources.in/full")

print(r.html.search())


import requests
from bs4 import BeautifulSoup

URL = 'https://indiacovidresources.in/dl/ewAiAHQAIgA6ADAALAAiAHMAIgA6ACIAYwBsAGEAcwBzAC0AZABhADIAMAA3AGYAZgAxAC0ANAA4AGEAMAAtADQAMABkAGMALQBhADQAZQAwAC0AOABjADIAYQAyADIANwAwADAAOQBmADYAIgAsACIAcgAiADoAIgBwADYAaQBuAFgAMgBPAFMAUgBiAE8AMABvAGkAdAA2AEsARAAyAHgALQBBACIALAAiAG4AIgA6ACIATgBvAGkAZABhACIAfQA%3D/full'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(id='app-root')
# results = soup.find_all("div", class_ = "ReactVirtualized__Grid__innerScrollContainer")
# print(results.prettify())
