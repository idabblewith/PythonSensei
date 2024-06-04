# Copyright (c) 2024 Jarid Prince

from days.day_047.files.helpers import *


def day_047():
    title("PRICE TRACKER")
    item_uri = "https://www.amazon.com.au/Nintendo-Ring-Fit-Adventure/dp/B07XW8BGFQ/ref=sr_1_1?dchild=1&keywords=ring+fit+adventure&qid=1619889211&sr=8-1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "X-Real-Ip": "180.150.80.162",
    }

    html = requests.get(item_uri, headers=headers)
    html.encoding = "utf-8"
    content = html.text

    soup = BeautifulSoup(content, "html.parser")
    item = soup.find(name="span", id="productTitle").getText().strip()
    # price = float(soup.find(name='span', id="priceblock_ourprice").getText().split("$")[1])
    price = float(soup.find(name="span", class_="a-price-whole").getText())

    desired_price = float(
        nli(
            f'"{item}" is currently ${price}.\nHow much would you actually pay in dollars?'
        )
    )

    if price < desired_price:
        with open("./tools/secrets/email_password.secret") as pass_file:
            password = pass_file.read()
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            my_email = "dmasamune.dokuganryuu@gmail.com"
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(
                from_addr=my_email,
                to_addrs="kaishunmasaji@outlook.com",
                msg=f"Subject: It's a reasonable price!!\n\n{item}: ${price}\n{item_uri}",
            )
        nls("Email sent!")
    else:
        nls("Still not at a reasonable price. Check again later.")
