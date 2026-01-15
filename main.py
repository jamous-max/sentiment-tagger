import json
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input_posts.txt"
OUTPUT_FILE = BASE_DIR / "sentiment_report.json"

# Simple sentiment keyword lists
positive_words = ["love", "amazing", "great", "happy", "excellent"]
negative_words = ["terrible", "bad", "hate", "awful", "not"]

def load_posts(file_path):
    """Read text posts from input file and return cleaned list."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        cleaned_lines = []
        for line in lines:
            if line.strip():                 # Skip empty lines
                cleaned_lines.append(line.strip().lower())
    return cleaned_lines

def get_sentiment(text, positive_words, negative_words):
    """Determine sentiment of a single text string."""
    words = text.split()                     # Split sentence into words
    
    for word in words:
        if word in positive_words:
            return "positive"
        if word in negative_words:
            return "negative"
    
    return "neutral"

def build_report(posts, positive_words, negative_words):
    """Build sentiment report list of dictionaries."""
    sent_report = []
    for post in posts:
        sentiment = get_sentiment(post, positive_words, negative_words)
        sent_report.append({"text": post, "sentiment": sentiment})
    return sent_report

def save_report(report, file_path):
    """Save sentiment report as JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

def main():
    cleaned_posts = load_posts(INPUT_FILE)
    report = build_report(cleaned_posts, positive_words, negative_words)
    save_report(report, OUTPUT_FILE)
    print("Sentiment report generated successfully!")

if __name__ == "__main__":
    main()
