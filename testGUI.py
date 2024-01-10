import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a frame with relative height and width
frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)

# Inside the frame, create a label with relative height and width
label = tk.Label(frame, text="Relative Label", bg="white")
label.place(relx=0.1, rely=0.1, relheight=5, relwidth=0.8)

root.mainloop()
