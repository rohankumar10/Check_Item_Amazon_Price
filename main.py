import requests, time, smtplib
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
url = input("Enter your URL here : ")
dp = int(input("Enter your desired price : "))

URL = url


def check_price():
  driver = webdriver.Chrome("YOUR CHROMEDRIVER PATH")
    print(URL)
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')
    title = soup.find('div')
    price = str(soup.find('div', {'class': '_1vC4OE _3qQ9m1'}))
    print(str(title))
    print(price)
    main_price = price[30:35]
    print(main_price)
    # LETS MAKE IT AN INTEGER---------------------------------------------------------------
    l = len(main_price)
    if l <= 4:
        main_price = price[30:35]
    else:
        p1 = price[30]
        p2 = price[32:35]
        pf = str(p1) + str(p2)
        main_price = int(pf)

    price_now = int(main_price)
    # VARIABLES FOR SENDING MAIL---------------------------------------
    title1 = str(title)
    main_price1 = main_price
    print("NAME : " + title1)
    print("CURRENT PRICE : " + str(main_price1))
    print("DESIRED PRICE : " + str(dp))
    # FUNCTION TO CHECK THE PRICE-------------------------------------------------------

    if price_now <= dp:
        send_mail()
    else:
        print("Rechecking... Last checked at " + str(datetime.now()))


# Lets send the mail-----------------------------------------------------------------
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('EMAIL ADDRESS HERE', 'Password')
    subject = "Price of Item has fallen down below Rs. " + str(dp)
    body = "Hey RK! \n The price of Item on AMAZON has fallen down below Rs." + str(
        dp) + ".\n So, hurry up & check the amazon link right now : " + url
    msg = f"Subject: {subject} \n\n {body} "
    server.sendmail(
        'EMAIL ADDRESS HERE',
        'EMAIL ADDRESS HERE',
        msg,
    )
    print("HEY USER, EMAIL HAS BEEN SENT SUCCESSFULLY.")

    server.quit()


# Now lets check the price after 5 min -----------------------------------------------
count = 0
while True:
    count += 1
    print("Count : " + str(count))
    check_price()
    time.sleep(3600)
