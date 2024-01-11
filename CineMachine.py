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

        #fonts
        self.header_font = ("ArchivoBlack-Regular", 32)
        self.header2_font = ("ArchivoBlack-Regular", 30, "bold")
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

        for F in (WelcomePage, HomePage, PopularPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PopularPage)

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
        popular_image_url = f"https://image.tmdb.org/t/p/w500/{randomPopularPoster['poster_path']}"
        popular_image_response = requests.get(popular_image_url)

        original_image = Image.open(BytesIO(popular_image_response.content))
        
        resized_image = original_image.resize((190, 260))
        
        popular_image = ImageTk.PhotoImage(resized_image)

        latest_image_url = f"https://image.tmdb.org/t/p/w500/{randomLatestPoster['poster_path']}"
        latest_image_response = requests.get(latest_image_url)

        original_image = Image.open(BytesIO(latest_image_response.content))
        
        resized_image = original_image.resize((190, 260))
        
        latest_image = ImageTk.PhotoImage(resized_image)

        #popular
        popular_frame = tk.Frame(popular_latest, bg=blue, width=220, height=365)

        popularLabel = ttk.Label(popular_frame, text="POPULAR", background=blue, foreground=text, font=controller.header2_font) 
        popular_poster = tk.Label(popular_frame, image=popular_image, )
        popular_poster.image = popular_image  
        popular_btn = ttk.Button(popular_frame, text="SELECT", style="selectButton.TButton", width=8, command=lambda: controller.show_frame(PopularPage))

        #latest 
        latest_frame = tk.Frame(popular_latest, bg=blue, width=220, height=365)

        latestLabel = ttk.Label(latest_frame, text="LATEST", background=blue, foreground=text, font=controller.header2_font)
        latest_poster = tk.Label(latest_frame, image=latest_image)
        latest_poster.image = latest_image  
        latest_btn = ttk.Button(latest_frame, text="SELECT", style="selectButton.TButton", width=8)

        #placing popular frame
        popular_frame.grid(column=0,row=0, padx=100, pady=(50,0))
        popularLabel.place(relx=0.5,y=35, anchor="center")
        popular_poster.place(relx=0.5,rely=0.55, anchor="center")
        popular_btn.place(relx=0.5,rely=0.96, anchor="center")

        #placing latest frame
        latest_frame.grid(column=1, row=0, padx=100, pady=(50,0))
        latestLabel.place(relx=0.5,y=35, anchor="center")
        latest_poster.place(relx=0.5,rely=0.55, anchor="center")
        latest_btn.place(relx=0.5,rely=0.96, anchor="center")

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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bg)

        #top bar
        top_bar = tk.Frame(self, bg=blue, height=50, width=1000)
        
        back_icon = Image.open('images/back icon.png')
        back_icon = back_icon.convert("RGBA")  
        back_icon.thumbnail((32, 32))  

        self.photo_image = ImageTk.PhotoImage(back_icon)

        back_btn = tk.Label(top_bar, text="back", image=self.photo_image, compound="top", bg=blue, fg=text)

        def on_enter(event):
            back_btn.config(bg="#5D8AA8")

        def on_leave(event):
            back_btn.config(bg=blue)

        def on_click(event):
            print("Label clicked!")

        back_btn.bind("<Enter>", on_enter)
        back_btn.bind("<Leave>", on_leave)
        back_btn.bind("<Button-1>", lambda event: controller.show_frame(HomePage))

        popular_title = tk.Label(top_bar, text="POPULAR", bg=blue, fg=text, font=controller.header2_font)
        
        back_btn.place(x=10, y=0)
        popular_title.place(relx=0.4, rely=0)

        top_bar.pack(side="top", fill="x")

        #popular movies
        popMovies_frame = tk.Frame(self, bg=bg, ) 

        popMovies_label = ttk.Label(popMovies_frame, text="Popular Movies", font=controller.header2_font, background=bg, foreground=text)

        popMovies_container = tk.Frame(popMovies_frame, bg=bg)

        popMovie_1 = tk.Frame(popMovies_container, bg=blue, width=250, height=300)
        popMovie_2 = tk.Frame(popMovies_container, bg=blue, width=250, height=300)
        popMovie_3 = tk.Frame(popMovies_container, bg=blue, width=250, height=300)
        
        popMovies_frame.pack(pady=(20,0))
        popMovies_label.pack(anchor="w", pady=(0,10))
        popMovies_container.pack()
        popMovie_1.grid(column=0, row=2)
        popMovie_2.grid(column=1, row=2, padx=60)
        popMovie_3.grid(column=2, row=2)


app = tkinterApp()
app.config(bg=bg)
app.geometry("1000x650")
app.title("CineMachine")
app.mainloop()
