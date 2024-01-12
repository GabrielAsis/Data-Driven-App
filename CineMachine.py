import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from PIL import ImageTk, Image  
import requests
import json
from io import BytesIO
import random
from tkinter import font
import os

# Colors
bg = "#111111"
blue = "#8d99ae"
darkBlue = "#616978"
text = "#edf2f4"

#api

#movies
#popular
urlMoviePopular = "https://api.themoviedb.org/3/trending/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlMoviePopular)
moviePopular = response.json()

with open('popular-movies.json', 'w') as file:
    json.dump(moviePopular, file, indent=4)

popularMoviePoster = moviePopular['results']
randomPopularPoster = random.choice(popularMoviePoster)

#top rated
urlMovieTop = "https://api.themoviedb.org/3/movie/top_rated"

headersMovieTop = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

response = requests.get(urlMovieTop, headers=headersMovieTop)

movieTop = response.json()

with open('top-movies.json', 'w') as file:
    json.dump(movieTop, file, indent=4) 

topMoviePoster = movieTop['results']
randomTopPoster = random.choice(topMoviePoster)

#shows
#popular
urlShowPopular = "https://api.themoviedb.org/3/trending/tv/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlShowPopular)
showPopular = response.json()

with open('popular-shows.json', 'w') as file:
    json.dump(showPopular, file, indent=4)

show1 = showPopular['results']

#top rated
urlShowTop = "https://api.themoviedb.org/3/tv/top_rated"

headersShowTop = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

response = requests.get(urlShowTop, headers=headersShowTop)

showTop = response.json()

with open('top-shows.json', 'w') as file:
    json.dump(showTop, file, indent=4) 
 
show1 = showTop['results']

#genre
genreUrl = "https://api.themoviedb.org/3/genre/movie/list?language=en"

genreHeaders = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

genreResponse = requests.get(genreUrl, headers=genreHeaders)

genreMovies = genreResponse.json()

with open('genre-movies.json', 'w') as file:
    json.dump(genreMovies, file, indent=4)



