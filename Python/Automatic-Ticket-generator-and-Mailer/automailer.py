import smtplib,ssl
import base64
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas
import csv
from Automailer_utils import *
from pathlib import Path
#import png




EMAIL_ADDRESS= os.environ.get('EMAIL_USER') #can set environment variable for email if any or can be set and used in the program
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS') #reading environment variable for password if any

# filename='codefoster.txt'
# fn =open(filename, "w")
# fn=fn.write(" CodeFoster Recuitment Test Resullt  \n\n Congratulations\n You have been Selected for the Interview Round. \n If you have done any project upload it on github or bring the project. \n\n Time:9:00am - 10:00am 8 Aug 2019 \n\n Venue - Cafe91\n\n All the best")
# with open(filename,'rb') as f:
#     file_data=f.read()
#     file_name=f.name



# pdfkit.from_string(body, 'out.pdf',configuration=config) 

# pdfkit.from_file('test.html', 'out1.pdf',configuration=config)
# pdfkit.from_url('http://google.com', 'micro.pdf',configuration=config)




MAIL_SUBJECT="This is mail subject"
MAIL_BODY="THIS IS MSG BODY"

path="C:/Users/HP/AppData/Local/Temp/code.png"
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    

    
    with open('testing.csv','rt')as f: #iterating csv file
        data = csv.reader(f)
        length=0
        for row in data:
            if length!=0:                #skipping first row as it is the attribute or  fieldsnames
                # print(type(row[0]),type(row[1]),type(row[2]))
                generate_qrcode(path,row[0],row[1])
                update_template('templates/template.html',row[0],length)
                msg=create_mail(EMAIL_ADDRESS,row[1],MAIL_SUBJECT,MAIL_BODY)
                server.sendmail(EMAIL_ADDRESS,row[1],msg)    
            length+=1
        
        
       
        
