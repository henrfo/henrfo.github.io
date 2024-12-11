# part2_clean_and_merge.py

import pandas as pd
import os
import re
from stopwords import norwegian_stopwords, remove_stopwords  # Import the stopword list for Norwegian words and the remove_stopwords function

def clean_text(text):
    """
    Cleans text strings by removing non-alphanumeric characters, 
    excessive whitespace, and normalizing the text.
    """
    if not isinstance(text, str):
        return ""
    # remove special characters, numbers, and excessive whitespace
    text = re.sub(r"[^a-zA-ZæøåÆØÅ\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def remove_stopwords(text, stopwords):
    """
    Removes stopwords from the text.
    """
    words = text.split()
    return " ".join(word for word in words if word.lower() not in stopwords)

def clean_and_merge_csvs(input_folder, output_file):
    """
    Merge and clean multiple CSV files into one consolidated file.
    """
    all_data = []  # list to store data from all CSVs
    
    # Iterates over all CSV files in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            print(f"Processing file: {file_path}")
            
            try:
                # Reads CSV file
                df = pd.read_csv(file_path, encoding="utf-8")
                
                # Drops rows that have a missing values
                df.dropna(subset=["Headline", "Source"], inplace=True)
                
                # Removes duplicate headlines
                df.drop_duplicates(subset=["Headline"], inplace=True)
                
                # Cleans the 'Headline' column
                df["Headline"] = df["Headline"].apply(clean_text)
                
                # Removes stopwords from the 'Headline' column
                df["Headline"] = df["Headline"].apply(lambda x: remove_stopwords(x, norwegian_stopwords))
                
                # Removes rows with empty headlines after cleaning
                df = df[df["Headline"].str.strip().astype(bool)]
                
                all_data.append(df)  # Appends the cleaned data to the list
                
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    
    # Combines all cleaned data into a single DataFrame
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"Total rows after merging: {len(combined_df)}")
        
        # Save the DataFrame to a new CSV file
        combined_df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"Cleaned and merged data saved to '{output_file}'.")
    else:
        print("No valid data found to merge.")

if __name__ == "__main__":
    input_folder = "headlines_csv"
    output_file = "merged_cleaned_headlines.csv"
    clean_and_merge_csvs(input_folder, output_file)
