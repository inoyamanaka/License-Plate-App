import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Make sure to install the Pillow library


import sys

sys.path.append('D:/python/LicensePlateDetector')
from GUI.database.connect_db import LicensePlateDatabase


database = LicensePlateDatabase()


root = tk.Tk()
root.title("Image Scrollbar Example")
root.title("Fullscreen Window")
root.attributes("-fullscreen", True)  

canvas = tk.Canvas(root, background="#1A1A1A", height=800, width=1110)
canvas.grid(row=1, column=1)

nav_frame = tk.Frame(root, bg="#1A1A1A")
nav_frame.grid(row=0, column=0)
nav_frame.place(height=860, width=400)

def refresh():
    root.destroy()
    os.popen("crud.py")
    
def delete_item(index):
    database.delete_record(index)
    refresh

def create_image_scrollbar_app():
    list_filepath = database.get_filepath_list()
    list_filename = database.get_file_name()
    list_filepredict = database.get_file_predict()
    
  
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=1, column=2, sticky=tk.NS)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas, background="#1A1A1A")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    images = []

    for i, image_path in enumerate(list_filepath):
        img = Image.open(image_path)
        img.thumbnail((200, 200))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

        label = tk.Label(frame, image=photo, bg="#1A1A1A")
        label.grid(row=i+1, column=0, padx=5, pady=5, sticky=tk.E)
        
        # Add text next to the image
        text_label = tk.Label(frame, text=f"{list_filename[i]}", fg="white", bg="#1A1A1A", font=("Helvetica", 16))
        text_label.grid(row=i + 1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Add text next to the image
        text_label = tk.Label(frame, text=f"{list_filepredict[i]}", fg="white", bg="#1A1A1A", font=("Helvetica", 16))
        text_label.grid(row=i + 1, column=2, padx=5, pady=5, sticky=tk.W)
        
        # Edit File Button
        button_img2 = ImageTk.PhotoImage(Image.open("GUI/assets/pen.png").resize((30, 30)))
        button2 = tk.Button(frame, image=button_img2, bg="white", bd=0, height=60, width=60)
        button2.grid(row=i + 1, column=3, padx=5, pady=5, sticky=tk.W)
        button2.image = button_img2
        
        # Delete File Button
        button_delete_img = ImageTk.PhotoImage(Image.open("GUI/assets/delete.png").resize((30, 30)))
        button_delete = tk.Button(frame, image=button_delete_img, bg="white", bd=0, height=60, width=60, command=delete_item(i))
        button_delete.grid(row=i + 1, column=4, padx=5, pady=5, sticky=tk.W)
        button_delete.image = button_delete_img 

    frame.update_idletasks()

    canvas.config(scrollregion=canvas.bbox("all"))

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Home Button
    button_home = tk.Button(nav_frame, text='Home',
                            font=("Helvetica", 14),
                            width=20, pady=5, )
    button_home.grid(row=0, column=0,pady=5, sticky="s")

    # ------------------------------------------------------------------------
    # Label Title
    label_titel = tk.LabelFrame(root , text="List of License Plate",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A", height=70, width=1200)
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    label_titel.place(x=400, y=10)

    root.mainloop()
    

# Run the function to create the image scrollbar app
create_image_scrollbar_app()


