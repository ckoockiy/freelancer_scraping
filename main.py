import requests
from bs4 import BeautifulSoup


def getFreelancer(page):
    r = requests.get(f"https://www.freelancer.mx/freelancers/{page}")
    
    if r.status_code == 200:
        print(r.url)
        with open ('data.txt', 'w', encoding="utf-8") as f:
            f.write(r.text)

getFreelancer(1)