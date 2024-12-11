# python3 test_functions.py

import os
import pandas as pd 

from part1_news_scraper import scrape_website
from part2_clean_and_merge import clean_text
from part3_analyze_and_visualize import generate_wordcloud_text
from stopwords import norwegian_stopwords

def test_scrape_function():
    print("Testing scrape_website...")
    websites = {
        "NRK": {"url": "https://www.nrk.no/", "selector": "h2.kur-room__title"}
    }
    try:
        # Run the scraper
        result = scrape_website(websites["NRK"]["url"], websites["NRK"]["selector"])
        assert isinstance(result, list), "scrape_website did not return a list"
        print(f"Scrape function works as intended! Collected {len(result)} headlines.")
    except Exception as e:
        print(f"Test failed: {e}")

def test_clean_text_function():
    print("Testing clean_text...")
    try:
        dirty_text = "Hallo, Verden! 123"
        cleaned = clean_text(dirty_text)
        assert cleaned == "Hallo Verden", f"clean_text failed: {cleaned}"
        print("Clean text function works as intended!")
    except Exception as e:
        print(f"Test failed: {e}")

def test_generate_wordcloud_text_function():
    print("Testing generate_wordcloud_text...")
    try:
        data = pd.DataFrame([{"Headline": "Hallo Verden"}, {"Headline": "Norge er et vakkert land"}])
        wordcloud_text = generate_wordcloud_text(data, "Headline", norwegian_stopwords)
        assert isinstance(wordcloud_text, str), "generate_wordcloud_text didnt return a string"
        assert "Hallo" not in wordcloud_text, "Stopwords were not removed correctly"
        assert "Verden" in wordcloud_text, "Wordcloud text output is incorrect"
        print("Generate wordcloud text function works as intended!")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_scrape_function()
    test_clean_text_function()
    test_generate_wordcloud_text_function()
    print("All tests are completed!")
