import tkinter as tk
from PIL import Image, ImageTk

def on_enter(event):
    label.config(bg="lightgray")

def on_leave(event):
    label.config(bg="white")

def on_click(event):
    print("Label clicked!")

root = tk.Tk()

# Load the ICO file using Pillow
ico_image = Image.open('images/back.ico')
ico_image = ico_image.convert("RGBA")  # Convert to RGBA format
ico_image.thumbnail((32, 32))  # Resize if needed

# Create a PhotoImage from the Pillow image
photo_image = ImageTk.PhotoImage(ico_image)

# Create a label with the icon
label = tk.Label(root, image=photo_image, bg="white")
label.pack(padx=10, pady=10)

# Bind events to the label
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)
label.bind("<Button-1>", on_click)

root.mainloop()
