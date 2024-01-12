import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from PIL import ImageTk, Image  
import requests
import json
from io import BytesIO
import random

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

#latest
urlMovieLatest = "https://api.themoviedb.org/3/latest/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlMoviePopular)
movieLatest = response.json()

with open('latest-movies.json', 'w') as file:
    json.dump(movieLatest, file, indent=4)

latestMoviePoster = movieLatest['results']
randomLatestPoster = random.choice(latestMoviePoster)

#shows
#popular
urlShowPopular = "https://api.themoviedb.org/3/trending/tv/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlShowPopular)
showPopular = response.json()

with open('popular-shows.json', 'w') as file:
    json.dump(showPopular, file, indent=4)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)    

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #fonts
        self.header_font = ("ArchivoBlack-Regular", 32)
        self.header2_font = ("ArchivoBlack-Regular", 30, "bold")
        self.header3_font = ("ArchivoBlack-Regular", 18, "bold")
        self.movie_title = ("ArchivoBlack-Regular", 8, "bold")
        self.logo_font = ("PPNeueMachina-PlainUltrabold", 65)
        self.small_logo_font = ("PPNeueMachina-PlainUltrabold", 18)
        self.normal_font= ("Poppins-Regular", 11, "bold")       
        self.button_font= ("Poppins-Regular", 22, "bold")       
        self.smaller_button_font= ("Poppins-Regular", 10, "bold")       
        
        #styles
        self.style = ttk.Style(self)
        self.style.configure("buttons.TButton", font=self.button_font)
        self.style.configure("searchEntry.TEntry", font=self.normal_font, padding=(4,4))
        self.style.configure("searchButton.TButton", font=self.normal_font, padding=(0,0), width=8)
        self.style.configure("selectButton.TButton", font=self.smaller_button_font, padding=(0,0))
        self.style.configure("TButton", font=self.smaller_button_font, padding=(0,0))
        self.style.configure("genreMenu.TMenubutton", font=self.smaller_button_font, padding=(2,4))

        self.frames = {}

        self.frames[WelcomePage] = WelcomePage(container, self)
        self.frames[HomePage] = HomePage(container, self)
        self.frames[PopularPage] = PopularPage(container, self, "title_text", "movies_label_text", "shows_label_text", moviePopular, showPopular)       
        
        self.frames[WelcomePage].grid(row=0, column=0, sticky="nsew")
        self.frames[HomePage].grid(row=0, column=0, sticky="nsew")
        self.frames[PopularPage].grid(row=0, column=0, sticky="nsew")

        self.show_frame(PopularPage)


    def show_frame(self, frame_index):
        frame = self.frames[frame_index]
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
        enter_btn = ttk.Button(self, text="ENTER APP", command=lambda: controller.show_frame(HomePage), style="buttons.TButton")
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
        latest_image_url = f"https://image.tmdb.org/t/p/w500/{randomLatestPoster['poster_path']}"
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
        popular_frame.bind("<Button-1>", lambda event: controller.show_frame(PopularPage))
        popularLabel.bind("<Button-1>", lambda event: controller.show_frame(PopularPage))
        popular_poster.bind("<Button-1>", lambda event: controller.show_frame(PopularPage))


        #latest 
        latest_frame = tk.Frame(popular_latest, bg=blue, width=220, height=365)

        latestLabel = ttk.Label(latest_frame, text="LATEST", background=blue, foreground=text, font=controller.header2_font)
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
        latest_frame.bind("<Button-1>", lambda event: controller.show_frame(PopularPage))

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

class PopularPage(tk.Frame):
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
            popMovie_1.config(cursor="hand2")

        def on_leave_backButton(event):
            back_btn.config(bg=blue)


        back_btn.bind("<Enter>", on_enter_backButton)
        back_btn.bind("<Leave>", on_leave_backButton)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

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
        popMovie_1.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

        popMovie_2.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_2, popular_title2))
        popMovie_2.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_2, popular_title2))
        popMovie_2.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

        popMovie_3.bind("<Enter>", lambda event: on_enter_frame(event, popMovie_3, popular_title3))
        popMovie_3.bind("<Leave>", lambda event: on_leave_frame(event, popMovie_3, popular_title3))
        popMovie_3.bind("<Button-1>", lambda event: controller.show_frame(HomePage))
            
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
        popShow_1.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

        popShow_2.bind("<Enter>", lambda event: on_enter_frame(event, popShow_2, popular_title_show2))
        popShow_2.bind("<Leave>", lambda event: on_leave_frame(event, popShow_2, popular_title_show2))
        popShow_2.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

        popShow_3.bind("<Enter>", lambda event: on_enter_frame(event, popShow_3, popular_title_show3))
        popShow_3.bind("<Leave>", lambda event: on_leave_frame(event, popShow_3, popular_title_show3))
        popShow_3.bind("<Button-1>", lambda event: controller.show_frame(HomePage))


app = tkinterApp()
app.config(bg=bg)
app.geometry("1000x650")
app.title("CineMachine")
app.mainloop()
