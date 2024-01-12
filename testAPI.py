# Assuming genreMovies is the variable containing genre details
genres_map = {genre['id']: genre['name'] for genre in genreMovies['genres']}

# Assuming moviePopular is the variable containing movie details
# Get genre_ids from movie details
genre_ids = moviePopular['results'][0]['genre_ids']

# Map genre_ids to genre names
genre_names = [genres_map[genre_id] for genre_id in genre_ids]

# Print the result
print(f"Genre IDs: {genre_ids}")
print(f"Genre Names: {genre_names}")