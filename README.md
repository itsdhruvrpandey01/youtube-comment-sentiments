# Youtube-Comment-Sentiments
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
1. **Download Twitter sentiment dataset from web or any sentiment dataset and rename it as:**
   ```bas
   sentiment140.csv 
2. **Create your Youtube API KEY:**
   follow below video if you dont know how to create it. 
   ``` bash
   https://youtu.be/LLAZUTbc97I?feature=shared
3. **Clone the Repository:**
   ```bash
   git clone https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/
   ```

4. **Navigate to the Project Directory:**
   ```bash
   cd youtube-comment-sentiments
   ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application:**
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

## Demo
### Home Page
![Home Page](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/abe885d0-fba0-45d7-a368-58cebda908da)

*Fig 5.1: Home Page of the application serves as the initial landing page where users can enter the URL of a YouTube video.*

### Analysis of All Comments
![All Comments Analysis](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/945fa707-906f-4a7a-9153-feabe6a7f456)

*Fig 5.2: Analysis of all comments*

### Positive Comments
![Positive Comments Analysis](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/f0c35627-4747-4262-a993-39b9c9aedc1c)

*Fig 5.3: Analysis of all Positive comments.*

### Neutral Comments
![Neutral Comments Analysis](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/ab4dfe84-fb53-417a-ac33-93273d00e7cf)

*Fig 5.4: Analysis of all Neutral comments.*

### Negative Comments
![Negative Comments Analysis](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/22941f0a-d904-4435-9321-db00ecb88605)

*Fig 5.5: Analysis of all Negative comments.*

### Unidentified Comments
![Unidentified Comments Analysis](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/83d64c5b-f2d2-41d2-9b8e-608d9f13f339)

*Fig 5.6: Analysis of all Unidentified comments.*

### Dark Mode
![Dark Mode](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/10ff2e7b-216b-4d4f-afe3-3f86ad8b1f5b)

*Fig 5.7: Dark mode view of the application.*

### Pie Chart of Analysis
![Pie Chart](https://github.com/itsdhruvrpandey01/youtube-comment-sentiments/assets/130044341/57dcc20e-0219-4836-86d9-116aec5d5217)

*Fig 5.8: Pie Chart showing the analysis of comments by category.*

## Contributors

- Frontend Development: **[Dhruv Pandey](https://github.com/itsdhruvrpandey01)**
- Backend Development:**[Laukik Pawar](https://github.com/Laukik-Pawar)**
