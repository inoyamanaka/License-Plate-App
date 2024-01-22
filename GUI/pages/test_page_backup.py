import asyncio
import os
import threading
import time
import tkinter as tk
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image  
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile 
from tkinter.ttk import Progressbar
from tkinter import filedialog
from prettytable import PrettyTable

import sys
sys.path.append('D:/python/license-plate-application')
from GUI.database.connect_db import LicensePlateDatabase
from GUI.services.single_test_detection import LicensePlateProcessor
from GUI.services.multi_test_detection import MultiLicensePlateProcessor

# --------------------------------------------
future_image_path = ''
database = LicensePlateDatabase()
processor = LicensePlateProcessor()
multi_processor = MultiLicensePlateProcessor()
    
# ---------------------------------------------

# from GUI.pages.home_page import FullscreenApp
ws = tk.Tk()
ws.title("Fullscreen Window")
ws.attributes("-fullscreen", True)  

# ---------------------------------------------
list_of_filename = []
list_of_filename_predict = []
# ---------------------------------------------
label_titel = tk.LabelFrame()
label_new = tk.Label()
label_new_2 = tk.Label()
label_new_3 = tk.Label()
label_new_4 = tk.Label()

button_next = tk.Button()

nav_frame = tk.Frame(ws, bg="#1A1A1A")
nav_frame.grid(row=0, column=0)
nav_frame.place(height=860, width=600)

content_frame = tk.Frame(ws, bg="#1A1A1A")
content_frame.grid(row=0, column=1 )
content_frame.place(height=860, width=1400, x=350)

box_nav = tk.LabelFrame(nav_frame, bg="#1A1A1A", height=250)
box_nav.grid(row=0, column=0)


def prevPage(master):
    master.destroy()
    import GUI.pages.home_page as home_page
    
def save_to(): 
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    
    filepath = asksaveasfile(filetypes = files, defaultextension = files) 
    return filepath

def exit_fullscreen(self, event):
    ws.attributes("-fullscreen", False)
    

def create_preview_img():
    global label_new, label_new_2, label_new_3, label_new_4, label_titel, future_image_path
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()

    file = askopenfile(filetypes=[('Image Files', '*.jpeg;*.jpg;*.png')])
    future_image_path = file.name
    
    
    # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Data Preview",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A", height=50, width=1920,)
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    
    # Create an object of tkinter ImageTk
    original_image = Image.open(future_image_path)
    resized_image = original_image.resize((700, 800))
    img = ImageTk.PhotoImage(resized_image)

    # Create a Label Widget to display the text or Image
    label_new = tk.Label(content_frame, image = img, height=700, width=800, background="#1A1A1A")
    label_new.grid(row=1, column=1,pady=5)
    label_new.place(x=150, y=90)
    label_new.image = img
    

