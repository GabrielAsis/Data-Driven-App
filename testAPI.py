import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

urlMoviePopular = "https://api.themoviedb.org/3/trending/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlMoviePopular)

moviePopular = response.json()

with open('popular-movies.json', 'w') as file:
    json.dump(moviePopular, file, indent=4)

# Assuming 'movie_data' is a list of dictionaries
movie_data = moviePopular['results']

# Pick a random movie from the list
random_movie = random.choice(movie_data)

# Create Tkinter window
root = tk.Tk()
root.title("Movie Poster Display")

# Function to fetch and display movie poster
def display_movie_poster(frame, title):
    poster_image_url = f"https://image.tmdb.org/t/p/w500/{random_movie['poster_path']}"
    poster_image_response = requests.get(poster_image_url)
    
    if poster_image_response.status_code == 200:
        # Open the image using PIL
        original_image = Image.open(BytesIO(poster_image_response.content))
        
        # Resize the image to the desired width and height
        resized_image = original_image.resize((300, 450), Image.ANTIALIAS)
        
        # Create a Tkinter-compatible image
        poster_image = ImageTk.PhotoImage(resized_image)
        
        # Create a Tkinter Label to display the resized image
        poster_label = tk.Label(frame, image=poster_image, text=title)
        poster_label.image = poster_image  
        poster_label.pack(padx=10, pady=10)
    else:
        print("Failed to fetch poster image")

# Create frames
main_content = tk.Frame(root, bg="white")
popular_latest = tk.Frame(main_content, bg="white")

# Popular frame
popular_frame = tk.Frame(popular_latest, bg="orange", width=240, height=310)
popular_label = ttk.Label(popular_frame, text="POPULAR", background="orange", foreground="black", font="Arial 16 bold")
display_movie_poster(popular_frame, random_movie['title'])

# Latest frame
latest_frame = tk.Frame(popular_latest, bg="orange", width=240, height=310)
latest_label = ttk.Label(latest_frame, text="LATEST", background="orange", foreground="black", font="Arial 16 bold")

# Place frames
popular_frame.grid(column=0, row=0, padx=100, pady=(50, 0))
latest_frame.grid(column=1, row=0, padx=100, pady=(50, 0))
popular_latest.pack()
main_content.pack()

root.mainloop()
