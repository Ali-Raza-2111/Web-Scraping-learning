import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
BASE_URL = 'https://remoteok.com/api/'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def get_job_postings():
    res = requests.get(url=BASE_URL,headers=headers)
    return res.json()

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i in range(0,len(headers)):
        job_sheet.write(0,i,headers[i])
    for i in range(0,len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(0,len(values)):
            job_sheet.write(i+1,x,values[x])
    wb.save('remote_Jobs.xls')
    
    
if __name__ == "__main__":
    json = get_job_postings()[1:]
    output_jobs_to_xls(json)