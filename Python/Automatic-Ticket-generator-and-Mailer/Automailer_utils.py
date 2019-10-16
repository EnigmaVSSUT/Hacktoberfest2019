import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas
import csv
import pyqrcode
import pdfkit
import time
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')




def generate_qrcode(*args):

    url = pyqrcode.create( args[1]+" "+args[2],error = 'H')
    url.svg('url.svg',  scale=int(8))
    print("Printing QR code")
    
    url.png(args[0], scale=6, module_color=[0, 0, 0, 128])
    time.sleep(2)


def create_mail(sender,receiver,subject,body,*args):
    msg = MIMEMultipart()
    msg['Subject']=subject
    msg['From']=sender
    msg['To']=receiver
    # body='\nCongratulations \n\nYou have been Selected for Interview round of Club Codefoster!\n\nPlease Ignore any previous mail if you have received.There is no interview on 8th August Morning.\n\nWe will convey further details shortly.'
    msg.attach(MIMEText(body ,'plain'))
    filename='output.pdf'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    return msg.as_string()

def update_template(filename,*args):
    file="code.png"
    body = open('templates/template.html').read().format(name=args[0],filename=file)
    print(body)
   
    fn=open('templates/updated.html','w')
    fn.write(body)
    fn.close()
    css_file="templates/template-CSS.css"
    pdfkit.from_file('templates/updated.html', 'output.pdf',configuration=config,css=css_file)
    # time.sleep(2)
    # pdfkit.from_string(body, 'out.pdf',configuration=config)
