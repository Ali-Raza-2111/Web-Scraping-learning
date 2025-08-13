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


def send_email(send_from, app_password, send_to, subject, text, files=None):

    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # Add body text
    msg.attach(MIMEText(text, "plain"))

    # Attach files (if any)
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
        msg.attach(part)

    # Connect to Gmail SMTP
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(send_from, app_password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        print(f"✅ Email sent successfully to {send_to}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
    finally:
        smtp.quit()

    
if __name__ == "__main__":
    json = get_job_postings()[1:]
    output_jobs_to_xls(json)
    send_email(
        send_from='youremail@gmail.com',
        app_password='',
        send_to=['otheremail@gmail.com'],
        subject='Job Postings',
        text='Please find attached the latest remote job listings.',
        files=['remote_jobs.xls']
    )