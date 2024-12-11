# part1_news_scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule
from datetime import datetime, timedelta
import re
import socket

# First, define websites and the CSS selectors
websites = {
    "NRK": {"url": "https://www.nrk.no/", "selector": "h2.kur-room__title"},
    "VG": {"url": "https://www.vg.no/", "selector": ".headline"},
    "Aftenposten": {"url": "https://www.aftenposten.no/", "selector": "h2"},
    "Se og Hør": {"url": "https://www.seher.no/", "selector": "h2.headline"}
}

# function that checks internet connectivity
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

# function to clean up text by normalizing space
def clean_text(text):
    """Remove excess whitespace, line breaks, and normalize spaces."""
    return re.sub(r'\s+', ' ', text).strip()

# function to scrape a single website
def scrape_website(url, headline_selector):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.encoding = "utf-8"  # to make sure it understands the Norwegian characters
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(headline_selector)
        
        # fetch and clean up headlines
        cleaned_headlines = []
        for headline in headlines:
            # join all parts of the text and ensuring spacing
            full_text = " ".join(headline.stripped_strings)  # Handles nested tags
            cleaned_headlines.append(clean_text(full_text))
        
        return cleaned_headlines
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# function to scrape and save data
def scrape_daily(retry_count=0):
    max_retries = 3

    # checks internet connectivity
    if not is_connected():
        print("No internet connection. Retrying in 1 hour...")
        if retry_count < max_retries:
            schedule.every(1).hour.do(lambda: scrape_daily(retry_count + 1))
        else:
            print("Max retries reached. Scraping aborted.")
        return

    try:
        print("Scraping started...")
        all_headlines = []

        # scrapes each of the Norwegian newspaper websites
        for site, info in websites.items():
            print(f"Scraping {site}...")
            headlines = scrape_website(info["url"], info["selector"])
            print(f"Collected {len(headlines)} headlines for {site}")
            for headline in headlines:
                all_headlines.append({
                    "Source": site,
                    "Headline": headline,
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Time": datetime.now().strftime("%H:%M:%S")
                })
            time.sleep(1)  # added a delay between requests

        # saves results to a CSV file for each day
        if all_headlines:
            date_today = datetime.now().strftime("%Y-%m-%d")
            file_name = f"news_headlines_{date_today}.csv"
            df = pd.DataFrame(all_headlines)
            df.to_csv(file_name, index=False, encoding="utf-8")
            print(f"Scraping complete! Data saved to '{file_name}'.")
        else:
            print("No headlines collected. No file saved.")
    except requests.exceptions.RequestException as e:
        print(f"Scraping failed: {e}")
        if retry_count < max_retries:
            print(f"Retrying in 1 hour... Attempt {retry_count + 1}/{max_retries}")
            schedule.every(1).hour.do(lambda: scrape_daily(retry_count + 1))
        else:
            print("Max retries reached. Scraping aborted.")
            
if __name__ == "__main__":
	# schedules the scraper to run daily at 8 AM San Diego time (== 5 PM Norway time)
	print("Scheduling scraper to run at 8 AM San Diego time (5 PM Norway time).")
	schedule.every().day.at("08:00").do(scrape_daily)

	# test scheduler in one minute for debugging
	test_time = (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")
	print(f"Test run scheduled at: {test_time}")
	schedule.every().day.at(test_time).do(scrape_daily)

	# run the scheduler
	print("Scheduler is running...")
	while True:
    		schedule.run_pending()
    		time.sleep(1)  # Waits one second before checking again
