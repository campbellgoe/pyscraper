import csv
from jobspy import scrape_jobs
from datetime import date
search_term = "three.js"
jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term=search_term,
    location="United Kingdom",
    results_wanted=20,
    hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='UK'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
today = date.today()
thedate = today.strftime("%d-%m-%Y")
jobs.to_csv(search_term+"_"+thedate+"_jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_xlsx