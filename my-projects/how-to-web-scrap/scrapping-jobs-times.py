from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

html_text = requests.get(url).text 

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    
for job in jobs:
    
    job_main = job.h2.text.strip()
    job_company = job.h3.text.strip()
    
    print(job_main)
    print(job_company)
    
    
    
    break