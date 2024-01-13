import requests
import json

# Function to get genre ID from genre name
def get_genre_id(genre_name):
    genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    genre_headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
    }
    response = requests.get(genre_url, headers=genre_headers)
    genres = response.json().get("genres", [])
    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None

# Get user input for genre
user_genre = input("Enter a movie genre: ")

# Get genre ID
genre_id = get_genre_id(user_genre)

if genre_id is not None:
    # Use the discovered genre ID in the discover movie API
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre_id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
    }
    
    response = requests.get(url, headers=headers)
    
    # Display movie information
    movies = response.json().get("results", [])
    if movies:
        for movie in movies:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    else:
        print("No movies found for the given genre.")
else:
    print("Genre not found.")
