import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys



sys.path.append('D:/python/license-plate-application')
from GUI.database.connect_db import LicensePlateDatabase
from GUI.pages.edit_detail_page import EditDetailPage
from GUI.pages.home_page import HomePage


class CrudLicensePlateApp:
    def __init__(self, master, single_preprocess, multi_preprocess):
        self.master = master
        self.master.title("Image Scrollbar Example")
        self.master.title("Fullscreen Window")
        self.master.attributes("-fullscreen", True)
        
        self.single_preprocess = single_preprocess
        self.multi_preprocess = multi_preprocess

        self.canvas = tk.Canvas(master, background="#1A1A1A", height=800, width=1110)
        self.canvas.grid(row=1, column=1)

        self.nav_frame = tk.Frame(master, bg="#1A1A1A")
        self.nav_frame.grid(row=0, column=0)
        self.nav_frame.place(height=860, width=400)

        self.database = LicensePlateDatabase()

        self.create_image_scrollbar_app()

    def refresh(self):
        try:
            self.master.destroy()
            CrudLicensePlateApp(tk.Tk(), self.single_preprocess, self.multi_preprocess)
        except Exception as e:
            print(f"Error during refresh: {e}")

    def prev_page(self):
        self.master.destroy()
        root = tk.Tk()
        HomePage(root, self.single_preprocess, self.multi_preprocess)
        
    def edit_page(self, image_path, index):
        self.master.destroy()
        root = tk.Tk()
        EditDetailPage(root, self.single_preprocess, self.multi_preprocess, image_path=image_path, db_index=index)
        
    def delete_item(self, index):
        answer = messagebox.askquestion("askquestion", "Are you sure want to delete this?")
        if answer == 'yes':
            self.database.delete_record(index)
            messagebox.showinfo("showinfo", "Success")
            self.refresh()

    def create_image_scrollbar_app(self):
        list_index = self.database.get_index()
        list_filepath = self.database.get_filepath_list()
        list_filename = self.database.get_file_name()
        list_filepredict = self.database.get_file_predict()

        scrollbar = ttk.Scrollbar(self.master, orient='vertical', command=self.canvas.yview)
        scrollbar.grid(row=1, column=2, sticky=tk.NS)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(self.canvas, background="#1A1A1A")
        self.canvas.create_window((0, 0), window=frame, anchor='nw')
        self.images = []

        for i, image_path in enumerate(list_filepath):
            self.img = Image.open(image_path)
            self.img.thumbnail((250, 200))
            photo = ImageTk.PhotoImage(self.img)
            self.images.append(photo)

            label = tk.Label(frame, image=photo, bg="#1A1A1A")
            label.grid(row=i + 1, column=0, padx=5, pady=5, sticky=tk.E)

            text_label = tk.Label(frame, text=f"{list_filename[i]}", fg="white", bg="#1A1A1A", font=("Helvetica", 16))
            text_label.grid(row=i + 1, column=1, padx=5, pady=5, sticky=tk.W)

            text_label = tk.Label(frame, text=f"{list_filepredict[i]}", fg="white", bg="#1A1A1A", font=("Helvetica", 16))
            text_label.grid(row=i + 1, column=2, padx=5, pady=5, sticky=tk.W)

            button_img2 = ImageTk.PhotoImage(Image.open("GUI/assets/pen.png").resize((30, 30)))
            button2 = tk.Button(frame, image=button_img2, bg="white", bd=0, height=60, width=60, command=lambda i=i: 
                self.edit_page(image_path=list_filepath[i], index=list_index[i]))
            button2.grid(row=i + 1, column=3, padx=5, pady=5, sticky=tk.W)
            button2.image = button_img2

            button_delete_img = ImageTk.PhotoImage(Image.open("GUI/assets/delete.png").resize((30, 30)))
            button_delete = tk.Button(frame, image=button_delete_img, bg="white", bd=0, height=60, width=60,
                                      command=lambda i=i: self.delete_item(list_index[i]))
            button_delete.grid(row=i + 1, column=4, padx=5, pady=5, sticky=tk.W)
            button_delete.image = button_delete_img

        frame.update_idletasks()

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        button_home = tk.Button(self.nav_frame, text='Home', font=("Helvetica", 14),
                                width=20, pady=5, command=self.prev_page)
        button_home.grid(row=0, column=0, pady=5, sticky="s")
        button_home.place(y=300, x=60)

        button_refresh = tk.Button(self.nav_frame, text='Refresh', font=("Helvetica", 14),
                                   width=20, pady=5, command=self.refresh)
        button_refresh.grid(row=1, column=0, pady=5, padx=80, sticky="s")
        button_refresh.place(y=360, x=60)

        label_title = tk.LabelFrame(self.master, text="List of License Plate",
                                    font=("Helvetica", 16), fg="white", background="#1A1A1A", height=70, width=1200)
        label_title.grid(row=0, column=1, pady=5)
        label_title.place(x=400, y=10)
        self.master.mainloop()
        

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CrudLicensePlateApp(root,)