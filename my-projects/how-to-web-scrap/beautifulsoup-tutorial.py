from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

html_text = requests.get(url).text 

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    
for job in jobs:
# job = soup.find('li', class_="clearfix job-bx wht-shd-bx")
    
    # job_title = job.find('strong', class_="blkclor").text.strip()
    job_company =  job.find('h3', class_="joblist-comp-name").text.strip()
    job_exp = job.ul.li.text.strip()
    job_loc = job.ul.span.text.strip()
    
    job_info = job.find('ul', class_="list-job-dtl clearfix")
    job_skills = job_info.span.text.strip().replace(' ', '').replace(',', ', ')
    
    # job_desc = job_info.li.text.strip()
    # index_job_desc1 = job_desc.index(':') + 3
    # index_job_desc2 = job_desc.index('...') + 3
    
    # job_posted = job.find('span', class_="sim-posted").text.strip()
    job_more = job.find('a')['href']
    print(f'''
Skills: {job_skills}
Experience: {job_exp[11:]}
Location: {job_loc}
Company: {job_company}
Link : {job_more}''')


