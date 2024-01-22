import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image
import yaml
from GUI.pages.home_page import HomePage

from GUI.services.train_yolo import YOLOv5Trainer

class TrainLicensePlateApp:
    def __init__(self, master, single_preprocess, multi_preprocess):
        self.master = master
        self.master.title("Fullscreen Window")
        self.master.attributes("-fullscreen", True)
        
        self.processor = single_preprocess
        self.multi_processor = multi_preprocess

        self.nav_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.nav_frame.grid(row=0, column=0)
        self.nav_frame.place(height=860, width=600)

        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)

        self.create_widgets()

    def create_widgets(self):
        box_nav = tk.LabelFrame(self.nav_frame, bg="#1A1A1A", height=250)
        box_nav.grid(row=0, column=0)


        # Choose File Button
        button_file = tk.Button(self.nav_frame, text='Pilih File',
                                font=("Helvetica", 14),
                                width=20,pady=5, command=self.create_preview_img)
        button_file.grid(row=1, column=0,pady=5,padx=80)

        # Training Button
        button_train = tk.Button(self.nav_frame, text='Training Parameter',
                                    font=("Helvetica", 14),
                                width=20, pady=5, command=self.tuning_parameter)
        button_train.grid(row=2, column=0,pady=5)

        # Result Button
        button_result = tk.Button(self.nav_frame, text='Training Result',
                                font=("Helvetica", 14),
                                width=20, pady=5, command=self.result_preview_img)
        button_result.grid(row=3, column=0,pady=5)

        # Home Button
        button_home = tk.Button(self.nav_frame, text='Home',
                                font=("Helvetica", 14),
                                width=20, pady=5,  command=lambda: self.prev_page())
        button_home.grid(row=4, column=0,pady=5, sticky="s")

        # ------------------------------------------------------------------------
        # Label Title
        labelframe = tk.LabelFrame(self.content_frame, text="Dataset Preview",
                                font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=2800)
        labelframe.grid(row=0, column=0,pady=5)
        labelframe.place(x=10, y=10)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("GUI/assets/folder.png"))

        # Create a Label Widget to display the text or Image
        label = tk.Label(self.content_frame, image = img, height=900, width=1400, background="#1A1A1A")
        label.grid(row=1, column=0,pady=5)
        label.place(x=10, y=60)

        self.master.mainloop()

    def prev_page(self):
        self.destroy()
        root = tk.Tk()
        HomePage(root, single_preprocess=self.processor, multi_preprocess=self.multi_processor)

    def copy_folder(self, source_path, destination_path):
        try:
            shutil.copytree(source_path, destination_path)
            print(f"Folder copied from {source_path} to {destination_path}")
        except Exception as e:
            print(f"Error copying folder: {str(e)}")

    def start_training(self, img_size, batch_size, epoch, data_path):
        # Lakukan sesuatu dengan nilai yang diperoleh
        print(f"Epoch: {epoch}")
        print(f"Batch Size: {batch_size}")
        print(f"Image Size: {img_size}")
        
        # with open(data_path, 'r') as file:
        #     config_data = yaml.safe_load(file)
        
        # # Ganti nilai variabel dengan path yang sesuai
        # config_data['train'] = '../dataset/data/train'
        # config_data['val'] = '../dataset/data/val'
        # config_data['test'] = '../dataset/data/test'
        
        # # Simpan kembali ke file YAML
        # with open(data_path, 'w') as file:
        #     yaml.dump(config_data, file)
        
        train = YOLOv5Trainer(
            img_size=img_size,
            batch_size=batch_size,
            epochs=epoch,
            data_path=data_path,
            weights_path="yolov5/yolov5s.pt",
        )
        
        train.train_yolov5()
        messagebox.showinfo("showinfo", "Success")

    def exit_fullscreen(self, event):
        self.attributes("-fullscreen", False)
        
    def copy_folder(self, source_folder, destination_folder):
        try:
            # Membuat direktori tujuan jika belum ada
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Menyalin isi folder
            shutil.copytree(source_folder, os.path.join(destination_folder, os.path.basename(source_folder)))

            print(f"Folder '{os.path.basename(source_folder)}' berhasil disalin ke '{destination_folder}'.")

        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")

    def create_preview_img(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
        self.images = []
        
        
        self.folder_selected = askdirectory()
        self.copy_folder(self.folder_selected, 'D:/python/license-plate-application/yolov5')
        
        
        # Label Title
        self.label_titel = tk.LabelFrame(self.content_frame, text="Data Preview",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=1920, )
        # Label Title
        self.label_titel.grid(row=0, column=0, pady=5)
        self.label_titel.place(y=10, x=10)


        folder_path = 'GUI/outputs/multiple/cropped_img'
        # preview image 
        i = 1
        j = 1
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            self.img = Image.open(file_path)
            self.img.thumbnail((200, 150))
            photo = ImageTk.PhotoImage(self.img)
            self.images.append(photo)
            
            label = tk.Label(self.content_frame, image=photo, bg="#1A1A1A")
            label.grid(row=i, column=j, padx=15, pady=5)
            label.place(x=30 + (200 * j), y=170 * i)
            j += 1
            
            if j % 5 == 0:
                i += 1 
                j = 1
        
    def tuning_parameter(self):
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)
        
         # Label Title
        self.label_titel = tk.LabelFrame(self.content_frame, text="Tuning Parameter",
                                    font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=1920, )
        # Label Title
        self.label_titel.grid(row=0, column=0, pady=5)
        
        # ---------------------------------------------------------------------------------------
        # Epoch
        self.label_text = tk.Label(self.content_frame , text='Epoch', fg='white',
                                    font=("Helvetica", 18),height=1,
                                    width=10, background="#1A1A1A")
        self.label_text.grid(row=1, column=1, pady=5)
        self.label_text.place(x=10, y=90)
        
        self.label_field = tk.Text(self.content_frame, background="#1A1A1A" , width=100, height= 2,font=('Helvatica', 20),fg='white')
        self.label_field.grid(row=1, column=2)
        self.label_field.place(x=200, y=90)
        
        # Batch size
        self.batch_text = tk.Label(self.content_frame , text='Batch size', fg='white',
                                    font=("Helvetica", 18),height=1,
                                    width=10, background="#1A1A1A")
        self.batch_text.grid(row=2, column=1, pady=5)
        self.batch_text.place(x=10, y=170)
        
        self.batch_field = tk.Text(self.content_frame, background="#1A1A1A" , width=100, height= 2,font=('Helvatica', 20),fg='white')
        self.batch_field.grid(row=2, column=2)
        self.batch_field.place(x=200, y=170)
        
        # Image size
        self.img_text = tk.Label(self.content_frame , text='Image size', fg='white',
                                    font=("Helvetica", 18),height=1,
                                    width=10, background="#1A1A1A")
        self.img_text.grid(row=3, column=1, pady=5)
        self.img_text.place(x=10, y=250)
        
        self.img_field = tk.Text(self.content_frame, background="#1A1A1A" , width=100, height= 2,font=('Helvatica', 20),fg='white')
        self.img_field.grid(row=3, column=2)
        self.img_field.place(x=200, y=250)
        
        
        self.button_next = tk.Button(self.content_frame, text='Next',
                                    font=("Helvetica", 14), width=20, pady=5,
                                    command=lambda: self.start_training(epoch=self.label_field.get("1.0", "end-1c"),
                                    batch_size=self.batch_field.get("1.0", "end-1c"),
                                    img_size=self.img_field.get("1.0", "end-1c"), 
                                    data_path=f'dataset/data/data.yaml'))
        
        self.button_next.grid(row=4, column=1, pady=5)
        self.button_next.place(y=450, x=260)
        
        

    def result_preview_img(self):
        # your existing result_preview_img code
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self.master, bg="#1A1A1A")
        self.content_frame.grid(row=0, column=1)
        self.content_frame.place(height=860, width=1400, x=350)

        # ------------------------------------------------------------------------
        # Label Title
        labelframe = tk.LabelFrame(self.content_frame, text="Result Graph [confusion matrix] [labels correlogram] [labels] [result]",
                                font=("Helvetica", 16), fg="white",
                                    background="#1A1A1A", height=50, width=2800)
        labelframe.grid(row=0, column=0,pady=5)
        labelframe.place(x=10, y=10)

        # Create an object of tkinter ImageTk
        self.img = Image.open("yolov5/runs/train/exp/confusion_matrix.png")
        self.img.thumbnail((300, 300))
        self.img = ImageTk.PhotoImage(self.img)

        # Create a Label Widget to display the text or Image
        self.label = tk.Label(self.content_frame, image = self.img, height=300, width=300, background="#1A1A1A")
        self.label.grid(row=1, column=0,pady=5)
        self.label.place(x=10, y=70)
        
        # Create an object of tkinter ImageTk result 2 
        self.img_2 = Image.open("yolov5/runs/train/exp/labels_correlogram.jpg")
        self.img_2.thumbnail((300, 300))
        self.img_2 = ImageTk.PhotoImage(self.img_2)

        # Create a Label Widget to display the text or Image
        self.label_2 = tk.Label(self.content_frame, image = self.img_2, height=300, width=300, background="#1A1A1A")
        self.label_2.grid(row=1, column=0,pady=5)
        self.label_2.place(x=10, y=400)
        
        # Create an object of tkinter ImageTk result 3
        self.img_3 = Image.open("yolov5/runs/train/exp/labels.jpg")
        self.img_3.thumbnail((300, 300))
        self.img_3 = ImageTk.PhotoImage(self.img_3)

        # Create a Label Widget to display the text or Image
        self.label_3 = tk.Label(self.content_frame, image = self.img_3, height=300, width=300, background="#1A1A1A")
        self.label_3.grid(row=0, column=1,pady=5, padx=5)
        self.label_3.place(x=450, y=70)
        
         # Create an object of tkinter ImageTk result 4
        self.img_4 = Image.open("yolov5/runs/train/exp/results.png")
        self.img_4.thumbnail((700, 300))
        self.img_4 = ImageTk.PhotoImage(self.img_4)

        # Create a Label Widget to display the text or Image
        self.label_4 = tk.Label(self.content_frame, text='result', fg='white', image = self.img_4, height=300, width=700, background="#1A1A1A")
        self.label_4.grid(row=1, column=1,pady=5, padx=5)
        self.label_4.place(x=400, y=400)

