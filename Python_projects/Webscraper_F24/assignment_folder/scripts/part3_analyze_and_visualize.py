# part3_analyze_and_visualize.py

import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from stopwords import norwegian_stopwords, remove_stopwords  # Import the stopword list for Norwegian words and the remove_stopwords function

# Useful Functions

def generate_wordcloud_text(df, column, stopwords):
    """
    Generates cleaned text for a word cloud.
    """
    return " ".join(remove_stopwords(text, stopwords) for text in df[column])

def calculate_word_frequencies(df, column, stopwords, top_n=20):
    """
    Calculates word frequencies for a specific column.
    """
    all_text = generate_wordcloud_text(df, column, stopwords)
    word_counts = Counter(all_text.split())
    return word_counts.most_common(top_n)

def plot_combined_wordclouds(df, stopwords):
    """
    Combined word cloud visualization for all the newspapers.
    """
    fig, axs = plt.subplots(1, 4, figsize=(20, 6))

    for i, (source, group) in enumerate(df.groupby("Source")):
        # Generates the word cloud text
        source_text = generate_wordcloud_text(group, "Headline", stopwords)
        wordcloud = WordCloud(width=400, height=400, background_color="white").generate(source_text)
        
        # Plot the word cloud
        axs[i].imshow(wordcloud, interpolation="bilinear")
        axs[i].axis("off")
        axs[i].set_title(f"Word Cloud - {source}", fontsize=14)

    plt.tight_layout()
    plt.show()

def plot_combined_frequencies(df, stopwords):
    """
    Combined frequency bar chart visualization for all the newspapers.
    """
    fig, axs = plt.subplots(1, 4, figsize=(20, 6))

    for i, (source, group) in enumerate(df.groupby("Source")):
        # Calculate the word frequencies
        source_word_counts = calculate_word_frequencies(group, "Headline", stopwords, top_n=10)
        words, counts = zip(*source_word_counts)

        # Plot the frequencies
        axs[i].barh(words, counts, color="skyblue")
        axs[i].set_title(f"Word Frequencies - {source}", fontsize=14)
        axs[i].set_xlabel("Frequency")
        axs[i].invert_yaxis()

    plt.tight_layout()
    plt.show()

# Main Script
if __name__ == "__main__":
    # Load the cleaned and merged CSV
    input_file = "merged_cleaned_headlines.csv"
    df = pd.read_csv(input_file, encoding="utf-8")
    print(f"Loaded {len(df)} headlines from '{input_file}'.")

    # Combined Word Clouds
    print("\n Combined Word Clouds for All Newspapers ")
    plot_combined_wordclouds(df, norwegian_stopwords)

    # Combined Frequencies
    print("\n Combined Frequencies for All Newspapers ")
    plot_combined_frequencies(df, norwegian_stopwords)

    # Overall Analysis
    print("\n Overall Analysis ")
    overall_text = generate_wordcloud_text(df, "Headline", norwegian_stopwords)
    overall_word_counts = calculate_word_frequencies(df, "Headline", norwegian_stopwords, top_n=20)

    # Plot Word Cloud (all)
    plt.figure(figsize=(10, 5))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(overall_text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud - All Newspapers Combined", fontsize=16)
    plt.show()

    # Plot Frequencies (all)
    words, counts = zip(*overall_word_counts)
    plt.figure(figsize=(8, 6))
    plt.barh(words, counts, color="skyblue")
    plt.xlabel("Frequency")
    plt.title("Word Frequencies - All Newspapers Combined", fontsize=16)
    plt.gca().invert_yaxis()
    plt.show()