class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)    

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #fonts
        self.header_font = ("Archivo Black", 32)
        self.header2_font = ("Archivo Black", 22)
        self.header3_font = ("Archivo Black", 18)
        self.movie_title = ("Poppins SemiBold", 8)
        self.logo_font = ("PPNeueMachina-PlainUltrabold", 65)
        self.small_logo_font = ("PPNeueMachina-PlainUltrabold", 18)
        self.normal_font= ("Poppins Bold", 11)       
        self.button_font= ("Poppins Bold", 22)       
        self.smaller_button_font= ("Poppins", 10)       
        self.movie_title_font = ("Poppins ExtraBold", 35)
        self.header_details_font = ("Poppins SemiBold", 26)
        self.overview_font= ("Poppins Regular", 11)       

        #styles
        self.style = ttk.Style(self)
        self.style.configure("buttons.TButton", font=self.button_font)
        self.style.configure("searchEntry.TEntry", font=self.normal_font, padding=(4,4))
        self.style.configure("searchButton.TButton", font=self.normal_font, padding=(0,0), width=8)
        self.style.configure("selectButton.TButton", font=self.smaller_button_font, padding=(0,0))
        self.style.configure("TButton", font=self.smaller_button_font, padding=(0,0))
        self.style.configure("genreMenu.TMenubutton", font=self.smaller_button_font, padding=(2,4))

        self.frames = {}

        self.frames["WelcomePage"] = WelcomePage(container, self)
        self.frames["HomePage"] = HomePage(container, self)
        self.frames["PopularPage"] = TemplateListPage(container, self, "POPULAR", "MOVIES", "SHOWS", moviePopular, showPopular)
        self.frames["TopPage"] = TemplateListPage(container, self, "TOP RATED", "MOVIES", "SHOWS", movieTop, showTop)
        self.frames["DetailsPage"] = TemplateDetailsPage(container, self)
        
        self.frames["WelcomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PopularPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["TopPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["DetailsPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("DetailsPage")


    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg)

        def about_message():
            tk.messagebox.showinfo(
                "About",
                "Instructions\n\n1. Click the “Enter App” button to start using App.\n\n2. Select between Popular, Latest, Genre, or Search for a specific Movie/Show\n\n\nDetails of Pages\n\n> Popular - This page shows the top 3 most popular shows and movies.\n\n> Latest - This page shows the top 3 latest shows and movies.\n\n> Genre - Choose a genre, and the page will generate a random movie within that category. You can easily switch genres using a drop-down menu.",
            )

        welcome_to = ttk.Label(self, text="Welcome to", background=bg, foreground=text, font=controller.header_font)
        title = ttk.Label(self, text="CineMachine", background=bg, foreground=text, font=controller.logo_font)
        enter_btn = ttk.Button(self, text="ENTER APP", command=lambda: controller.show_frame("HomePage"), style="buttons.TButton")
        about_btn = ttk.Button(self, text="ABOUT", command=about_message, style="buttons.TButton")

        welcome_to.pack(pady=(65, 0))
        title.pack(pady=0)
        enter_btn.pack(pady=(200, 0))
        about_btn.pack(pady=(50, 0))

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg)

        #top bar
        top_bar = tk.Frame(self, bg=blue, height=50, width=1000)

        logo = ttk.Label(top_bar, text="CineMachine", background=blue, foreground=text, font=controller.small_logo_font)
        search_container = tk.Frame(top_bar, bg=blue)
        search_bar = ttk.Entry(search_container, text="CineMachine", background="white", foreground="black", style="searchEntry.TEntry")        
        search_btn = ttk.Button(search_container, text="SEARCH", style="searchButton.TButton")
        
        logo.place(x=20, rely=0.12)
        search_bar.pack(side="left")
        search_btn.pack(side="left")
        search_container.place(relx=0.4, rely=0.22)

        top_bar.pack(side="top", fill="x")

        #main content of page
        main_content = tk.Frame(self, bg=bg)

        #popular and latest 
        popular_latest = tk.Frame(main_content, bg=bg)
        
        #images
        #popular poster
        popular_image_url = f"https://image.tmdb.org/t/p/w500/{randomPopularPoster['poster_path']}"
        popular_image_response = requests.get(popular_image_url)

        original_image = Image.open(BytesIO(popular_image_response.content))
        
        resized_image = original_image.resize((190, 260))
        
        popular_image = ImageTk.PhotoImage(resized_image)

        #latest poster
        latest_image_url = f"https://image.tmdb.org/t/p/w500/{randomTopPoster['poster_path']}"
        latest_image_response = requests.get(latest_image_url)

        original_image = Image.open(BytesIO(latest_image_response.content))
        
        resized_image = original_image.resize((190, 260))
        
        latest_image = ImageTk.PhotoImage(resized_image)

        def on_enter_frame(event, frame, title):
            frame.config(bg=darkBlue)
            title.config(background=darkBlue)
            frame.config(cursor="hand2")

        def on_leave_frame(event, frame, title):
            frame.config(bg=blue)
            title.config(background=blue)

        #popular
        popular_frame = tk.Frame(popular_latest, bg=blue, width=220, height=365)

        popularLabel = ttk.Label(popular_frame, text="POPULAR", background=blue, foreground=text, font=controller.header2_font) 
        popular_poster = tk.Label(popular_frame, image=popular_image, )
        popular_poster.image = popular_image  

        popular_frame.bind("<Enter>", lambda event: on_enter_frame(event, popular_frame, popularLabel))
        popular_frame.bind("<Leave>", lambda event: on_leave_frame(event, popular_frame, popularLabel))
        popular_frame.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))
        popularLabel.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))
        popular_poster.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))


        #latest 
        latest_frame = tk.Frame(popular_latest, bg=blue, width=220, height=365)

        latestLabel = ttk.Label(latest_frame, text="TOP RATED", background=blue, foreground=text, font=controller.header2_font)
        latest_poster = tk.Label(latest_frame, image=latest_image)
        latest_poster.image = latest_image  

        #placing popular frame
        popular_frame.grid(column=0,row=0, padx=100, pady=(50,0))
        popularLabel.place(relx=0.5,y=35, anchor="center")
        popular_poster.place(relx=0.5,rely=0.55, anchor="center")

        #placing latest frame
        latest_frame.grid(column=1, row=0, padx=100, pady=(50,0))
        latestLabel.place(relx=0.5,y=35, anchor="center")
        latest_poster.place(relx=0.5,rely=0.55, anchor="center")

        latest_frame.bind("<Enter>", lambda event: on_enter_frame(event, latest_frame, latestLabel))
        latest_frame.bind("<Leave>", lambda event: on_leave_frame(event, latest_frame, latestLabel))
        latest_frame.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        latestLabel.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        latest_poster.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        popular_latest.pack()   
        
        #genre
        genreFrame = tk.Frame(main_content, bg=bg)
        genreLabel = ttk.Label(genreFrame, text="GENRE", background=bg, foreground=text, font=controller.header2_font) 
        
        #dropdown menu
        genreMenuFrame = tk.Frame(genreFrame, bg=bg)

        genreMenu = ttk.Combobox(genreMenuFrame, style="genreMenu.TMenubutton", state= "readonly")
        genreMenu['values']=["Select Genre", "Action", "Adventure", "Animation", "Comedy", "Drama", "Fantasy"]
        genreMenu.current(0)
        selected_genre = genreMenu.get()
        
        genreBtn = ttk.Button(genreMenuFrame, text="GENERATE", style="generateButton.TButton")
        
        genreFrame.pack(pady=(50,0))
        genreLabel.pack()
        genreMenuFrame.pack(pady=(15,0))
        genreMenu.grid(column=0, row=0)
        genreBtn.grid(column=1, row=0)

        main_content.pack()

