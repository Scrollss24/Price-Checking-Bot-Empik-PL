# Price Checking Bot (v3.0 – Playwright Update) 📈🚀

An advanced Python-based web scraper that automates product price monitoring. Upgraded from Requests to **Playwright** to successfully bypass modern anti-bot protection (like Cloudflare) and handle dynamically rendered elements on major e-commerce platforms like Empik.

Tailored for both **small niche websites** and **large e-commerce giants**.

## 🌟 What's New in v3.0
* 🤖 **Browser Automation:** Powered by Playwright to simulate real user behavior.
* 🍪 **Cookie Banner Handling:** Automatically detects and clicks privacy consent forms.
* 🎯 **Class-Agnostic Scraping:** Uses advanced XPath text-location to find prices without relying on volatile CSS classes.
* 🛠️ **Fault Tolerance & Safety:** Fully equipped with network exception handling (`try-except`), timeouts, and input validation.

## 🛠️ How to Run

1. Clone the repository and navigate to the folder:
   ```bash
   git clone https://github.com
   cd Simple-price-checking-bot-
   ```

2. Install the required Python packages:
   ```bash
   pip install playwright
   ```

3. Install the required browser binaries for Playwright:
   ```bash
   playwright install
   ```

4. Run the script:
   ```bash
   python Bot_core/main.py
   ```
