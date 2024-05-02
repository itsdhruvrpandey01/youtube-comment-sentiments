from flask import Flask, render_template, request, redirect, url_for
from textblob import TextBlob
from googleapiclient.discovery import build
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from googleapiclient.errors import HttpError
from langdetect import detect

app = Flask(__name__)

# Set your YouTube API key here
API_KEY = "Your_api_key"

# Download NLTK resources
nltk.download('vader_lexicon')

# Load Sentiment140 dataset
sentiment140_df = pd.read_csv('sentiment140.csv', encoding='latin-1', header=None)
sentiment140_df.columns = ['polarity', 'id', 'date', 'query', 'user', 'text']

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        try:
            return redirect(url_for('sentiment_analyzer', video_url=video_url))
        except InvalidVideoUrlError as e:
            return render_template("invalid_url.html", error=str(e))
    return render_template("index.html")

@app.route("/sentiment", methods=["GET", "POST"])
def sentiment_analyzer():
    video_url = request.args.get('video_url')
    try:
        sentiment_result, comment_data = perform_sentiment_analysis(video_url)
        return render_template("home.html", sentiment_result=sentiment_result, 
                               positive=comment_data["positive"], negative=comment_data["negative"],
                               neutral=comment_data["neutral"], unidentified=comment_data["unidentified"],
                               comments=comment_data["comments_with_sentiment"])
    except InvalidVideoUrlError as e:
        return render_template("invalid_url.html", error=str(e))

class InvalidVideoUrlError(Exception):
    pass

def perform_sentiment_analysis(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise InvalidVideoUrlError("Invalid YouTube video URL")

    comments = get_youtube_comments(video_id)

    comment_data = {
        "comments_with_sentiment": [],
        "positive": 0,
        "negative": 0,
        "neutral": 0,
        "unidentified": 0  # Add a count for unidentified comments
    }

    for comment in comments:
        # Detect language of the comment
        try:
            language = detect(comment)
        except:
            language = "unidentified"

        # If the language is not English, consider it unidentified
        
            

        if language != 'en':
            comment_data["unidentified"] += 1
            comment_data["comments_with_sentiment"].append((comment, "unidentified"))
            continue

        sentiment = analyze_sentiment_from_dataset(comment)
        if sentiment is None:
            sentiment = analyze_sentiment_using_textblob_vader(comment)

        # Determine sentiment category
        sentiment_category = ""
        if sentiment > 0:
            sentiment_category = "Positive"
        elif sentiment < 0:
            sentiment_category = "Negative"
        elif sentiment ==0 :
            sentiment_category = "Neutral"
        else:
            sentiment_category = "unidentified"


        # Append comment with sentiment category to the list
        comment_data["comments_with_sentiment"].append((comment, sentiment_category))
        # Increment count for the corresponding sentiment category
        comment_data[sentiment_category.lower()] += 1

    return "Sentiment Analysis Result", comment_data



def analyze_sentiment_from_dataset(comment):
    matching_row = sentiment140_df[sentiment140_df['text'] == comment]
    if not matching_row.empty:
        return matching_row.iloc[0]['polarity']
    else:
        return None

def analyze_sentiment_using_textblob_vader(comment):
    blob = TextBlob(comment)
    sentiment_textblob = blob.sentiment.polarity
    sentiment_vader = sia.polarity_scores(comment)["compound"]
    return sentiment_textblob if abs(sentiment_textblob) > abs(sentiment_vader) else sentiment_vader

def extract_video_id(video_url):
    video_id = None
    if "youtube.com" in video_url:
        video_id = video_url.split("v=")[1]
    elif "youtu.be" in video_url:
        video_id = video_url.split("/")[-1]
    return video_id

def get_youtube_comments(video_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=350
    )
    try:
        response = request.execute()
        comments = [item["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for item in response["items"]]
        return comments
    except HttpError as e:
        raise InvalidVideoUrlError("Invalid YouTube video URL")

if __name__ == "__main__":
    app.run(debug=True)
