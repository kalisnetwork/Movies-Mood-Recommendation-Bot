# Mood-Based Movie Recommendation Bot

Welcome to the Mood-Based Movie Recommendation Bot! This Python bot helps you discover movies that match your mood. Choose from a variety of emotions, and the bot will recommend movies that suit your current state of mind.

![movie_recommendations_bot](https://github.com/kalisnetwork/Movies-Mood-Recommendation-Bot/assets/106701723/21642305-68b8-453d-9fd1-da70f0978b12)

## Features

- Recommend movies based on emotions like happiness, sadness, anger, and more.
- Provides a list of movie titles and genres for each mood.
- Simple command-line interface for easy interaction.
- Powered by web scraping IMDb for movie data.
- Incorporates sentiment analysis for accurate mood detection.
- Leverages collaborative and content-based filtering for personalized recommendations.

## How to Use

1. Clone this repository to your local machine.
2. Install the required Python libraries using:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the bot by executing the `app.py` script:
    ```sh
    python app.py
    ```
4. Open your web browser and go to `http://127.0.0.1:5000/`.
5. Follow the on-screen instructions to select your mood and receive movie recommendations.

## Mood Categories

- Happy
- Sad
- Neutral
- Angry
- Scared
- Surprise
- Disgust
- Romantic
- Excited
- Nostalgic

## Requirements

- Python 3.x
- Requests library
- Beautiful Soup library
- Pandas library
- Scikit-learn library
- Flask library
- Transformers library
- TextBlob library

## Project Structure

movie_recommendation_bot/ ├── app.py├── templates/ │ ├── index.html│ ├── recommendations.html└── requirements.txt


- `app.py`: Main script containing the Flask application and recommendation logic.
- `templates/`: Directory containing HTML templates for the web interface.
  - `index.html`: Homepage for mood input.
  - `recommendations.html`: Displays the recommended movies.
- `requirements.txt`: Lists the dependencies required for the project.

### Example Code Snippets

#### Scrape IMDb for Movie Data
```python
import requests
from bs4 import BeautifulSoup

def scrape_imdb_movies_by_genre(genre_name):
    url = f"https://www.imdb.com/search/title/?genres={genre_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        movies = []
        for idx, movie in enumerate(soup.select("h3.lister-item-header"), start=1):
            title = movie.find("a").get_text()
            movies.append({"title": title, "genre": genre_name, "number": idx})
        return movies
    else:
        print(f"Failed to retrieve IMDb data for {genre_name} genre.")
        return []
Sentiment Analysis
python
from transformers import pipeline

def get_sentiment(text):
    sentiment_analyzer = pipeline('sentiment-analysis')
    sentiment = sentiment_analyzer(text)[0]['label'].lower()
    return sentiment
Flask Application
python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['mood']
    sentiment = get_sentiment(user_input)
    recommended_genre = mood_categories.get(sentiment, 'Drama')
    movies = scrape_imdb_movies_by_genre(recommended_genre)
    return render_template('recommendations.html', movies=movies, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
BeautifulSoup

Flask

Transformers

Feel free to contribute or provide feedback to improve the bot. Enjoy your movie recommendations!
