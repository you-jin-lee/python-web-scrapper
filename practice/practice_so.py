import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort-i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)

    return {'title': title}
    
def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        results = requests.get(f"{URL}&pg={page}")
        soup = BeautifulSoup(results.text, 'html.parser')
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
            
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