class TemplateListPage(tk.Frame):
    def __init__(self, parent, controller, title_text, movies_label_text, shows_label_text, movieAPI, showAPI):
        tk.Frame.__init__(self, parent, bg=bg)

        self.title_text=title_text
        self.movies_label_text=movies_label_text
        self.shows_label_text=shows_label_text
        self.movieAPI=movieAPI
        self.showAPI=showAPI

        #top bar
        top_bar = tk.Frame(self, bg=blue, height=50, width=1000)
        
        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(top_bar, text="back", image=self.photo_image, compound="top", bg=blue, fg=text)

        def on_enter_backButton(event):
            back_btn.config(bg=darkBlue)
            back_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=blue)


        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        popular_title = tk.Label(top_bar, text=self.title_text, bg=blue, fg=text, font=controller.header2_font)
        
        back_btn.place(x=10, y=0)
        popular_title.place(relx=0.4, rely=0)

        top_bar.pack(side="top", fill="x")

        #popular movies
        popMovies_frame = tk.Frame(self, bg=bg, ) 

        popMovies_label = ttk.Label(popMovies_frame, text=self.movies_label_text, font=controller.header3_font, background=bg, foreground=text)

        popMovies_container = tk.Frame(popMovies_frame, bg=bg)

        #title
        #movies
        popMovieTitle1 = self.movieAPI['results'][0]['title']
        popMovieTitle2 = self.movieAPI['results'][1]['title']
        popMovieTitle3 = self.movieAPI['results'][2]['title']

        #shows
        popShowTitle1 = self.showAPI['results'][0]['name']
        popShowTitle2 = self.showAPI['results'][1]['name']
        popShowTitle3 = self.showAPI['results'][2]['name']

        #images
        #movies
        popMoviePoster1 = self.movieAPI['results'][0]['poster_path']
        popMoviePoster2 = self.movieAPI['results'][1]['poster_path']
        popMoviePoster3 = self.movieAPI['results'][2]['poster_path']
        
        #movies
        popShowPoster1 = self.showAPI['results'][0]['poster_path']
        popShowPoster2 = self.showAPI['results'][1]['poster_path']
        popShowPoster3 = self.showAPI['results'][2]['poster_path']

        #movie poster
        #poster 1
        popular_image_url_1 = f"https://image.tmdb.org/t/p/w500/{popMoviePoster1}"
        popular_image_response_1 = requests.get(popular_image_url_1)

        original_image_1 = Image.open(BytesIO(popular_image_response_1.content))
        resized_image_1 = original_image_1.resize((130, 180))
        popular_poster1 = ImageTk.PhotoImage(resized_image_1)

        #poster 2
        popular_image_url_2 = f"https://image.tmdb.org/t/p/w500/{popMoviePoster2}"
        popular_image_response_2 = requests.get(popular_image_url_2)

        original_image_2 = Image.open(BytesIO(popular_image_response_2.content))
        resized_image_2 = original_image_2.resize((130, 180))
        popular_poster2 = ImageTk.PhotoImage(resized_image_2)

        #poster 3
        popular_image_url_3 = f"https://image.tmdb.org/t/p/w500/{popMoviePoster3}"
        popular_image_response_3 = requests.get(popular_image_url_3)

        original_image_3 = Image.open(BytesIO(popular_image_response_3.content))
        resized_image_3 = original_image_3.resize((130, 180))
        popular_poster3 = ImageTk.PhotoImage(resized_image_3)

        #show posters
        #poster1
        popular_image_url_show1 = f"https://image.tmdb.org/t/p/w500/{popShowPoster1}"
        popular_image_response_show1 = requests.get(popular_image_url_show1)

        original_image_show1 = Image.open(BytesIO(popular_image_response_show1.content))
        resized_image_show1 = original_image_show1.resize((130, 180))
        popular_poster_show1 = ImageTk.PhotoImage(resized_image_show1)

        #poster 2
        popular_image_url_show2 = f"https://image.tmdb.org/t/p/w500/{popShowPoster2}"
        popular_image_response_show2 = requests.get(popular_image_url_show2)

        original_image_show2 = Image.open(BytesIO(popular_image_response_show2.content))
        resized_image_show2 = original_image_show2.resize((130, 180))
        popular_poster_show2 = ImageTk.PhotoImage(resized_image_show2)

        #poster 3
        popular_image_url_show3 = f"https://image.tmdb.org/t/p/w500/{popShowPoster3}"
        popular_image_response_show3 = requests.get(popular_image_url_show3)

        original_image_show3 = Image.open(BytesIO(popular_image_response_show3.content))
        resized_image_show3 = original_image_show3.resize((130, 180))
        popular_poster_show3 = ImageTk.PhotoImage(resized_image_show3)

        popMovie_1 = tk.Frame(popMovies_container, bg=blue, width=150, height=220)
        popular_title1 = ttk.Label(popMovie_1, background=blue, foreground=text, text=popMovieTitle1, font=controller.movie_title, wraplength=150, justify='center')
        popular_image1 = tk.Label(popMovie_1, image=popular_poster1)
        popular_image1.image = popular_poster1

        popMovie_2 = tk.Frame(popMovies_container, bg=blue, width=150, height=220)
        popular_title2 = ttk.Label(popMovie_2, background=blue, foreground=text, text=popMovieTitle2, font=controller.movie_title, wraplength=150, justify='center')
        popular_image2 = tk.Label(popMovie_2, image=popular_poster2)
        popular_image2.image = popular_poster2

        popMovie_3 = tk.Frame(popMovies_container, bg=blue, width=150, height=220)
        popular_title3 = ttk.Label(popMovie_3, background=blue, foreground=text, text=popMovieTitle3, font=controller.movie_title, wraplength=150, justify='center')
        popular_image3 = tk.Label(popMovie_3, image=popular_poster3)
        popular_image3.image = popular_poster3

        popMovies_frame.pack(pady=(20,0))
        popMovies_label.pack(anchor="w", pady=(0,10))
        popMovies_container.pack()

        popMovie_1.grid(column=0, row=2)
        popular_image1.place(relx=0.5, rely=0.56, anchor="center")
        popular_title1.place(relx=0.5, y=16, anchor="center")

        popMovie_2.grid(column=1, row=2, padx=60)
        popular_image2.place(relx=0.5, rely=0.56, anchor="center")
        popular_title2.place(relx=0.5, y=16, anchor="center")

        popMovie_3.grid(column=2, row=2)
        popular_image3.place(relx=0.5, rely=0.56, anchor="center")
        popular_title3.place(relx=0.5, y=16, anchor="center")

        def on_enter_frame(event, frame, title):
            frame.config(bg=darkBlue)
            title.config(background=darkBlue)
            frame.config(cursor="hand2")

        def on_leave_frame(event, frame, title):
            frame.config(bg=blue)
            title.config(background=blue)

        popMovie_1.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_1, popular_title1))
        popMovie_1.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_1, popular_title1))
        popMovie_1.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        popMovie_2.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_2, popular_title2))
        popMovie_2.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_2, popular_title2))
        popMovie_2.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        popMovie_3.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_3, popular_title3))
        popMovie_3.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_3, popular_title3))
        popMovie_3.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))
            
        #popular shows
        popShow_frame = tk.Frame(self, bg=bg, ) 
        popShow_label = ttk.Label(popShow_frame, text=self.shows_label_text, font=controller.header3_font, background=bg, foreground=text)

        popShow_container = tk.Frame(popShow_frame, bg=bg)

        popShow_1 = tk.Frame(popShow_container, bg=blue, width=150, height=220)
        popular_title_show1 = ttk.Label(popShow_1, background=blue, foreground=text, text=popShowTitle1, font=controller.movie_title, wraplength=150, justify='center')
        popular_image_show1 = tk.Label(popShow_1, image=popular_poster_show1)
        popular_image_show1.image = popular_poster_show1

        popShow_2 = tk.Frame(popShow_container, bg=blue, width=150, height=220)
        popular_title_show2 = ttk.Label(popShow_2, background=blue, foreground=text, text=popShowTitle2, font=controller.movie_title, wraplength=150, justify='center')
        popular_image2 = tk.Label(popShow_2, image=popular_poster_show2)
        popular_image2.image = popular_poster_show2

        popShow_3 = tk.Frame(popShow_container, bg=blue, width=150, height=220)
        popular_title_show3 = ttk.Label(popShow_3, background=blue, foreground=text, text=popShowTitle3, font=controller.movie_title, wraplength=150, justify='center')
        popular_image_show3 = tk.Label(popShow_3, image=popular_poster_show3)
        popular_image_show3.image = popular_poster_show3

        popShow_frame.pack(pady=(20,0))
        popShow_label.pack(anchor='w', pady=(0,10))
        popShow_container.pack()

        popShow_1.grid(column=0, row=2)
        popular_image_show1.place(relx=0.5, rely=0.56, anchor="center")
        popular_title_show1.place(relx=0.5, y=16, anchor="center")

        popShow_2.grid(column=1, row=2, padx=60)
        popular_image2.place(relx=0.5, rely=0.56, anchor="center")
        popular_title_show2.place(relx=0.5, y=16, anchor="center")

        popShow_3.grid(column=2, row=2)
        popular_image_show3.place(relx=0.5, rely=0.56, anchor="center")
        popular_title_show3.place(relx=0.5, y=16, anchor="center")

        popShow_1.bind("<Enter>", lambda event: on_enter_frame(event, popShow_1, popular_title_show1))
        popShow_1.bind("<Leave>", lambda event: on_leave_frame(event, popShow_1, popular_title_show1))
        popShow_1.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        popShow_2.bind("<Enter>", lambda event: on_enter_frame(event, popShow_2, popular_title_show2))
        popShow_2.bind("<Leave>", lambda event: on_leave_frame(event, popShow_2, popular_title_show2))
        popShow_2.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        popShow_3.bind("<Enter>", lambda event: on_enter_frame(event, popShow_3, popular_title_show3))
        popShow_3.bind("<Leave>", lambda event: on_leave_frame(event, popShow_3, popular_title_show3))
        popShow_3.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

class TemplateDetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg)

        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(self, text="back", image=self.photo_image, compound="top", bg=bg, fg=text)

        def on_enter_backButton(event):
            back_btn.config(bg="#212121")
            back_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=bg)

        #details
        title = moviePopular['results'][0]['title'] #title
        poster = moviePopular['results'][0]['poster_path'] #poster image
        overview = moviePopular['results'][0]['overview'] #overview
        date = moviePopular['results'][0]['release_date']
        rating = moviePopular['results'][0]['vote_average']
    
        #credits
        id = moviePopular['results'][0]['id']

        url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
        }

        response = requests.get(url, headers=headers)

        credits = response.json()

        with open('credits.json', 'w') as file:
            json.dump(credits, file, indent=4) 

        if 'cast' in credits:
            actors = [member['name'] for member in credits['cast'][:3]]
        else:
            actors = []

        director_name = ', '.join([crew_member["name"] for crew_member in credits["crew"] if crew_member["job"] == "Director"])

        #genre
        genres_map = {genre['id']: genre['name'] for genre in genreMovies['genres']}


        genre_ids = moviePopular['results'][0]['genre_ids']

        genre_names = ', '.join([genres_map[genre_id] for genre_id in genre_ids])

        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))
        back_btn.place(x=0, y=0)

        main_content = tk.Frame(self, bg=bg)

        poster_container = tk.Frame(main_content, width=430, height=580)

        #image  
        poster = f"https://image.tmdb.org/t/p/w500/{poster}"
        poster_response = requests.get(poster)

        poster_image_original = Image.open(BytesIO(poster_response.content))
        poster_resized = poster_image_original.resize((420, 570))
        poster_image = ImageTk.PhotoImage(poster_resized)

        poster_image_label = tk.Label(poster_container, image=poster_image)
        poster_image_label.image = poster_image

        details_container = tk.Frame(main_content, bg=blue, width=430, height=580)
        title_label = ttk.Label(details_container, text=title, background=blue, foreground=text, font=controller.movie_title_font)
        overview_label = ttk.Label(details_container, text="Overview:", background=blue, foreground=text, font=controller.header_details_font)
        overview_label2 = ttk.Label(details_container, text=overview, background=blue, foreground=text, font=controller.overview_font, wraplength=425)
        details_label = ttk.Label(details_container, text="Details:", background=blue, foreground=text, font=controller.header_details_font, wraplength=425)
        details_label2 = ttk.Label(details_container, text=f"Director: {director_name}\nCast: {', '.join(actors)}\nGenre: {genre_names}\nRelease Date: {date}", background=blue, foreground=text, font=controller.overview_font)
        
        poster_container.grid(column=0, row=0, padx=(0,8))
        poster_image_label.place(x=0, y=0, relwidth=1, relheight=1) 

        details_container.grid(column=1, row=0, padx=(8,0))
        title_label.place(x=0, y=-15)
        overview_label.place(x=0, y=70)
        overview_label2.place(x=5, y=120)
        details_label.place(x=5, y=260)
        details_label2.place(x=5, y=310)
        main_content.pack(pady=(25, 0))
app = tkinterApp()
app.config(bg=bg)
app.geometry("1000x650")
app.title("CineMachine")
app.mainloop()