def preprocessing_stage():
    global label_new, label_new_2, label_new_3, label_new_4, label_titel, button_next, future_image_path
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
    # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Preprocessing Stage",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A",height=80, width=1200, )
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    
    label_new = tk.LabelFrame(content_frame, text="1. Image Cropping",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A",height=80, width=900, )
    label_new.grid(row=1, column=1,pady=(20,0), padx=5)
    label_new.place(x=19, y=160)  
    label_new.config(image=None)
    

    label_new_2 =tk.LabelFrame(content_frame, text="2. Skew correction",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A",height=80, width=900, )
    label_new_2.grid(row=2, column=1,pady=(10,0), padx=5)
    label_new_2.place(x=19, y=250)  
    label_new_2.config(image=None)


    label_new_3 = tk.LabelFrame(content_frame, text="3. Character Detection with OCR",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A",height=80, width=900, )
    label_new_3.grid(row=3, column=1,pady=(10,0), padx=5)
    label_new_3.place(x=19, y=350)  
    label_new_3.config(image=None)
    
    
     # Home Button
    button_next = tk.Button(content_frame, text='Next',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=do_preprocessing)
    button_next.grid(row=4, column=1,pady=5)
    button_next.place(y=750, x=860)


    label.place(x=10, y=60,width=0, height=0)
    
def do_preprocessing():
    global processor
    processor = LicensePlateProcessor()
    # multi_processor = MultiLicensePlateProcessor()
    processor.process_image(future_image_path, os.path.basename(future_image_path))
    preprocessing_1()
    
def preprocessing_1():
    global label_new, label_new_2, label_new_3, label_new_4,  label_titel, button_next, label, future_image_path
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
    # Testing parameter
    
     # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Preprocessing Stage 1",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A", height=50, width=900,)
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    
    # Create an object of tkinter ImageTk
    original_image = Image.open(f"GUI/outputs/single/cropped_img/cropped_image_{os.path.basename(future_image_path)}")
    resized_image = original_image.resize((900, 450))
    img = ImageTk.PhotoImage(resized_image)

    # Create a Label Widget to display the text or Image
    label_new = tk.Label(content_frame, image = img, height=450, width=900, background="#1A1A1A")
    label_new.grid(row=1, column=1,pady=5)
    label_new.place(x=150, y=160)
    label_new.image = img
        
    # label_new = tk.Label(content_frame,text='Test pre1').grid(row=1, column=1,pady=(10,0), padx=5)
    # label_new.place(x=19, y=160)  
    
    label_new_2 = tk.Label()
    label_new_3 = tk.Label()
    label_new_4 = tk.Label()

    # Previous Button
    button_prev = tk.Button(content_frame, text='Prev',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=preprocessing_stage)
    button_prev.grid(row=4, column=1,pady=5)
    button_prev.place(y=750, x=600)
    
     # Next Button
    button_next = tk.Button(content_frame, text='Next',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=preprocessing_2)
    button_next.grid(row=4, column=2,pady=5)
    button_next.place(y=750, x=860)

def preprocessing_2():
    global label_new, label_new_2, label_new_3, label_new_4,  label_titel, button_next
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
     # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Preprocessing Stage 2",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A", height=50, width=900,)
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    
    # Create an object of tkinter ImageTk
    original_image = Image.open(f"GUI/outputs/single/angle_fix_img/gambar_lurus_{os.path.basename(future_image_path)}")
    resized_image = original_image.resize((900, 450))
    img = ImageTk.PhotoImage(resized_image)
    
    # Create a Label Widget to display the text or Image
    label_new = tk.Label(content_frame, image = img, height=450, width=900, background="#1A1A1A")
    label_new.grid(row=1, column=1,pady=5)
    label_new.place(x=150, y=160)
    label_new.image = img
        
    # label_new = tk.Label(content_frame,text='Test pre1').grid(row=1, column=1,pady=(10,0), padx=5)
    # label_new.place(x=19, y=160)  
    
    label_new_2 = tk.Label()
    label_new_3 = tk.Label()
    label_new_4 = tk.Label()
    
    # Previous Button
    button_prev = tk.Button(content_frame, text='Prev',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=preprocessing_1)
    button_prev.grid(row=4, column=1,pady=5)
    button_prev.place(y=750, x=600)
    
     # Next Button
    button_next = tk.Button(content_frame, text='Next',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=preprocessing_3)
    button_next.grid(row=4, column=2,pady=5)
    button_next.place(y=750, x=860)
    
    

def preprocessing_3():
    global label_new, label_new_2, label_new_3, label_new_4,  label_titel, button_next, label
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
     # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Preprocessing Stage 3",
                            font=("Helvetica", 16), fg="white",
                                background="#1A1A1A", height=50, width=900,)
    # Label Title
    label_titel.grid(row=0, column=1,pady=5)
    
    # Create an object of tkinter ImageTk
    original_image = Image.open(f"GUI/outputs/single/final_img/text_draw_{os.path.basename(future_image_path)}")
    resized_image = original_image.resize((700, 1200))
    img = ImageTk.PhotoImage(resized_image)

    # Create a Label Widget to display the text or Image
    label_new = tk.Label(content_frame, image = img, height=650, width=750, background="#1A1A1A")
    label_new.grid(row=1, column=1,pady=5)
    label_new.place(x=150, y=60)
    label_new.image = img
        
    # label_new = tk.Label(content_frame,text='Test pre1').grid(row=1, column=1,pady=(10,0), padx=5)
    # label_new.place(x=19, y=160)  
    
    label_new_2 = tk.Label()
    label_new_3 = tk.Label()
    label_new_4 = tk.Label()

    
    # Previous Button
    button_prev = tk.Button(content_frame, text='Prev',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=preprocessing_2)
    button_prev.grid(row=4, column=1,pady=5)
    button_prev.place(y=750, x=600)
    
     # Next Button
    button_next = tk.Button(content_frame, text='Finish',
                            font=("Helvetica", 14),
                            width=20, pady=5, command=result_preview_img)
    button_next.grid(row=4, column=2,pady=5)
    button_next.place(y=750, x=860)



def pilih_folder():
    global list_of_filename, list_of_filename_predict
    folder_selected = filedialog.askdirectory()
    
    try:
        files = os.listdir(folder_selected)
        for file in files:
            file_path = os.path.join(folder_selected, file)
            if os.path.isfile(file_path):
                character =  multi_processor.process_image(f"{folder_selected}/{file}", filename=file_path)
                list_of_filename.append(file)
                list_of_filename_predict.append(character)
            elif os.path.isdir(file_path):
                print("Folder:", file)
                
        table = PrettyTable()
        table.field_names = ["File Index", "Filename", "Predicted FIlename"]
        for index, file_path in enumerate(list_of_filename, start=0):
            table.add_row([index, list_of_filename[index], list_of_filename_predict[index]])
        filepath = save_to()
        save_table_to_txt(table, filepath.name, 'test_output.txt')
        


    except Exception as e:
        print("Error:", str(e))
    

def result_preview_img():
    global label_new, label_new_2, label_new_3, label_new_4,  label_titel, button_next
    label_titel.destroy()
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    button_next.destroy()
    
    plate_character = processor.get_character()
    database.insert_record(os.path.basename(future_image_path), plate_character, future_image_path)
    
    # Label Title
    label_titel = tk.LabelFrame(content_frame, text="Testing Result",  font=("Helvetica", 20),height=80, fg='white', width=900,         
                                background="#1A1A1A",labelanchor="n")
    # Label Title
    label_titel.grid(row=0, column=0,pady=5)
    label_titel.place(x=150, y=0)
    
    original_image = Image.open(f"GUI/outputs/single/final_img/text_draw_{os.path.basename(future_image_path)}")
    resized_image = original_image.resize((700, 800))
    img = ImageTk.PhotoImage(resized_image)

    # Create a Label Widget to display the text or Image
    label_new = tk.Label(content_frame, image = img, height=700, width=1000, background="#1A1A1A")
    label_new.grid(row=1, column=1,pady=5)
    label_new.place(x=150, y=90)
    label_new.image = img
    
    label_new_2 = tk.LabelFrame(content_frame, text=plate_character,  font=("Helvetica", 20),height=80, fg='white', width=900,         
                                background="#1A1A1A",labelanchor="n")
    label_new_2.grid(row=2, column=1,pady=5)
    label_new_2.place(x=150, y=750)
    
     # Next Button
    button_next.grid(row=4, column=2,pady=5)
    button_next.place(y=0, x=0)

    
def save_table_to_txt(table, output_folder, output_file='list_of_license_plate.txt'):
    output_file_path = os.path.join(output_folder, output_file)
    
    with open(output_file_path, 'w') as f:
        f.write(str(table))

# Choose File Button
button_file = tk.Button(nav_frame, text='Pilih File',
                        font=("Helvetica", 14),
                        width=20,pady=5, command=create_preview_img)
button_file.grid(row=1, column=0,pady=5,padx=80)

# Choose File Button
button_folder = tk.Button(nav_frame, text='Pilih Folder',
                        font=("Helvetica", 14),
                        width=20,pady=5, command=pilih_folder)
button_folder.grid(row=2, column=0,pady=5,padx=80)

# Training Button
button_train = tk.Button(nav_frame, text='Preprocessing',
                            font=("Helvetica", 14),
                        width=20, pady=5, command=preprocessing_stage)
button_train.grid(row=3, column=0,pady=5)

# Result Button
button_result = tk.Button(nav_frame, text='Testing Result',
                        font=("Helvetica", 14),
                        width=20, pady=5, command=result_preview_img)
button_result.grid(row=4, column=0,pady=5)

# Home Button
button_home = tk.Button(nav_frame, text='Home',
                        font=("Helvetica", 14),
                        width=20, pady=5,  command=lambda: prevPage(ws))
button_home.grid(row=5, column=0,pady=5, sticky="s")

# ------------------------------------------------------------------------
# Label Title
label_titel = tk.LabelFrame(content_frame, text="Dataset Preview",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A", height=50, width=2800)
# Label Title
label_titel.grid(row=0, column=0,pady=5)
label_titel.place(x=10, y=10)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("GUI/assets/folder.png"))

# Create a Label Widget to display the text or Image
label = tk.Label(content_frame, image = img, height=900, width=1400, background="#1A1A1A")
label.grid(row=1, column=0,pady=5)
label.place(x=10, y=60)

ws.mainloop()
