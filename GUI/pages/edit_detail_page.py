import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys

sys.path.append('D:/python/license-plate-application')
from GUI.database.connect_db import LicensePlateDatabase
from GUI.pages.home_page import HomePage

class EditDetailPage:
    def __init__(self, master, single_preprocess, multi_preprocess):
        self.master = master
        self.master.title("Edit Detail Page")
        self.master.title("Fullscreen Window")
        self.master.attributes("-fullscreen", True)
        
        self.single_preprocess = single_preprocess
        self.multi_preprocess = multi_preprocess

        self.nav_frame = tk.Frame(master, bg="#1A1A1A")
        self.nav_frame.grid(row=0, column=0)
        self.nav_frame.place(height=860, width=400, x=0)
        
        self.canvas = tk.Frame(master, background="#1A1A1A", height=1300, width=2000)
        self.canvas.grid(row=0, column=1)
        self.canvas.place(height=860, width=2000, x=401)
        
        self.database = LicensePlateDatabase()

        self.create_ui_content()

    def prev_page(self):
        self.master.destroy()
        from GUI.pages.crud_page import CrudLicensePlateApp
        
        root = tk.Tk()
        CrudLicensePlateApp(root, single_preprocess=self.single_preprocess, multi_preprocess= self.multi_preprocess)
        
    def ganti_nama_file(self, path_lama, nama_lama, nama_baru):
        path_file_lama = os.path.join(path_lama, nama_lama)
        path_file_baru = os.path.join(path_lama, nama_baru)

        try:
            os.rename(path_file_lama, path_file_baru)
            print(f"Nama file berhasil diubah dari {nama_lama} menjadi {nama_baru}")
        except FileNotFoundError:
            print(f"File dengan nama {nama_lama} tidak ditemukan di path {path_lama}.")
        except FileExistsError:
            print(f"File dengan nama {nama_baru} sudah ada di path {path_lama}.")


    def create_ui_content(self):
        label_title = tk.LabelFrame(self.canvas, text="Edit Data Preview Image",
                                    font=("Helvetica", 16), fg="white", background="#1A1A1A", height=70, width=1200)
        label_title.grid(row=1, column=1, pady=5)
        
        # Create an object of tkinter ImageTk
        original_image = Image.open('D:/python/license-plate-application/GUI/assets/folder.png')
        resized_image = original_image.resize((500, 500))
        img = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        self.label_new = tk.Label(self.canvas, image=img, height=500, width=500, background="#1A1A1A")
        self.label_new.grid(row=2, column=1, pady=5)
        
        self.form_frame = tk.Frame(self.canvas, background="#1A1A1A", height=1300, width=2000, padx=200)
        self.form_frame.grid(row=3, column=1)
        self.form_frame.place(x=50, y=600)
        
        # ---------------------------------------------------------------------------------------
        # Label
        self.label_text = tk.Label(self.form_frame , text='Label', fg='white',
                                    font=("Helvetica", 18),height=1,
                                    width=30, background="#1A1A1A")
        self.label_text.grid(row=0, column=1, pady=5)
        # self.label_text.place(x=10, y=10)
        
        self.label_field = tk.Text(self.form_frame, background="#1A1A1A" , width=150, height= 10,font=('Helvatica', 20),fg='white')
        self.label_field.grid(row=0, column=2)
        self.label_field.place(x=350)
        
        # ---------------------------------------------------------------------------------------
        # Change Label Text
        self.button_change_label = tk.Label(self.form_frame, text='Change Picture', fg='white',
                                    font=("Helvetica", 18),height=1,
                                    width=20, background="#1A1A1A")
        self.button_change_label.grid(row=1, column=1)
        
        self.button_change = tk.Button(self.form_frame, text='Change Picture')
        self.button_change.grid(row=1, column=2)
        self.button_change.place(x=350, y=50)
        
        # ---------------------------------------------------------------------------------------
        # Change Picture
        button_back = tk.Button(self.nav_frame, text='Back', font=("Helvetica", 14),
                                width=20, pady=5,)
        button_back.grid(row=0, column=0, pady=5, sticky="s")
        button_back.place(y=300, x=60)

        self.master.mainloop()    
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EditDetailPage(root)
