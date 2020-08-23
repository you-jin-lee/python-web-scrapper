import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=python&limit=50"
LIMIT = 50

def extract_indeed_page():
    indeed_result = requests.get(URL)

    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
    pagination = indeed_soup.find("div", "pagination")

    links = pagination.find_all("a")

    pages = []

    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = max(pages)

    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")

    return jobs
