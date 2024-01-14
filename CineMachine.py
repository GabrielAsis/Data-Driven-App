import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from PIL import ImageTk, Image  
from tkinter import PhotoImage
import requests, json, threading, random, os, nltk
from io import BytesIO
from tkinter import font
nltk.download('punkt')

# Colors
bg_color = "#111111"
blue = "#023047"
lightBlue = "#219ebc"
text = "#edf2f4"

#api

#movies
#popular
urlMoviePopular = "https://api.themoviedb.org/3/trending/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlMoviePopular)
moviePopular = response.json()

with open('JSON files/popular-movies.json', 'w') as file:
    json.dump(moviePopular, file, indent=4)


#top rated
urlMovieTop = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=2"

headersMovieTop = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

response = requests.get(urlMovieTop, headers=headersMovieTop)

movieTop = response.json()

with open('JSON files/top-movies.json', 'w') as file:
    json.dump(movieTop, file, indent=4) 

#shows
#popular
urlShowPopular = "https://api.themoviedb.org/3/trending/tv/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlShowPopular)
showPopular = response.json()

with open('JSON files/popular-shows.json', 'w') as file:
    json.dump(showPopular, file, indent=4)

#top rated
urlShowTop = "https://api.themoviedb.org/3/tv/top_rated?language=en-US&page=2"

headersShowTop = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

response = requests.get(urlShowTop, headers=headersShowTop)

showTop = response.json()

with open('JSON files/top-shows.json', 'w') as file:
    json.dump(showTop, file, indent=4) 

#genre movies
genreMovieseUrl = "https://api.themoviedb.org/3/genre/movie/list?language=en"

genreMoviesHeaders = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

genreMovieResponse = requests.get(genreMovieseUrl, headers=genreMoviesHeaders)

genreMovies = genreMovieResponse.json()

with open('JSON files/genre-movies.json', 'w') as file:
    json.dump(genreMovies, file, indent=4)

#genre shows
genrShowseUrl = "https://api.themoviedb.org/3/genre/tv/list?language=en"

genreShowsHeaders = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
}

genreShowResponse = requests.get(genrShowseUrl, headers=genreShowsHeaders)

genreShows = genreShowResponse.json()

