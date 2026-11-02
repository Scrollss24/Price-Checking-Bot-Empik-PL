import time
from Mail import email_message
from playwright.sync_api import sync_playwright

print("Hello to my price checking bot")
to = input("Firstly input your email address: ")
URL = input("Secondly input your URL adres: ")
while True:
    try:
        Max_price = float(input("Lastly set your max price: "))
        break
    except ValueError:
        print("Please input a valid price")


def checking_price(url, max_price):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            print("bot downloads page data\n")
            page.goto(url,timeout=30000)
            page.click('text="Zaakceptuj zgody"')
            page.wait_for_timeout(timeout=2000)

            print("bot is finding the price\n")
            price_element = page.locator('//span[contains(text(), "zł")] | //div[contains(text(), "zł")]').first
            price_text = price_element.inner_text()
            if "\n" in price_text:
                price_text = price_text.split("\n")[0]
            clean_price = float(price_text.replace("zł", "").replace(",", ".").strip())
            print(f"Actual price: {clean_price}")

            if clean_price < max_price:
                return True
            else:
                print("Still too high price")
                return False
        except Exception as e:
            print(f"oof something is wrong: {e}")
            return False
        finally:
            browser.close()
while True:
    sending = checking_price(URL, Max_price)
    if sending:
        print("I´m sending an email")
        email_message(to,Max_price,URL)
        break
    time.sleep(1200)