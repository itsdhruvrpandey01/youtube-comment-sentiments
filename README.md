# youtube-comment-sentiments
## Introduction
This project is a YouTube comment sentiments tool that takes a YouTube video URL as input, fetches comments using the YouTube Data API, analyzes the sentiment of the comments, and displays the results categorized as positive, negative, neutral, or undefined. The sentiment analysis is performed using both a dataset and the VADER lexicon.

## Features
- Input a YouTube video URL for sentiment analysis.
- Fetch comments from the specified YouTube video.
- Detect the language of each comment and categorize them accordingly.
- Analyze sentiment using both a dataset and the VADER lexicon.
- Display the sentiment analysis results.
- Display a chart with the percentage of comments in each sentiment category.

## Technologies Used
- Python
- Flask (for the backend)
- HTML, CSS, JavaScript (for the frontend)
- TextBlob library (for sentiment analysis)
- Google API Client Library (for accessing the YouTube Data API)
- NLTK library (for language detection and sentiment analysis)
- CanvasJS (for chart visualization)

## Installation

To run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd youtube-comment-sentiments
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

Access the application at http://127.0.0.1:5000/ in your web browser.

## Usage
- Run the Flask application:
  ```bash
  python app.py
- Open a web browser and go to http://localhost:5000.
- Enter a valid YouTube video URL in the input field and submit.
- View the sentiment analysis results displayed on the webpage.
- Optionally, click on the "Open Chart" button to view a chart with the percentage of comments in each sentiment category.