with open('JSON files/genre-shows.json', 'w') as file:
    json.dump(genreShows, file, indent=4)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.config(bg=None)

        #fonts
        self.header_font = ("Archivo Black", 25)
        self.header2_font = ("Archivo Black", 28)
        self.header3_font = ("Archivo Black", 18)
        self.movie_title = ("Poppins SemiBold", 10)
        self.logo_font = ("PPNeueMachina-PlainUltrabold", 65)
        self.small_logo_font = ("PPNeueMachina-PlainUltrabold", 18)
        self.normal_font= ("Poppins Bold", 15)
        self.button_font= ("Poppins SemiBold", 23)
        self.smaller_button_font= ("Poppins", 10) 
        self.details_title_font = ("Archivo Black", 25)
        self.header_details_font = ("Poppins SemiBold", 22)
        self.rating_font = ("Poppins Regular", 15)
        self.rating_font_bold = ("Poppins SemiBold", 15)
        self.overview_font= ("Poppins Regular", 13)
        self.details_title_font2 = ("Archivo Black", 22)
        self.header_details_font2 = ("Poppins SemiBold", 19)
        self.rating_font2 = ("Poppins Regular", 12)
        self.rating_font_bold2 = ("Poppins SemiBold", 12)
        self.overview_font2= ("Poppins Regular", 10)

        #styles
        self.style = ttk.Style(self)
        self.style.configure("searchEntry.TEntry", font="Helvetica", size=52, padding=(15,5))

        self.frames = {}

        fire_background = "images/fire background.png"
        star_background = "images/star background.png"

        self.frames["WelcomePage"] = WelcomePage(container, self)
        self.frames["HomePage"] = HomePage(container, self)
        self.frames["PopularPage"] = TemplateListPage(container, self, "POPULAR", "MOVIES", "SHOWS", moviePopular, showPopular, "Popular", "PopularPage", fire_background)
        self.frames["TopPage"] = TemplateListPage(container, self, "TOP RATED", "MOVIES", "SHOWS", movieTop, showTop, "Top", "TopPage", star_background)
        
        self.frames["WelcomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PopularPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["TopPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def create_details_frame(self, container, api, name, index, date, page, genreAPI, media_type):
        if container:
            self.frames["DetailsPage"] = TemplateDetailsPage(container, self, api, name, index, date, page, genreAPI, media_type)
            self.frames["DetailsPage"].grid(row=0, column=0, sticky="nsew")
            self.show_frame("DetailsPage")


    def create_search_frame(self, container, api, index, name, date, genreAPI):
        if container:
            self.frames["SearchResultsPage"] = SearchResultsPage(container, self, api, index, name, date, genreAPI)
            self.frames["SearchResultsPage"].grid(row=0, column=0, sticky="nsew")
            self.show_frame("SearchResultsPage")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg_color)

        self.bg_image= PhotoImage(file="images/Background Image.png")
        self.bg_label_welcome = ttk.Label(self, image=self.bg_image, background=bg_color)
        self.bg_label_welcome.place(relwidth=1, relheight=1)

        def about_message():
            tk.messagebox.showinfo(
                "About",
                "Instructions\n\n1. Click the \"START\" button to start using App.\n\n2. Select between Popular, Top Rated or Search for a specific Movie/Show using the search bar\n\n\nDetails of Pages\n\n> Popular - This page displays three random popular movies and shows of the week. Select one from the six options to view its information, Additionally click the \'RANDOM\' button to randomize movies and shows displayed.\n\n> Top Rated - This page displays three random highest rated movies and shows of all time. Select one from the six options to view its information, Additionally click the \'RANDOM\' button to randomize movies and shows displayed.\n\n>Search Results - After entering your desired movie or show in the entry field, you will be directed to this page where details of the selected movie or show are displayed. You can explore additional results by clicking the 'Next' or 'Previous' buttons\n\n\nMADE BY\nGabriel Gono Asis",
            )
        
        welcome_to = ttk.Label(self, text="Welcome to", background=bg_color, foreground=text, font=controller.header_font)
        logo = Image.open('images/cinemachine logo.png')
        logo.thumbnail((350, 350))  
        self.logo_image = ImageTk.PhotoImage(logo)
        logo = tk.Label(self, image=self.logo_image, bg=bg_color)

        start_black = Image.open('images/start black.png')
        start_black.thumbnail((25, 25))  
        self.start_image_black = ImageTk.PhotoImage(start_black)

        start_white = Image.open('images/start white.png')
        start_white.thumbnail((25, 25))  
        self.start_image_white = ImageTk.PhotoImage(start_white)

        start_btn = tk.Button(self, text="START", image=self.start_image_black, compound="left", command=lambda: controller.show_frame("HomePage"), font=controller.button_font, background="white", foreground="black", relief="flat", width=150, height=50)
        
        info_black = Image.open('images/info black.png')
        info_black.thumbnail((25, 25))  
        self.info_image_black = ImageTk.PhotoImage(info_black)

        info_white = Image.open('images/info white.png')
        info_white.thumbnail((25, 25))  
        self.info_image_white = ImageTk.PhotoImage(info_white)

        about_btn = tk.Button(self, text="ABOUT", image=self.info_image_black, compound="left", command=about_message, font=controller.button_font, background="white", foreground="black", relief="flat", width=150, height=50)
        
        def on_enter(event, button, image):
            button.config(bg=blue)
            button.config(fg=text)
            button.config(image=image)
            button.config(cursor="hand2")
            
        def on_leave(event, button, image):
            button.config(bg="white")
            button.config(fg="black")
            button.config(image=image)

        start_btn.bind("<Enter>", lambda event: on_enter(event, start_btn, self.start_image_white))
        start_btn.bind("<Leave>", lambda event: on_leave(event, start_btn, self.start_image_black))

        about_btn.bind("<Enter>", lambda event: on_enter(event, about_btn, self.info_image_white))
        about_btn.bind("<Leave>", lambda event: on_leave(event, about_btn, self.info_image_black))

        welcome_to.pack(pady=(16, 0))
        logo.pack()
        start_btn.pack(pady=(30, 0))
        about_btn.pack(pady=(35, 0))

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg_color)

        #top bar
        top_bar = tk.Frame(self, bg=blue, height=55, width=1000)

        logo = Image.open('images/cinemachine logo.png')
        logo.thumbnail((55, 55))  
        self.logo_image = ImageTk.PhotoImage(logo)
        logo = tk.Label(top_bar, image=self.logo_image, bg=blue)

        search_container = tk.Frame(top_bar, bg=blue)
        search_bar = ttk.Entry(search_container, text="CineMachine", background="white", foreground="black", style="searchEntry.TEntry")        
        search_bar.insert(0, 'Search')

        search_bar.bind('<FocusIn>', lambda event: search_bar.delete(0, 'end'))  # Clear the placeholder text when focused

        def search(event):

            query = search_bar.get()

            url = f"https://api.themoviedb.org/3/search/multi?query={query}&include_adult=true&language=en-US&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
            }

            response = requests.get(url, headers=headers)

            search = response.json()

            with open('JSON files/search.json', 'w') as file:
                json.dump(search, file, indent=4)

            if 'results' in search and search['results']:
                search_media_type = search['results'][0]['media_type']
                if search_media_type == 'movie':
                    title = search['results'][0]['title']
                    date = search['results'][0]['release_date']
                    genreAPI = genreMovies
                elif search_media_type == 'tv':
                    title = search['results'][0]['name']
                    date = search['results'][0]['first_air_date']
                    genreAPI = genreShows
            else:
                print("DEBUG: No Results Found")
                tk.messagebox.showerror("ERROR", "No Results Found :(\n\nTry being more specific")


            create_search_frame(parent,search, 0, title, date, genreAPI)

        def create_search_frame(parent,search, index, title, date, genreAPI):
            controller.create_search_frame(parent,search, index, title, date, genreAPI)
        
        search_btn = Image.open('images/search icon.png')
        search_btn = search_btn.convert("RGBA")  
        search_btn.thumbnail((26, 26))  

        self.photo_image = ImageTk.PhotoImage(search_btn)

        search_btn = tk.Label(search_container, image=self.photo_image, compound="top", bg="white", fg="black")
        
        def on_enter_backButton(event):
            search_btn.config(bg="lightgray")
            search_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            search_btn.config(bg="white")

        search_btn.bind("<Enter>", on_enter_backButton)
        search_btn.bind("<Leave>", on_leave_backButton)
        search_btn.bind("<Button-1>", search)
        search_bar.bind("<Return>", search)

        logo.place(x=30, rely=0.5, anchor="center")
        search_bar.pack(side="left")
        search_btn.pack(side="left")
        search_container.place(relx=0.5, rely=0.5, anchor="center")

        top_bar.pack(side="top", fill="x")

        #main content of page
        main_content = tk.Frame(self, bg=bg_color)

        instruction_label = tk.Label(main_content, text="Select One", font=controller.header2_font, bg=bg_color, fg=text)
        instruction_label.pack(pady=(30,0))

        #popular and top 
        popular_top = tk.Frame(main_content, bg=bg_color)
        
        #popular poster
        popular_image_original = Image.open('images/fire icon.png')
        popular_image_original.thumbnail((260, 260))  

        self.popular_image = ImageTk.PhotoImage(popular_image_original)

        #top poster
        top_image_original = Image.open('images/top rated.png')
        top_image_original.thumbnail((260, 260))  

        self.top_image = ImageTk.PhotoImage(top_image_original)

        def on_enter_frame(event, frame, title, poster, border):
            frame.config(bg=lightBlue)
            title.config(background=lightBlue)
            poster.config(background=lightBlue)
            border.config(background="white")
            frame.config(cursor="hand2")
            title.config(cursor="hand2")
            poster.config(cursor="hand2")

        def on_leave_frame(event, frame, title, poster, border):
            frame.config(bg=blue)
            title.config(background=blue)
            poster.config(background=blue)
            border.config(background=lightBlue)

        #popular
        border1_frame = tk.Frame(popular_top, bg=lightBlue, width=324, height=374)
        popular_frame = tk.Frame(border1_frame, bg=blue, width=320, height=370)

        popularLabel = ttk.Label(popular_frame, text="POPULAR", background=blue, foreground=text, font=controller.header2_font) 
        popular_poster = tk.Label(popular_frame, image=self.popular_image, bg=blue)
        popular_poster.image = self.popular_image  

        popular_frame.bind("<Enter>", lambda event: on_enter_frame(event, popular_frame, popularLabel, popular_poster, border1_frame))
        popular_frame.bind("<Leave>", lambda event: on_leave_frame(event, popular_frame, popularLabel, popular_poster, border1_frame))
        popular_frame.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))
        popularLabel.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))
        popular_poster.bind("<Button-1>", lambda event: controller.show_frame("PopularPage"))

        #top 
        border2_frame = tk.Frame(popular_top, bg=lightBlue, width=324, height=374)
        top_frame = tk.Frame(border2_frame, bg=blue, width=320, height=370)

        topLabel = ttk.Label(top_frame, text="TOP RATED", background=blue, foreground=text, font=controller.header2_font)
        top_poster = tk.Label(top_frame, image=self.top_image, bg=blue)
        top_poster.image = self.top_image  

        #placing popular frame
        border1_frame.grid(column=0,row=0, padx=100, pady=(50,0))
        popular_frame.place(relx=0.5,rely=0.5, anchor="center")
        popularLabel.place(relx=0.5,y=35, anchor="center")
        popular_poster.place(relx=0.5,rely=0.6, anchor="center")

        #placing top frame
        border2_frame.grid(column=1,row=0, padx=100, pady=(50,0))
        top_frame.place(relx=0.5,rely=0.5, anchor="center")
        topLabel.place(relx=0.5,y=35, anchor="center")
        top_poster.place(relx=0.5,rely=0.6, anchor="center")

        top_frame.bind("<Enter>", lambda event: on_enter_frame(event, top_frame, topLabel, top_poster, border2_frame))
        top_frame.bind("<Leave>", lambda event: on_leave_frame(event, top_frame, topLabel, top_poster, border2_frame))
        top_frame.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        topLabel.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        top_poster.bind("<Button-1>", lambda event: controller.show_frame("TopPage"))
        popular_top.pack()   
        
        main_content.pack()

