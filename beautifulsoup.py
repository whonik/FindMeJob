from bs4 import BeautifulSoup
from openpyxl import Workbook , load_workbook
import requests 

wb = Workbook()
ws = wb.active
ws.title= "Jobs Info" 
ws.append(["Comapny Name","Sills Required","Link To Apply"])
for i in range(10):    
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Back%20Office&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation=Pune&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0back%20office0DQT0&cboWorkExp1=0&pDate=I&sequence="+str(i)+"&startPage=1").text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')

    ban_words=['voice' ,'call']
    key_words = ['bpo','back','data','finance','insurance']

    for job in jobs:
        company_name = job.find('h3' , class_='joblist-comp-name').text.replace("  ","")#replaces blank spaces
        info_link= job.header.a['href']
        skills = job.find('span', class_='srp-skills').text.replace("  ",'\n')


        isban = False
        for word in ban_words:
            if word in skills.lower():
                isban=True
                break
           
        if not isban:
            for key in key_words:
                if key in skills.lower():
                    ws.append([company_name, skills  , info_link])
                    print(f"Comapny : {company_name}")
                    print(f"Skills Required : {skills}")
                    print(f"Link : {info_link}")

wb.save("Data.xlsx")