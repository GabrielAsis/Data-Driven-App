import requests
import json

import requests

query = input("Search: ")

url = f"https://api.themoviedb.org/3/search/multi?query={query}&include_adult=true&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

response = requests.get(url, headers=headers)

search = response.json()

with open('search.json', 'w') as file:
    json.dump(search, file, indent=4)

# Check if there are any results
if 'results' in search and search['results']:
    print(search['results'][0]['title'])
else:
    print("No results.")