class TemplateListPage(tk.Frame):
    def __init__(self, parent, controller, title_text, movies_label_text, shows_label_text, movieAPI, showAPI, category, page, back_image_path):        
        tk.Frame.__init__(self, parent, bg=bg_color)
        self.title_text=title_text
        self.movies_label_text=movies_label_text
        self.shows_label_text=shows_label_text
        self.movieAPI=movieAPI
        self.showAPI=showAPI
        self.category=category
        self.page=page

        self.bg_image= PhotoImage(file=back_image_path)
        self.bg_label= ttk.Label(self, image=self.bg_image, background=bg_color)
        self.bg_label.place(relwidth=1, relheight=1)

        #top bar
        top_bar = tk.Frame(self, bg=blue, height=50, width=1000)
        
        #back_icon
        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(top_bar, text="back", image=self.photo_image, compound="top", bg=blue, fg=text)

        def on_enter_backButton(event):
            back_btn.config(bg=lightBlue)
            back_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=blue)


        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))

        back_btn.place(x=10, y=0)

        #random generator
        random_icon = Image.open('images/random.png')
        random_icon = random_icon.convert("RGBA")  
        random_icon.thumbnail((32, 32))  

        self.random_image = ImageTk.PhotoImage(random_icon)

        random_btn = tk.Label(top_bar, text="random", image=self.random_image, compound="top", bg=blue, fg=text)

        def on_enter_randomButton(event):
            random_btn.config(bg=lightBlue)
            random_btn.config(cursor="hand2")

        def on_leave_randomButton(event):
            random_btn.config(bg=blue)


        random_btn.bind("<Enter>", on_enter_randomButton)
        random_btn.bind("<Leave>", on_leave_randomButton)
        random_btn.bind("<Button-1>", self.create_random_indexes)

        random_btn.place(relx=0.95, y=0)

        popular_title = tk.Label(top_bar, text=self.title_text, bg=blue, fg=text, font=controller.header2_font)
        popular_title.place(relx=0.5, rely=0.5, anchor="center")

        top_bar.pack(side="top", fill="x")

        #popular movies
        popMovies_frame = tk.Frame(self, bg=bg_color, ) 

        popMovies_label = ttk.Label(popMovies_frame, text=self.movies_label_text, font=controller.header3_font, background=bg_color, foreground=text)

        popMovies_container = tk.Frame(popMovies_frame, bg=bg_color)

        movie_indexes = self.random_movie_indexes(movieAPI['results'])
        show_indexes = self.random_show_indexes(showAPI['results'])

        self.random_movie_index1 = movie_indexes[0]
        self.random_movie_index2 = movie_indexes[1]
        self.random_movie_index3 = movie_indexes[2]

        self.random_show_index1 = show_indexes[0]
        self.random_show_index2 = show_indexes[1]
        self.random_show_index3 = show_indexes[2]

        #title
        #movies
        self.popMovieTitle1 = self.movieAPI['results'][self.random_movie_index1]['title']
        self.popMovieTitle2 = self.movieAPI['results'][self.random_movie_index2]['title']
        self.popMovieTitle3 = self.movieAPI['results'][self.random_movie_index3]['title']

        #shows
        self.popShowTitle1 = self.showAPI['results'][self.random_show_index1]['name']
        self.popShowTitle2 = self.showAPI['results'][self.random_show_index2]['name']
        self.popShowTitle3 = self.showAPI['results'][self.random_show_index3]['name']

        #images
        #movies
        self.popMoviePoster1 = self.movieAPI['results'][self.random_movie_index1]['poster_path']
        self.popMoviePoster2 = self.movieAPI['results'][self.random_movie_index2]['poster_path']
        self.popMoviePoster3 = self.movieAPI['results'][self.random_movie_index3]['poster_path']
        
        #movies
        self.popShowPoster1 = self.showAPI['results'][self.random_show_index1]['poster_path']
        self.popShowPoster2 = self.showAPI['results'][self.random_show_index2]['poster_path']
        self.popShowPoster3 = self.showAPI['results'][self.random_show_index3]['poster_path']

        #movie poster
        #poster 1
        popular_image_url_1 = f"https://image.tmdb.org/t/p/w500/{self.popMoviePoster1}"
        popular_image_response_1 = requests.get(popular_image_url_1)

        original_image_1 = Image.open(BytesIO(popular_image_response_1.content))
        resized_image_1 = original_image_1.resize((130, 180))
        self.popular_poster1 = ImageTk.PhotoImage(resized_image_1)

        #poster 2
        popular_image_url_2 = f"https://image.tmdb.org/t/p/w500/{self.popMoviePoster2}"
        popular_image_response_2 = requests.get(popular_image_url_2)

        original_image_2 = Image.open(BytesIO(popular_image_response_2.content))
        resized_image_2 = original_image_2.resize((130, 180))
        self.popular_poster2 = ImageTk.PhotoImage(resized_image_2)

        #poster 3
        popular_image_url_3 = f"https://image.tmdb.org/t/p/w500/{self.popMoviePoster3}"
        popular_image_response_3 = requests.get(popular_image_url_3)

        original_image_3 = Image.open(BytesIO(popular_image_response_3.content))
        resized_image_3 = original_image_3.resize((130, 180))
        self.popular_poster3 = ImageTk.PhotoImage(resized_image_3)

        #show posters
        #poster1
        popular_image_url_show1 = f"https://image.tmdb.org/t/p/w500/{self.popShowPoster1}"
        popular_image_response_show1 = requests.get(popular_image_url_show1)

        original_image_show1 = Image.open(BytesIO(popular_image_response_show1.content))
        resized_image_show1 = original_image_show1.resize((130, 180))
        self.popular_poster_show1 = ImageTk.PhotoImage(resized_image_show1)

        #poster 2
        popular_image_url_show2 = f"https://image.tmdb.org/t/p/w500/{self.popShowPoster2}"
        popular_image_response_show2 = requests.get(popular_image_url_show2)

        original_image_show2 = Image.open(BytesIO(popular_image_response_show2.content))
        resized_image_show2 = original_image_show2.resize((130, 180))
        self.popular_poster_show2 = ImageTk.PhotoImage(resized_image_show2)

        #poster 3
        popular_image_url_show3 = f"https://image.tmdb.org/t/p/w500/{self.popShowPoster3}"
        popular_image_response_show3 = requests.get(popular_image_url_show3)

        original_image_show3 = Image.open(BytesIO(popular_image_response_show3.content))
        resized_image_show3 = original_image_show3.resize((130, 180))
        self.popular_poster_show3 = ImageTk.PhotoImage(resized_image_show3)

        #movie list
        border1_frame = tk.Frame(popMovies_container, bg=lightBlue, width=154, height=224)
        popMovie_1 = tk.Frame(border1_frame, bg=blue, width=150, height=220)
        self.popular_title1 = ttk.Label(popMovie_1, background=blue, foreground=text, text=self.shorten_text(self.popMovieTitle1), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image1 = tk.Label(popMovie_1, image=self.popular_poster1)
        self.popular_image1.image = self.popular_poster1

        border2_frame = tk.Frame(popMovies_container, bg=lightBlue, width=154, height=224)
        popMovie_2 = tk.Frame(border2_frame, bg=blue, width=150, height=220)
        self.popular_title2 = ttk.Label(popMovie_2, background=blue, foreground=text, text=self.shorten_text(self.popMovieTitle2), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image2 = tk.Label(popMovie_2, image=self.popular_poster2)
        self.popular_image2.image = self.popular_poster2

        border3_frame = tk.Frame(popMovies_container, bg=lightBlue, width=154, height=224)
        popMovie_3 = tk.Frame(border3_frame, bg=blue, width=150, height=220)
        self.popular_title3 = ttk.Label(popMovie_3, background=blue, foreground=text, text=self.shorten_text(self.popMovieTitle3), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image3 = tk.Label(popMovie_3, image=self.popular_poster3)
        self.popular_image3.image = self.popular_poster3

        popMovies_frame.pack(pady=(10,0))
        popMovies_label.pack(anchor="w", pady=(0,6))
        popMovies_container.pack()
        
        border1_frame.grid(column=0, row=2)
        popMovie_1.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image1.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title1.place(relx=0.5, y=16, anchor="center")

        border2_frame.grid(column=1, row=2, padx=10)
        popMovie_2.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image2.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title2.place(relx=0.5, y=16, anchor="center")

        border3_frame.grid(column=2, row=2)
        popMovie_3.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image3.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title3.place(relx=0.5, y=16, anchor="center")

        def on_enter_frame(event, frame, title):
            frame.config(bg=lightBlue)
            title.config(background=lightBlue)
            frame.config(cursor="hand2")

        def on_leave_frame(event, frame, title):
            frame.config(bg=blue)
            title.config(background=blue)

        popMovie_1.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_1, self.popular_title1))
        popMovie_1.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_1, self.popular_title1))
        popMovie_1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index1, "release_date", page, genreMovies, "movie"))
        self.popular_image1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index1, "release_date", page, genreMovies, "movie"))
        self.popular_title1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index1, "release_date", page, genreMovies, "movie"))

        popMovie_2.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_2, self.popular_title2))
        popMovie_2.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_2, self.popular_title2))
        popMovie_2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index2, "release_date", page, genreMovies, "movie"))
        self.popular_image2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index2, "release_date", page, genreMovies, "movie"))
        self.popular_title2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index2, "release_date", page, genreMovies, "movie"))

        popMovie_3.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_3, self.popular_title3))
        popMovie_3.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_3, self.popular_title3))
        popMovie_3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index3, "release_date", page, genreMovies, "movie"))
        self.popular_image3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index3, "release_date", page, genreMovies, "movie"))
        self.popular_title3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, movieAPI, "title", self.random_movie_index3, "release_date", page, genreMovies, "movie"))
            
        #popular shows
        popShow_frame = tk.Frame(self, bg=bg_color, ) 
        popShow_label = ttk.Label(popShow_frame, text=self.shows_label_text, font=controller.header3_font, background=bg_color, foreground=text)

        popShow_container = tk.Frame(popShow_frame, bg=bg_color)

        border4_frame = tk.Frame(popShow_container, bg=lightBlue, width=154, height=224)
        popShow_1 = tk.Frame(border4_frame, bg=blue, width=150, height=220)
        self.popular_title_show1 = ttk.Label(popShow_1, background=blue, foreground=text, text=self.shorten_text(self.popShowTitle1), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image_show1 = tk.Label(popShow_1, image=self.popular_poster_show1)
        self.popular_image_show1.image = self.popular_poster_show1

        border5_frame = tk.Frame(popShow_container, bg=lightBlue, width=154, height=224)
        popShow_2 = tk.Frame(border5_frame, bg=blue, width=150, height=220)
        self.popular_title_show2 = ttk.Label(popShow_2, background=blue, foreground=text, text=self.shorten_text(self.popShowTitle2), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image_show2 = tk.Label(popShow_2, image=self.popular_poster_show2)
        self.popular_image_show2.image = self.popular_poster_show2

        border6_frame = tk.Frame(popShow_container, bg=lightBlue, width=154, height=224)
        popShow_3 = tk.Frame(border6_frame, bg=blue, width=150, height=220)
        self.popular_title_show3 = ttk.Label(popShow_3, background=blue, foreground=text, text=self.shorten_text(self.popShowTitle3), font=controller.movie_title, wraplength=150, justify='center')
        self.popular_image_show3 = tk.Label(popShow_3, image=self.popular_poster_show3)
        self.popular_image_show3.image = self.popular_poster_show3

        popShow_frame.pack(pady=(20,0))
        popShow_label.pack(anchor='w', pady=(0,10))
        popShow_container.pack()

        border4_frame.grid(column=0, row=2)
        popShow_1.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image_show1.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title_show1.place(relx=0.5, y=16, anchor="center")

        border5_frame.grid(column=1, row=2, padx=10)
        popShow_2.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image_show2.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title_show2.place(relx=0.5, y=16, anchor="center")

        border6_frame.grid(column=2, row=2)
        popShow_3.place(relx=0.5, rely=0.5, anchor="center")
        self.popular_image_show3.place(relx=0.5, rely=0.56, anchor="center")
        self.popular_title_show3.place(relx=0.5, y=16, anchor="center")

        popShow_1.bind("<Enter>", lambda event: on_enter_frame(event, popShow_1, self.popular_title_show1))
        popShow_1.bind("<Leave>", lambda event: on_leave_frame(event, popShow_1, self.popular_title_show1))
        popShow_1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index1, "first_air_date", page, genreShows, "tv"))
        self.popular_image_show1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index1, "first_air_date", page, genreShows, "tv"))
        self.popular_title_show1.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index1, "first_air_date", page, genreShows, "tv"))

        popShow_2.bind("<Enter>", lambda event: on_enter_frame(event, popShow_2, self.popular_title_show2))
        popShow_2.bind("<Leave>", lambda event: on_leave_frame(event, popShow_2, self.popular_title_show2))
        popShow_2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index2, "first_air_date", page, genreShows, "tv"))
        self.popular_image_show2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index2, "first_air_date", page, genreShows, "tv"))
        self.popular_title_show2.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index2, "first_air_date", page, genreShows, "tv"))

        popShow_3.bind("<Enter>", lambda event: on_enter_frame(event, popShow_3, self.popular_title_show3))
        popShow_3.bind("<Leave>", lambda event: on_leave_frame(event, popShow_3, self.popular_title_show3))
        popShow_3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index3, "first_air_date", page, genreShows, "tv"))
        self.popular_image_show3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index3, "first_air_date", page, genreShows, "tv"))
        self.popular_title_show3.bind("<Button-1>", lambda event: controller.create_details_frame(parent, showAPI, "name", self.random_show_index3, "first_air_date", page, genreShows, "tv"))
                

        def create_details_frame(parent, api, name, index, date, page, genreAPI, media_type):
            controller.create_details_frame(parent, api, name, index, date, page, genreAPI, media_type)

    def create_random_indexes(self, event):
        movie_indexes = self.random_movie_indexes(self.movieAPI['results'])
        show_indexes = self.random_show_indexes(self.showAPI['results'])

        self.update_display_with_random_indexes(movie_indexes, show_indexes)

    def update_display_with_random_indexes(self, movie_indexes, show_indexes):
        # Update display with random indexes for movies
        self.random_movie_index1, self.random_movie_index2, self.random_movie_index3 = movie_indexes
        popMovieTitle1, popMovieTitle2, popMovieTitle3 = (
            self.movieAPI['results'][self.random_movie_index1]['title'],
            self.movieAPI['results'][self.random_movie_index2]['title'],
            self.movieAPI['results'][self.random_movie_index3]['title']
        )
        popMoviePoster1, popMoviePoster2, popMoviePoster3 = (
            self.movieAPI['results'][self.random_movie_index1]['poster_path'],
            self.movieAPI['results'][self.random_movie_index2]['poster_path'],
            self.movieAPI['results'][self.random_movie_index3]['poster_path']
        )
        self.update_display_for_movies(popMovieTitle1, popMovieTitle2, popMovieTitle3,
                                       popMoviePoster1, popMoviePoster2, popMoviePoster3)

        # Update display with random indexes for shows
        self.random_show_index1, self.random_show_index2, self.random_show_index3 = show_indexes
        popShowTitle1, popShowTitle2, popShowTitle3 = (
            self.showAPI['results'][self.random_show_index1]['name'],
            self.showAPI['results'][self.random_show_index2]['name'],
            self.showAPI['results'][self.random_show_index3]['name']
        )
        popShowPoster1, popShowPoster2, popShowPoster3 = (
            self.showAPI['results'][self.random_show_index1]['poster_path'],
            self.showAPI['results'][self.random_show_index2]['poster_path'],
            self.showAPI['results'][self.random_show_index3]['poster_path']
        )
        self.update_display_for_shows(popShowTitle1, popShowTitle2, popShowTitle3,
                                       popShowPoster1, popShowPoster2, popShowPoster3)

    def update_display_for_movies(self, title1, title2, title3, poster1, poster2, poster3):
        self.popular_title1.config(text=self.shorten_text(title1))
        self.popular_title2.config(text=self.shorten_text(title2))
        self.popular_title3.config(text=self.shorten_text(title3))

        self.update_image_widget(self.popular_image1, poster1)
        self.update_image_widget(self.popular_image2, poster2)
        self.update_image_widget(self.popular_image3, poster3)

    def update_display_for_shows(self, title1, title2, title3, poster1, poster2, poster3):
        self.popular_title_show1.config(text=self.shorten_text(title1))
        self.popular_title_show2.config(text=self.shorten_text(title2))
        self.popular_title_show3.config(text=self.shorten_text(title3))

        self.update_image_widget(self.popular_image_show1, poster1)
        self.update_image_widget(self.popular_image_show2, poster2)
        self.update_image_widget(self.popular_image_show3, poster3)

    def update_image_widget(self, image_widget, poster_path):
        image_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        image_response = requests.get(image_url)

        original_image = Image.open(BytesIO(image_response.content))
        resized_image = original_image.resize((130, 180))
        updated_image = ImageTk.PhotoImage(resized_image)

        image_widget.config(image=updated_image)
        image_widget.image = updated_image

    def random_movie_indexes(self, movieAPI):
        movieIndexes = set()

        while len(movieIndexes) < 3:
            random_index = random.randint(0, len(movieAPI) - 1)
            movieIndexes.add(random_index)

        return list(movieIndexes)

    def random_show_indexes(self, showAPI):
        showIndexes = set()

        while len(showIndexes) < 3:
            random_index = random.randint(0, len(showAPI) - 1)
            showIndexes.add(random_index)

        return list(showIndexes)
    
    def shorten_text(self, text):
        if len(text) > 23:
            return text[:22-3] + "..."
        else:
            return text 
     
