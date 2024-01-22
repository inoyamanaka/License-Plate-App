import sys
import tkinter as tk
from PIL import ImageTk, Image



sys.path.append('D:/python/license-plate-application')
from tkinter.tix import IMAGETEXT

class HomePage:
    def __init__(self, master, single_preprocess, multi_preprocess):
        self.master = master
        self.master.title("Fullscreen Window")
        self.master.attributes("-fullscreen", True)
        self.single_preprocess = single_preprocess
        self.multi_preprocess = multi_preprocess
        self.create_content()

    def on_training_click(self):
        self.master.destroy()
        
        from GUI.pages.train_page import TrainLicensePlateApp
        TrainLicensePlateApp(master=tk.Tk(), single_preprocess=self.single_preprocess, multi_preprocess=self.multi_preprocess)

    def on_testing_click(self):
        self.master.destroy()

        from GUI.pages.test_page import TestLicensePlateApp
        TestLicensePlateApp(master=tk.Tk(), single_preprocess=self.single_preprocess, multi_preprocess=self.multi_preprocess)

    def on_crud_click(self):
        self.master.destroy()
        
        from GUI.pages.crud_page import CrudLicensePlateApp
        CrudLicensePlateApp(tk.Tk(), single_preprocess=self.single_preprocess, multi_preprocess=self.multi_preprocess)

    def exit_fullscreen(self, event):
        self.master.attributes("-fullscreen", False)

    def create_content(self):
        frame = tk.Frame(self.master, bg="#1A1A1A")
        frame.pack(expand=True, fill='both')

        # Gambar
        image_path = "GUI/assets/license-plate.png"  # Ganti dengan path gambar Anda
        img = Image.open(image_path)
        img = img.resize((350, 380),)
        photo = ImageTk.PhotoImage(img)

        box_size = 390
        x_position = (self.master.winfo_screenwidth() - box_size) // 2
        y_position = (self.master.winfo_screenheight() - box_size) // 2

        box = tk.Canvas(frame, width=box_size, height=box_size - 40, bg="white")
        box.grid(row=0, column=0, pady=90, columnspan=2, rowspan=2, padx=x_position)

        # Menambahkan gambar ke dalam Canvas
        box.create_image(box_size // 2, box_size // 2, anchor=tk.CENTER, image=photo)

        # Button Training
        button_training = tk.Button(frame, text="Training", command=lambda: self.on_training_click(),
                                    bg="#D9D9D9", fg="black",
                                    font=("Helvetica", 14),
                                    width=20, pady=5,
                                    relief=tk.FLAT)
        button_training.grid(row=2, column=0, columnspan=2, rowspan=2)

        # Button Testing
        button_testing = tk.Button(frame, text="Testing", command=lambda: self.on_testing_click(),
                                    bg="#D9D9D9", fg="black",
                                    font=("Helvetica", 14),
                                    padx=0, pady=5,
                                    width=20,
                                    relief=tk.FLAT)
        button_testing.grid(row=4, column=0, pady=10, columnspan=2, rowspan=2)

        # Button Settings
        # button_training = tk.Button(frame, text="Settings", command=self.on_training_click,
        #                             bg="#D9D9D9", fg="black",
        #                             font=("Helvetica", 14),
        #                             padx=0, pady=5,
        #                             width=20,
        #                             relief=tk.FLAT)
        # button_training.grid(row=6, column=0, columnspan=2, rowspan=2)

        # Button Crud
        button_testing = tk.Button(frame, text="List License", command=lambda: self.on_crud_click(),
                                    bg="#D9D9D9", fg="black",
                                    font=("Helvetica", 14),
                                    padx=0, pady=5,
                                    width=20,
                                    relief=tk.FLAT)
        button_testing.grid(row=8, column=0, columnspan=2, rowspan=2)

        # Label Made By
        label_bottom_left = tk.Label(frame, text="By Herlambang Kurniawan", fg="white", bg="#1A1A1A")
        label_bottom_left.grid(row=10, column=0, sticky=tk.SW, padx=10, pady=180,)

        self.master.bind("<Escape>", self.exit_fullscreen)
        self.master.mainloop()
        


