import requests
from bs4 import BeautifulSoup


# Scrape IMDb for Movie Data (Sample URL: "https://www.imdb.com/search/title/?genres=genre_name")
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


# Define Mood Categories as IMDb Genres
mood_categories = {
    "happy 😄": "Comedy",
    "sad 😞": "Drama",
    "neutral 😐": "Action",
    "angry 😠": "Thriller",
    "scared 😨": "Horror",
    "surprise 😲": "Mystery",
    "disgust 🤢": "Horror",
    "romantic 😘": "Romance",
    "excited 😦": "Adventure",
    "nostalgic 😇": "History",
}

# List of Emotions
emotions = list(mood_categories.keys())


# User Interaction and Recommendation
def main():
    print("Welcome to the IMDb Mood-based Movie Recommendation Bot!")

    while True:
        print("Available emotions:")
        for idx, emotion in enumerate(emotions, start=1):
            print(f"{idx}. {emotion.capitalize()}")

        user_choice = input("Select your emotion (enter the number): ").strip().lower()

        if user_choice.isdigit() and 1 <= int(user_choice) <= len(emotions):
            selected_emotion = emotions[int(user_choice) - 1]
            recommended_genre = mood_categories[selected_emotion]
            movies = scrape_imdb_movies_by_genre(recommended_genre)
            if movies:
                print(
                    f"Recommended movies to match your mood ({selected_emotion.capitalize()}):"
                )
                for movie in movies:
                    print(f"{movie['number']}. {movie['title']}")
            else:
                print(f"No movies found for the {recommended_genre} genre.")
        else:
            print("Invalid selection. Please choose a valid number.")

        another_recommendation = (
            input("Do you want another recommendation? (y/n): ").strip().lower()
        )
        if another_recommendation != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    # Run the Bot
    main()