class TemplateDetailsPage(tk.Frame):
    def __init__(self, parent, controller, api, name, index, date, page, genreAPI, media_type):        
        tk.Frame.__init__(self, parent, bg=bg_color)

        self.bg_image= PhotoImage(file="images/Background Image.png")
        self.bg_label_welcome = ttk.Label(self, image=self.bg_image, background=bg_color)
        self.bg_label_welcome.place(relwidth=1, relheight=1)

        self.api=api
        self.name=name
        self.index=index
        self.page=page
        self.genreAPI=genreAPI
        self.media_type=media_type

        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(self, text="back", image=self.photo_image, compound="top", bg=bg_color, fg=text)

        def on_enter_backButton(event):
            back_btn.config(bg="#212121")
            back_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=bg_color)

        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame(page))
        back_btn.place(x=0, y=0)

        #details
        title = api['results'][index][name] #title
        poster = api['results'][index]['poster_path'] #poster image
        overview = api['results'][index]['overview'].split("\n\n")[0] #overview
        date = api['results'][index][date] #release date
        rating = api['results'][index]['vote_average'] #vote average
    
        #credits
        id = api['results'][index]['id']

        if media_type == "movie":
            url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"
        elif media_type == "tv":
            url = f"https://api.themoviedb.org/3/tv/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
        }

        response = requests.get(url, headers=headers)

        credits = response.json()

        with open(f"JSON files/credits-{media_type}.json", 'w') as file:
            json.dump(credits, file, indent=4)

        if 'cast' in credits:
            actors = [member['name'] for member in credits['cast'][:5]]
        else:
            actors = []

        #genre
        genres_map = {genre['id']: genre['name'] for genre in genreAPI['genres']}

        genre_ids = api['results'][index]['genre_ids']

        genre_names = [genres_map[genre_id] for genre_id in genre_ids]

        main_content = tk.Frame(self, bg=bg_color)

        poster_container = tk.Frame(main_content, width=430, height=580)

        #image  
        poster = f"https://image.tmdb.org/t/p/w500/{poster}"
        poster_response = requests.get(poster)

        poster_image_original = Image.open(BytesIO(poster_response.content))
        poster_resized = poster_image_original.resize((420, 570))
        poster_image = ImageTk.PhotoImage(poster_resized)

        poster_image_label = tk.Label(poster_container, image=poster_image)
        poster_image_label.image = poster_image

        rating_container = tk.Frame(poster_container, bg=blue)
        rating_label = ttk.Label(rating_container, text="Rating: ", background=blue, foreground=text, font=controller.rating_font_bold)
        rating_label2 = ttk.Label(rating_container, text=f"{rating}", background=blue, foreground=text, font=controller.rating_font)

        details_container = tk.Frame(main_content, bg=blue, width=430, height=580)

        title_label = tk.Label(details_container, text=title.upper(), background=blue, foreground=text, font=controller.details_title_font, wraplength=430, justify="center")
        overview_container = tk.Frame(details_container, background=blue)
        overview_label = ttk.Label(overview_container, text="Overview:", background=blue, foreground=text, font=controller.header_details_font)
        overview_label2 = ttk.Label(overview_container, text=overview, background=blue, foreground=text, font=controller.overview_font, wraplength=425)
        details_frame = tk.Frame(details_container, background=blue)
        details_label = ttk.Label(details_frame, text="Details:", background=blue, foreground=text, font=controller.header_details_font)
        details_label2 = ttk.Label(details_frame, text=f"Cast: {', '.join(actors)}\nGenre: {', '.join(genre_names)}\nRelease Date: {date}", background=blue, foreground=text, font=controller.overview_font, wraplength=425)
        
        poster_container.grid(column=0, row=0, padx=(0,8))
        poster_image_label.place(x=0, y=0, relwidth=1, relheight=1) 

        rating_container.place(x=5, y=535)
        rating_label.grid(column=0,row=0)
        rating_label2.grid(column=1,row=0)

        details_container.grid(column=1, row=0, padx=(8,0))
        title_label.place(relx=0.5, y=40, anchor="center")
        overview_container.place(x=5, rely=0.15)
        overview_label.pack(anchor="w", pady=0)
        overview_label2.pack(anchor="w", pady=0)
        details_frame.place(x=5, rely=0.6)
        details_label.pack(anchor="w", pady=0)
        details_label2.pack(anchor="w", pady=0)

        main_content.pack(pady=(25, 0))

