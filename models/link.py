import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Function to extract text content from a URL
def extract_text_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and extract all text content
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text
    except Exception as e:
        print("Error occurred while extracting text:", e)
        return None

# Function to summarize text content
def summarize_text(text):
    try:
        # Initialize a summarization pipeline
        summarizer = pipeline("summarization")
        # Summarize the text
        summary = summarizer(text, max_length=1000, min_length=150, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("Error occurred while summarizing text:", e)
        return None

# Function to handle user input and summarize the content of the URL
def summarize_url():
    # Prompt the user to enter a URL
    url = input("Enter the URL you want to summarize: ")
    # Extract text content from the URL
    text = extract_text_from_url(url)
    if text:
        # Summarize the extracted text
        summary = summarize_text(text)
        if summary:
            print("\nSummary:")
            print(summary)
        else:
            print("Failed to summarize the content.")
    else:
        print("Failed to extract text content from the URL.")

# Call the function to summarize the URL provided by the user
summarize_url()
