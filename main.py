#built in sublime
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you don't have")
unfamiliar_skills = input('>')


unfamiliar_skills = unfamiliar_skills.split(' ')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            
            counter = 0
            for skill in unfamiliar_skills: 
                if skill not in skills:
                    counter += 1 
                if counter == len(unfamiliar_skills):
                    with open(f'posts/{index}.txt','w') as f:
                        f.write(f"Company Name: {company_name.strip()} \n")
                        f.write(f"Required Skills: {skills.strip()} \n")
                        f.write(f"More Info: {more_info} \n")
                    print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
