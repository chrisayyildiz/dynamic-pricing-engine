from playwright.sync_api import sync_playwright
import time


def get_skiplagged_price(origin: str, destination: str, date: str) -> float:
    url = f"https://skiplagged.com/flights/{origin}/{destination}/{date}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        time.sleep(6)  # Let page load

        prices = []
        try:
            items = page.query_selector_all("div[class*='Result']")
            for item in items:
                text = item.inner_text()
                if "£" in text:
                    price_text = text.split("£")[1].split()[0].replace(",", "")
                    price = float(price_text)
                    prices.append(price)
        except Exception as e:
            print("Error parsing prices:", e)

        browser.close()
        return min(prices) if prices else -1
