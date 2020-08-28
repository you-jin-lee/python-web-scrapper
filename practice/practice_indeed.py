import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=python&limit=50"
LIMIT = 50

def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", "pagination")

    links = pagination.find_all("a")

    pages = []

    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = max(pages)

    return max_page

def extract_job(html):
    title = html.find("h2", {"class":"title"}).find("a")["title"] # 요소의 속성 접근 방식 = 배열 요소 접근 방식
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})['data-rc-loc']
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f'https://www.indeed.com/viewjob?jk={job_id}'}

    
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"scrapping page{page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_pages = get_last_page()
    jobs = extract_jobs(last_pages)
    return jobs
    
