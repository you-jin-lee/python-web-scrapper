import requests
from bs4 import BeautifulSoup
from practice_indeed import extract_indeed_page, extract_indeed_jobs

indeed_page = extract_indeed_page()

indeed_jobs = extract_indeed_jobs(indeed_page)
