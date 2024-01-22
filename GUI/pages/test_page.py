import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile, askdirectory
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from prettytable import PrettyTable
from tkinter import messagebox


sys.path.append('D:/python/license-plate-application')
from GUI.pages.home_page import HomePage
from GUI.database.connect_db import LicensePlateDatabase
# from GUI.services.single_test_detection import LicensePlateProcessor
# from GUI.services.multi_test_detection import MultiLicensePlateProcessor

class TestLicensePlateApp:
    def __init__(self, master, single_preprocess, multi_preprocess):
        self.master = master
        self.master.title("License Plate Application")
        self.master.attributes("-fullscreen", True)

        self.list_of_filename = []
        self.list_of_filename_predict = []

        self.database = LicensePlateDatabase()
        self.processor = single_preprocess
        self.multi_processor = multi_preprocess

        self.label_titel = tk.LabelFrame()
        self.label_new = tk.Label()
        self.label_new_2 = tk.Label()
        self.label_new_3 = tk.Label()
        self.label_new_4 = tk.Label()

        self.button_next = tk.Button()

        self.nav_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.nav_frame.grid(row=0, column=0)
        self.nav_frame.place(height=860, width=600)

        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.create_ui()

    def create_ui(self):
          # ------------------------------------------------------------------------
        # Label Title
        self.label_titel = tk.LabelFrame(self.content_frame, text="Dataset Preview",
                                         font=("Helvetica", 16), fg="white",
                                         background="#1A1A1A", height=50, width=2800)
        # Label Title
        self.label_titel.grid(row=0, column=0,pady=5)
        self.label_titel.place(x=10, y=10)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("GUI/assets/folder.png"))

        # Create a Label Widget to display the text or Image
        self.label = tk.Label(self.content_frame, image = img, height=900, width=1400, background="#1A1A1A")
        self.label.grid(row=1, column=0,pady=5)
        self.label.place(x=10, y=60)
        
        # Choose File Button
        button_file = tk.Button(self.nav_frame, text='Pilih File',
                                font=("Helvetica", 14),
                                width=20,pady=5, command=lambda: self.create_preview_img())
        button_file.grid(row=1, column=0,pady=5,padx=80)

        # Choose Folder Button
        button_folder = tk.Button(self.nav_frame, text='Pilih Folder',
                                  font=("Helvetica", 14),
                                  width=20,pady=5, command=self.choose_folder)
        button_folder.grid(row=2, column=0,pady=5,padx=80)

        # Training Button
        button_train = tk.Button(self.nav_frame, text='Preprocessing',
                                 font=("Helvetica", 14),
                                 width=20, pady=5, command=lambda: self.preprocessing_stage())
        button_train.grid(row=3, column=0,pady=5)

        # Result Button
        button_result = tk.Button(self.nav_frame, text='Testing Result',
                                  font=("Helvetica", 14),
                                  width=20, pady=5, command=lambda: self.result_preview_img())
        button_result.grid(row=4, column=0,pady=5)

        # Home Button
        button_home = tk.Button(self.nav_frame, text='Home',
                                font=("Helvetica", 14),
                                width=20, pady=5,  command=self.prev_page)
        button_home.grid(row=5, column=0,pady=5, sticky="s")

        self.content_frame.update_idletasks()
        
        
        self.master.mainloop()

    def prev_page(self):
        self.master.destroy()
        root = tk.Tk()
        HomePage(root, single_preprocess=self.processor, multi_preprocess=self.multi_processor)

    def save_to(self):
        files = [('Text Document', '*.txt')]

        filepath = asksaveasfile(filetypes=files, defaultextension=files)
        return filepath

    def exit_fullscreen(self, event):
        self.master.attributes("-fullscreen", False)

    def create_preview_img(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.label_titel = tk.LabelFrame(self.content_frame, text="Data Preview",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=1920, )

        self.label_titel.grid(row=0, column=1, pady=5)

        self.label_new.config(image=None)

        file = askopenfile(filetypes=[('Image Files', '*.jpeg;*.jpg;*.png')])
        self.future_image_path = file.name

        # Label Title
        self.label_titel = tk.LabelFrame(self.content_frame, text="Data Preview",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=1920, )
        # Label Title
        self.label_titel.grid(row=0, column=1, pady=5)

        # Create an object of tkinter ImageTk
        original_image = Image.open(self.future_image_path)
        resized_image = original_image.resize((700, 800))
        img = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        self.label_new = tk.Label(self.content_frame, image=img, height=700, width=800, background="#1A1A1A")
        self.label_new.grid(row=1, column=1, pady=5)
        self.label_new.place(x=150, y=90)
        self.label_new.image = img
        
        self.content_frame.update_idletasks()

    def preprocessing_stage(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.label_titel = tk.LabelFrame(self.content_frame, text="Preprocessing Stage",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=80, width=1200, )
        self.label_titel.grid(row=0, column=1, pady=5)

        self.label_new = tk.LabelFrame(self.content_frame, text="1. Image Cropping",
                                  font=("Helvetica", 16), fg="white",
                                  background="#1A1A1A", height=80, width=900, )
        self.label_new.grid(row=1, column=1, pady=(20, 0), padx=5)
        self.label_new.place(x=19, y=160)
        self.label_new.config(image=None)

        self.label_new_2 = tk.LabelFrame(self.content_frame, text="2. Skew correction",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=80, width=900, )
        self.label_new_2.grid(row=2, column=1, pady=(10, 0), padx=5)
        self.label_new_2.place(x=19, y=250)
        self.label_new_2.config(image=None)

        self.label_new_3 = tk.LabelFrame(self.content_frame, text="3. Character Detection with OCR",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=80, width=900, )
        self.label_new_3.grid(row=3, column=1, pady=(10, 0), padx=5)
        self.label_new_3.place(x=19, y=350)
        self.label_new_3.config(image=None)

        self.button_next = tk.Button(self.content_frame, text='Next',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.do_preprocessing)
        self.button_next.grid(row=4, column=1, pady=5)
        self.button_next.place(y=750, x=860)
        
        self.content_frame.update_idletasks()
        


    def do_preprocessing(self):
        # self.processor = LicensePlateProcessor()
        try:
            self.processor.process_image(self.future_image_path, os.path.basename(self.future_image_path))
            self.preprocessing_1()
            messagebox.showinfo("showinfo", "Success")
            
        except:
            messagebox.showinfo("showinfo", "kendaraan tidak ditemukan, mohon masukan gambar yang benar")
            

    def preprocessing_1(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.label_titel = tk.LabelFrame(self.content_frame, text="Preprocessing Stage 1",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=900, )
        self.label_titel.grid(row=0, column=1, pady=5)

        original_image = Image.open(f"GUI/outputs/single/cropped_img/cropped_image_{os.path.basename(self.future_image_path)}")
        resized_image = original_image.resize((900, 450))
        img = ImageTk.PhotoImage(resized_image)

        self.label_new = tk.Label(self.content_frame, image=img, height=450, width=900, background="#1A1A1A")
        self.label_new.grid(row=1, column=1, pady=5)
        self.label_new.place(x=150, y=160)
        self.label_new.image = img

        self.button_prev = tk.Button(self.content_frame, text='Prev',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.preprocessing_stage)
        self.button_prev.grid(row=4, column=1, pady=5)
        self.button_prev.place(y=750, x=600)

        self.button_next = tk.Button(self.content_frame, text='Next',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.preprocessing_2)
        self.button_next.grid(row=4, column=2, pady=5)
        self.button_next.place(y=750, x=860)
        
        self.content_frame.update_idletasks()
        
        
    def preprocessing_2(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        self.label_titel = tk.LabelFrame(self.content_frame, text="Preprocessing Stage 2",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=900, )
        self.label_titel.grid(row=0, column=1, pady=5)

        original_image = Image.open(f"GUI/outputs/single/angle_fix_img/gambar_lurus_{os.path.basename(self.future_image_path)}")
        resized_image = original_image.resize((900, 450))
        img = ImageTk.PhotoImage(resized_image)

        self.label_new = tk.Label(self.content_frame, image=img, height=450, width=900, background="#1A1A1A")
        self.label_new.grid(row=1, column=1, pady=5)
        self.label_new.place(x=150, y=160)
        self.label_new.image = img

        button_prev = tk.Button(self.content_frame, text='Prev',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.preprocessing_1)
        button_prev.grid(row=4, column=1, pady=5)
        button_prev.place(y=750, x=600)

        button_next = tk.Button(self.content_frame, text='Next',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.preprocessing_3)
        button_next.grid(row=4, column=2, pady=5)
        button_next.place(y=750, x=860)
        
        self.content_frame.update_idletasks()
        

    def preprocessing_3(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        self.label_titel = tk.LabelFrame(self.content_frame, text="Preprocessing Stage 3",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=900, )
        self.label_titel.grid(row=0, column=1, pady=5)

        original_image = Image.open(f"GUI/outputs/single/final_img/text_draw_{os.path.basename(self.future_image_path)}")
        resized_image = original_image.resize((700, 1200))
        img = ImageTk.PhotoImage(resized_image)

        self.label_new = tk.Label(self.content_frame, image=img, height=650, width=750, background="#1A1A1A")
        self.label_new.grid(row=1, column=1, pady=5)
        self.label_new.place(x=150, y=60)
        self.label_new.image = img

        button_prev = tk.Button(self.content_frame, text='Prev',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.preprocessing_2)
        button_prev.grid(row=4, column=1, pady=5)
        button_prev.place(y=750, x=600)

        button_next = tk.Button(self.content_frame, text='Finish',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.result_preview_img)
        button_next.grid(row=4, column=2, pady=5)
        button_next.place(y=750, x=860)
        
        self.content_frame.update_idletasks()
        
    
    def result_preview_img(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        plate_character = self.processor.get_character()
        self.label_titel = tk.LabelFrame(self.content_frame, text="Testing Result",
                                    font=("Helvetica", 20), height=80, fg='white', width=900,
                                    background="#1A1A1A", labelanchor="n")
        self.label_titel.grid(row=0, column=0, pady=5)
        self.label_titel.place(x=150, y=0)

        original_image = Image.open(f"GUI/outputs/single/final_img/text_draw_{os.path.basename(self.future_image_path)}")
        resized_image = original_image.resize((700, 800))
        img = ImageTk.PhotoImage(resized_image)

        self.label_new = tk.Label(self.content_frame, image=img, height=700, width=1000, background="#1A1A1A")
        self.label_new.grid(row=1, column=1, pady=5)
        self.label_new.place(x=150, y=90)
        self.label_new.image = img
        
        self.label_new_2 = tk.LabelFrame(self.content_frame, text=plate_character,
                                    font=("Helvetica", 20), height=80, fg='white', width=900,
                                    background="#1A1A1A", labelanchor="n")
        self.label_new_2.grid(row=2, column=1, pady=5)
        self.label_new_2.place(x=150, y=750)
        
        self.database.insert_record(os.path.basename(self.future_image_path), plate_character, self.future_image_path)
        
    def save_table_to_txt(self, table, output_folder):
        output_file_path = os.path.join(output_folder)
        print(output_file_path)
        with open(output_file_path, 'w') as f:
            f.write(str(table))
            
        print('test')
        

    def choose_folder(self):
        folder_selected = askdirectory()

        print("Selected Folder:", folder_selected)

        try:
            index = 1
            files = os.listdir(folder_selected)

            for file in files:
                file_path = os.path.join(folder_selected, file)

                if os.path.isfile(file_path):
                    # messagebox.showinfo("showinfo", "Success")
                    character = self.multi_processor.process_image(f"{folder_selected}/{file}", filename=file_path, file_index=index)
                    self.list_of_filename.append(file)
                    self.list_of_filename_predict.append(character)
                    print("File:", file)
                
                elif os.path.isdir(file_path):
                    print("Folder:", file)
                
                index += 1
            
            
            self.folder_preprocess_1()
            
            print('ini')

            table = PrettyTable()
            table.field_names = ["File Index", "Filename", "Predicted FIlename"]
            for index, file_path in enumerate(self.list_of_filename, start=0):
                table.add_row([index, self.list_of_filename[index], self.list_of_filename_predict[index]])

            folderpath =self.save_to()
            
            print(folderpath)

            self.save_table_to_txt(table, folderpath.name)

        except Exception as e:
            print("Error:", str(e))
            
   
    def folder_preprocess_1(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.images = []
        self.label_titel = tk.LabelFrame(self.content_frame, text="Testing Result",
                                    font=("Helvetica", 20), height=80, fg='white', width=900,
                                    background="#1A1A1A", labelanchor="n")
        self.label_titel.grid(row=0, column=0, pady=5)
        # self.label_titel.place(x=150, y=0)
        
        folder_path = 'GUI/outputs/multiple/cropped_img'
        i = 1
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            self.img = Image.open(file_path)
            self.img.thumbnail((200, 150))
            photo = ImageTk.PhotoImage(self.img)
            self.images.append(photo)
            
            label = tk.Label(self.content_frame, image=photo, bg="#1A1A1A")
            label.grid(row=i + 1, column=0, padx=5, pady=5)
            label.place(x=100, y=170 * i)
            i += 1
        
        folder_path = 'GUI/outputs/multiple/angle_fix_img'
        i = 1
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            self.img = Image.open(file_path)
            self.img.thumbnail((200, 150))
            photo = ImageTk.PhotoImage(self.img)
            self.images.append(photo)
            
            label = tk.Label(self.content_frame, image=photo, bg="#1A1A1A")
            label.grid(row=i + 1, column=1, padx=5, pady=5)
            label.place(x=400, y=170 * i)
            i += 1
            
        folder_path = 'GUI/outputs/multiple/final_img'
        i = 1
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            self.img = Image.open(file_path)
            self.img.thumbnail((200, 230))
            photo = ImageTk.PhotoImage(self.img)
            self.images.append(photo)
            
            label = tk.Label(self.content_frame, image=photo, bg="#1A1A1A")
            label.grid(row=i + 1, column=2, padx=5, pady=5)
            label.place(x=750, y=170 * i)
            i += 1
       
# Instantiate the LicensePlateApp class and run the application
# app = TestLicensePlateApp(tk.Tk())
# app.run()