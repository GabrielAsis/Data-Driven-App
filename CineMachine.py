import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image  
import requests
import json
from io import BytesIO
import random

# Colors
bg = "#111111"
orange = "#8d99ae"
text = "#edf2f4"

#api
urlMoviePopular = "https://api.themoviedb.org/3/trending/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"


response = requests.get(urlMoviePopular)
moviePopular = response.json()

popularMoviePoster = moviePopular['results']
randomPopularPoster = random.choice(popularMoviePoster)


with open('popular-movies.json', 'w') as file:
    json.dump(moviePopular, file, indent=4)

urlMovieLatest = "https://api.themoviedb.org/3/latest/movie/week?api_key=7b4cd2e5e43193f539b94a70b6ee8483"

response = requests.get(urlMoviePopular)
movieLatest = response.json()

with open('latest-movies.json', 'w') as file:
    json.dump(movieLatest, file, indent=4)

latestMoviePoster = movieLatest['results']
randomLatestPoster = random.choice(latestMoviePoster)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.header_font = ("ArchivoBlack-Regular", 32)
        self.header2_font = ("ArchivoBlack-Regular", 30, "bold")
        self.logo_font = ("PPNeueMachina-PlainUltrabold", 65)
        self.small_logo_font = ("PPNeueMachina-PlainUltrabold", 18)
        self.normal_font= ("Poppins-Regular", 12, "bold")       
        self.button_font= ("Poppins-Regular", 22, "bold")       


        self.style = ttk.Style(self)
        self.style.configure("buttons.TButton", font=self.button_font)
        self.style.configure("searchButton.TButton", font=self.normal_font, padding=(0,0))

        self.frames = {}

        for F in (WelcomePage, HomePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
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

        welcome_to.pack(pady=(50, 0))
        title.pack(pady=0)
        enter_btn.pack(pady=(200, 0))
        about_btn.pack(pady=(50, 0))

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg)

        #top bar
        top_bar = tk.Frame(self, bg=orange, height=50)

        logo = ttk.Label(top_bar, text="CineMachine", background=orange, foreground=text, font=controller.small_logo_font)
        search_container = tk.Frame(top_bar, bg=orange)
        search_bar = ttk.Entry(search_container, text="CineMachine", background="white", foreground="black", font=controller.normal_font, )        
        search_btn = ttk.Button(search_container, text="SEARCH", style="searchButton.TButton")
        
        logo.pack(side="left", padx=(10,0))
        search_bar.pack(side="left")
        search_btn.pack(side="left")
        search_container.pack(pady=10, padx=(0,150))

        top_bar.pack(side="top", fill="x")

        #main content of page
        main_content = tk.Frame(self, bg=bg)

        #popular and latest 
        popular_latest = tk.Frame(main_content, bg=bg)
        
        #images
        popular_image_url = f"https://image.tmdb.org/t/p/w500/{randomPopularPoster['poster_path']}"
        popular_image_response = requests.get(popular_image_url)

        original_image = Image.open(BytesIO(popular_image_response.content))
        
        resized_image = original_image.resize((200, 270), Image.ANTIALIAS)
        
        popular_image = ImageTk.PhotoImage(resized_image)

        latest_image_url = f"https://image.tmdb.org/t/p/w500/{randomLatestPoster['poster_path']}"
        latest_image_response = requests.get(latest_image_url)

        original_image = Image.open(BytesIO(latest_image_response.content))
        
        resized_image = original_image.resize((200, 270), Image.ANTIALIAS)
        
        latest_image = ImageTk.PhotoImage(resized_image)


        #popular
        popular_frame = tk.Frame(popular_latest, bg=orange, width=260, height=370)
        popularLabel = ttk.Label(popular_frame, text="POPULAR", background=orange, foreground=text, font=controller.header2_font) 
        popular_poster = tk.Label(popular_frame, image=popular_image)
        popular_poster.image = popular_image  

        #latest 
        latest_frame = tk.Frame(popular_latest, bg=orange, width=260, height=370)
        latestLabel = ttk.Label(latest_frame, text="LATEST", background=orange, foreground=text, font=controller.header2_font)
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

        popular_latest.pack()   
        main_content.pack()
app = tkinterApp()
app.config(bg=bg)
app.geometry("1000x650")
app.mainloop()
