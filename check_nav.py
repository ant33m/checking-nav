import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()  # Make sure you call this if you're using .env locally

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = [
    os.getenv("CHAT_ID_1"),
    os.getenv("CHAT_ID_2")
]

NAV_THRESHOLD = 10
NAV_URL = "https://www.nimbacecapital.com/mutual-fund/nav-nibl-sahabhagita-fund/"

def send_telegram(message):
    for chat_id in CHAT_IDS:
        if chat_id:  # ensure it's not None
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {"chat_id": chat_id.strip(), "text": message}
            response = requests.post(url, data=payload)
            print(f"Sent to {chat_id.strip()} - Status: {response.status_code} - Response: {response.text}")
        else:
            print("⚠️ CHAT_ID is missing or not set.")

def get_nav():
    try:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(NAV_URL, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        nav_div = soup.find("div", class_="todays-nav third")
        if nav_div:
            nav_em = nav_div.find("em")
            if nav_em:
                nav_value = float(nav_em.text.strip())
                return nav_value
            else:
                raise ValueError("Could not find NAV <em> tag.")
        else:
            raise ValueError("Could not find NAV container.")
    except Exception as e:
        send_telegram(f"⚠️ NAV Check failed:\n{str(e)}")
        return None

def main():
    nav = get_nav()
    if nav is not None:
        print(f"NIBLSF NAV = Rs. {nav}")
        if nav <= NAV_THRESHOLD:  # always send for debug
            send_telegram(f"📉 ALERT: NIBLSF NAV is Rs. {nav} (<= Rs. {NAV_THRESHOLD})")
        else:
            print("✅ NAV is above threshold.")
    else:
        print("❌ NAV check failed.")

if __name__ == "__main__":
    main()
