from bs4 import BeautifulSoup
import requests
import time

def main():
    ls = []
    counter = 0
    while True:
        if counter == 0: # First time
            url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=West+India&cboWorkExp1=0'
            ls.append(url)
            find_jobs(url)
            print(f'\nCOUNTER: {counter}')   
            counter += 1
   
        else:
            url = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation=West%20India&luceneResultSize=25&postWeek=3&txtKeywords=python&cboWorkExp1=0&pDate=I&sequence=2&startPage='
            url = url + str(counter)
            
            try:
                find_jobs(url)
                ls.append(url)
                print(f'\nCOUNTER: {counter}')
                counter += 1
            # if counter == 2:
            #     html_text = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}).text 
            #     soup = BeautifulSoup(html_text, 'lxml')
            #     test = open('test.html', 'w')
            #     test.write(str(soup))
            #     test.close()
            #     break
                
            except:
                print('Acabou os jobs...')
                break
    for i in ls:
        print(i)
        
            
            
def find_jobs(url):
    html_text = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}).text 
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
        
    for job in jobs:
        job_company =  job.find('h3', class_="joblist-comp-name").text.strip()
        # job_exp = job.ul.li.text.strip()
        # job_loc = job.ul.span.text.strip() 
        # job_info = job.find('ul', class_="list-job-dtl clearfix")
        # job_skills = job_info.span.text.strip().replace(' ', '').replace(',', ', ')
        # job_link = job.find('a')['href']
        
        print('Company: ', job_company)
#         print(f'''
# Skills: {job_skills}
# Experience: {job_exp[11:]}
# Location: {job_loc}
# Company: {job_company}
# Link : ''')


if __name__ == '__main__':
    main()