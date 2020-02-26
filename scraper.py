import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?keywords=sony+a7&qid=1582730829&sr=8-1"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=price[2:]
    converted_price=converted_price.replace(',', '')
    converted_price=float(converted_price)
    if(converted_price<200000):
        send_mail()
    




def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('vinay04031998@gmail.com', 'aefrxzacosiojgyj')
    subject="Price fell down"
    body="check the amazon link:https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?keywords=sony+a7&qid=1582730829&sr=8-1"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'vinay04031998@gmail.com',
        'yadavg04031998@gmail.com',
        msg
    )
    print('HEY! EMAIL HAS BEEN SENT')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)