class SearchResultsPage(tk.Frame):
    def __init__(self, parent, controller, api, index, name, date, genreAPI):
        tk.Frame.__init__(self, parent, bg=bg_color)

        self.bg_image= PhotoImage(file="images/Background Image.png")
        self.bg_label_welcome = ttk.Label(self, image=self.bg_image, background=bg_color)
        self.bg_label_welcome.place(relwidth=1, relheight=1)

        self.api=api
        self.index=index
        self.name=name
        self.genreAPI=genreAPI

        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(self, text="back", image=self.photo_image, compound="top", bg=bg_color, fg=text)

        def on_enter_backButton(event):
            back_btn.config(bg="#212121")
            back_btn.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=bg_color)

        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame("HomePage"))
        back_btn.place(x=0, y=0)

        media_type= api['results'][index]['media_type']

        #details
        poster = api['results'][index]['poster_path'] #poster image

        overview_text = api['results'][index]['overview'] 
        sentences = nltk.sent_tokenize(overview_text)
        overview = ' '.join(sentences[:3]) #overview

        rating = api['results'][index]['vote_average'] #vote average
    
        #credits
        id = api['results'][index]['id']

        if media_type == "movie":
            creditsUrl = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"
        elif media_type == "tv":
            creditsUrl = f"https://api.themoviedb.org/3/tv/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
        }

        creditsResponse = requests.get(creditsUrl, headers=headers)

        credits = creditsResponse.json()

        with open(f"JSON files/credits-{media_type}.json", 'w') as file:
            json.dump(credits, file, indent=4)

        if 'cast' in credits:
            actors = [member['name'] for member in credits['cast'][:5]]
        else:
            actors = []

        #genre
        genres_map = {genre['id']: genre['name'] for genre in genreAPI['genres']}
        genre_ids = api['results'][index]['genre_ids']
        genre_names = [genres_map[genre_id] for genre_id in genre_ids]

        #all details
        main_content = tk.Frame(self, bg=bg_color)

        poster_container = tk.Frame(main_content, width=400, height=550)

        #image  
        poster = f"https://image.tmdb.org/t/p/w500/{poster}"
        poster_response = requests.get(poster)

        poster_image_original = Image.open(BytesIO(poster_response.content))
        poster_resized = poster_image_original.resize((390, 540))
        poster_image = ImageTk.PhotoImage(poster_resized)

        self.poster_image_label = tk.Label(poster_container, image=poster_image)
        self.poster_image_label.image = poster_image

        rating_container = tk.Frame(poster_container, bg=blue)
        rating_label = ttk.Label(rating_container, text="Rating: ", background=blue, foreground=text, font=controller.rating_font_bold2)
        self.rating_label2 = ttk.Label(rating_container, text=f"{rating}", background=blue, foreground=text, font=controller.rating_font2)

        details_container = tk.Frame(main_content, bg=blue, width=400, height=550) 

        self.title_label = tk.Label(details_container, text=name.upper(), background=blue, foreground=text, font=controller.details_title_font2, wraplength=400, justify="center")
        overview_container = tk.Frame(details_container, background=blue)
        overview_label = ttk.Label(overview_container, text="Overview:", background=blue, foreground=text, font=controller.header_details_font2)
        self.overview_label2 = ttk.Label(overview_container, text=overview, background=blue, foreground=text, font=controller.overview_font2, wraplength=395)
        details_frame = tk.Frame(details_container, background=blue)
        details_label = ttk.Label(details_frame, text="Details:", background=blue, foreground=text, font=controller.header_details_font2)
        self.details_label2 = ttk.Label(details_frame, text=f"Cast: {', '.join(actors)}\nGenre: {', '.join(genre_names)}\nRelease Date: {date}", background=blue, foreground=text, font=controller.overview_font2, wraplength=395)
        
        navigation_container = tk.Frame(self, background=bg_color)

        prev_icon = Image.open('images/prev.png')
        prev_icon = prev_icon.convert("RGBA")  
        prev_icon.thumbnail((32, 32))  

        
        next_icon = Image.open('images/next.png')
        next_icon = next_icon.convert("RGBA")  
        next_icon.thumbnail((32, 32))  

        self.prev_image = ImageTk.PhotoImage(prev_icon)

        self.next_image = ImageTk.PhotoImage(next_icon)

        self.prev_btn = tk.Label(navigation_container, text="Previous", image=self.prev_image, compound="top", bg=blue, fg=text, width=50, height=50)
        self.next_btn = tk.Label(navigation_container, text="Next", image=self.next_image, compound="top", bg=blue, fg=text, width=50, height=50)

        def on_enter_nav(button, event):
            button.config(bg=lightBlue)
            button.config(cursor="hand2")

        def on_leave_nav(button, event):
            button.config(bg=blue)

        self.next_btn.bind("<Enter>", lambda event: on_enter_nav(self.next_btn, event))
        self.next_btn.bind("<Leave>", lambda event: on_leave_nav(self.next_btn, event))
        self.next_btn.bind("<Button-1>", lambda event: self.next_prev_result(event, direction="next"))

        self.prev_btn.bind("<Enter>", lambda event: on_enter_nav(self.prev_btn, event))
        self.prev_btn.bind("<Leave>", lambda event: on_leave_nav(self.prev_btn, event))
        self.prev_btn.bind("<Button-1>", lambda event: self.next_prev_result(event, direction="prev"))

        self.prev_btn.grid(column=0,row=0, padx=(0,315))
        self.next_btn.grid(column=1,row=0, padx=(315,0))

        poster_container.grid(column=0, row=0, padx=(0,8))
        self.poster_image_label.place(x=0, y=0, relwidth=1, relheight=1) 
        rating_container.place(x=5, y=514)
        rating_label.grid(column=0,row=0)
        self.rating_label2.grid(column=1,row=0)

        details_container.grid(column=1, row=0, padx=(8,0))
        self.title_label.place(relx=0.5, y=40, anchor="center")
        overview_container.place(x=5, rely=0.14)
        overview_label.pack(anchor="w", pady=0)
        self.overview_label2.pack(anchor="w", pady=0)
        details_frame.place(x=5, rely=0.65)
        details_label.pack(anchor="w", pady=0)
        self.details_label2.pack(anchor="w", pady=0)

        main_content.pack(pady=(25, 0))
        navigation_container.pack(pady=(10,0))

        self.next_prev_result(None)

    def update_content(self):
        current_result = self.api['results'][self.index]

        title = current_result.get('title') or current_result.get('name')
        overview = current_result.get('overview')
        poster = current_result.get('poster_path')
        date = current_result.get('release_date') or current_result.get('first_air_date')
        rating = current_result.get('vote_average')

        id = current_result.get('id')
        media_type = current_result.get('media_type')

        if media_type == "movie":
            credits_url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"
        elif media_type == "tv":
            credits_url = f"https://api.themoviedb.org/3/tv/{id}/credits?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjRjZDJlNWU0MzE5M2Y1MzliOTRhNzBiNmVlODQ4MyIsInN1YiI6IjY1NzZlMDE3ZTkzZTk1MjE4ZGNiOGU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.P81gH5DvyfmZmeIgCooIa-9Cf2UJmacUG2kimCKH1QQ"
        }

        credits_response = requests.get(credits_url, headers=headers)

        credits = credits_response.json()

        with open(f"JSON files/credits-{media_type}.json", 'w') as file:
            json.dump(credits, file, indent=4)

        if 'cast' in credits:
            actors = [member['name'] for member in credits['cast'][:5]]
        else:
            actors = []

        if media_type == "movie":
            genreAPI = genreMovies
        elif media_type == "tv":
           genreAPI = genreShows

        genres_map = {genre['id']: genre['name'] for genre in genreAPI['genres']}
        genre_ids = current_result.get('genre_ids', [])
        genre_names = [genres_map[genre_id] for genre_id in genre_ids]
        
        self.title_label.config(text=title.upper())
        self.overview_label2.config(text=overview)
        self.details_label2.config(text=f"Cast: {', '.join(actors)}\nGenre: {', '.join(genre_names)}\nRelease Date: {date}")
        self.rating_label2.config(text=f"{rating}")

        poster = f"https://image.tmdb.org/t/p/w500/{poster}"
        poster_response = requests.get(poster)
        poster_image_original = Image.open(BytesIO(poster_response.content))
        poster_resized = poster_image_original.resize((390, 540))
        poster_image = ImageTk.PhotoImage(poster_resized)
        self.poster_image_label.config(image=poster_image)
        self.poster_image_label.image = poster_image

    def next_prev_result(self, event, direction=None):
        if direction == "next":
            self.index += 1
        elif direction == "prev":
            self.index -= 1

        self.index = max(0, min(self.index, len(self.api['results']) - 1))

        self.update_content()

        if self.index == len(self.api['results']) - 1:
            self.next_btn.grid_remove()  
        else:
            self.next_btn.grid()

        if self.index == 0:
            self.prev_btn.grid_remove() 
        else:
            self.prev_btn.grid() 

app = tkinterApp()
app.geometry("1000x650")
app.title("CineMachine")
app.resizable(width=False, height=False)
app.mainloop()
