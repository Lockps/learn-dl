import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK resources (only needed for the first time)
nltk.download('vader_lexicon')

# Create an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "I love this movie. It's so exciting and well-made!"

# Perform sentiment analysis
sentiment_scores = sia.polarity_scores(text)

# Print the sentiment scores
print("Sentiment Scores:")
for key, value in sentiment_scores.items():
    print(f"{key}: {value}")
