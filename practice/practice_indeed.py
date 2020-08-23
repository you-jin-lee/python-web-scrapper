import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=python&limit=50"
LIMIT = 50

def extract_indeed_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", "pagination")

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
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            title = result.find("h2", {"class": "title"}).find("a")["title"]
            print(title)
    return jobs
