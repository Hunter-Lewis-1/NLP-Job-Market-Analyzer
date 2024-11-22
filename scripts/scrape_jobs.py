import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url_template = "https://www.indeed.com/jobs?q=data+scientist+software+engineer&l=United+States&start={}"
headers = {"User-Agent": "Mozilla/5.0"}
jobs = []

for start in range(0, 1000, 10):  # Scrape 1000+ jobs
    response = requests.get(url_template.format(start), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for job in soup.select('.job_seen_beacon'):
        title = job.find('h2', class_='jobTitle').text.strip() if job.find('h2') else "N/A"
        desc = job.find('div', class_='job-snippet').text.strip() if job.find('div', class_='job-snippet') else "N/A"
        salary = job.find('span', class_='salary-snippet')
        salary = salary.text.strip() if salary else None
        date = job.find('span', class_='date').text.strip() if job.find('span', class_='date') else "N/A"
        jobs.append([title, desc, salary, date])
    time.sleep(2)  # Avoid rate limits

df = pd.DataFrame(jobs, columns=['title', 'description', 'salary', 'date'])
df.to_csv('../data/raw/job_postings.csv', index=False)
print(f"Scraped {len(df)} jobs to ../data/raw/job_postings.csv")
