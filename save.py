import csv

def save_to_file(jobs):
    file = open("jobs.csv", "w", -1, 'utf-8-sig', newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
