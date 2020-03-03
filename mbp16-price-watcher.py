
import requests
import smtplib
from bs4 import BeautifulSoup

# Get data from webpage
URL = 'https://www.amazon.com/Apple-MacBook-16-Inch-Storage-2-3GHz/dp/B081FV1Y57/ref=sr_1_3?crid=1FVQXW6TRU4CD&keywords=macbook+pro+16&qid=1583255999&sprefix=macbook%2Caps%2C163&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:6].replace(",",""))

    if converted_price < 2400:
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('myname@gmail.com', 'mypassword')

    subject = 'Price is less than 2,400!'
    body = 'Check the Amazon link: https://www.amazon.com/Apple-MacBook-16-Inch-Storage-2-3GHz/dp/B081FV1Y57/ref=sr_1_3?crid=1FVQXW6TRU4CD&keywords=macbook+pro+16&qid=1583255999&sprefix=macbook%2Caps%2C163&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'myname@gmail.com',
        'myname@hotmail.com',
        msg
    )

    print("Email has been sent")

    server.quit()

check_price()
