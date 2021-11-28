from bs4 import BeautifulSoup
import requests

def scrape():
    k = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Scientist&txtLocation=").text
    soup = BeautifulSoup(k, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    
    Links_list, Companies_list, Experience_list, Skills_list, Location_list, Uploaded_list = ([] for i in range(6))

    for job in jobs:
        Uploaded_list.append(job.div.div.div.find_all("span")[1].span.text)
        Links_list.append(job.header.h2.a["href"])
        Companies_list.append(job.header.find("h3", class_="joblist-comp-name").text.strip())
        Experience_list.append(job.ul.li.text.strip().replace(job.ul.li.i.text.strip(), ""))
        j = job.ul.find_all("li")[1]
        Location_list.append(j.span["title"].strip())
        j = job.find_all("ul")[1]
        k = j.find_all("li")[1]
        l = k.span.text.strip()
        Skills_list.append(l.split("  ,  "))

    jobs_list = []
    for i in range(len(Companies_list)):
        jobs_list.append({"href":Links_list[i], "company":Companies_list[i], "experience":Experience_list[i], "skills":Skills_list[i], 
    "location":Location_list[i], "date of upload":Uploaded_list[i]})
    return jobs_list


if __name__=="__main__":
    scrape()


