import shutil
import sys
import tkinter as tk
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image

sys.path.append('D:/python/license-plate-application')
from GUI.pages.train_yolo import YOLOv5Trainer  

# from GUI.pages.home_page import FullscreenApp
ws = tk.Tk()
ws.title("Fullscreen Window")
ws.attributes("-fullscreen", True)  

# ---------------------------------------------
label_new = tk.Label()
label_new_2 = tk.Label()
label_new_3 = tk.Label()
label_new_4 = tk.Label()

def prevPage(master):
    master.destroy()
    import GUI.pages.home_page as home_page
    
def copy_folder(self, source_path, destination_path):
    try:
        shutil.copytree(source_path, destination_path)
        print(f"Folder copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying folder: {str(e)}")

    
def start_training(self, img_size, batch_size, epoch):
    train = YOLOv5Trainer(
        img_size=img_size,
        batch_size=batch_size,
        epochs=epoch,
        data_path="D:/python/license-plate-application/roboflowdata/data.yaml",
        weights_path="yolov5/yolov5s.pt",
    )
    
    train.train_yolov5()

def exit_fullscreen(self, event):
    ws.attributes("-fullscreen", False)
    
def create_preview_img():
    global label_new, label_new_2, label_new_3, label_new_4
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
    # preview image 
    for i in range (1,8):
        label_new = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new.grid(row=1, column=i,pady=(80,0), padx=5)
        
    for i in range (1,8):
        label_new_2 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_2.grid(row=2, column=i,pady=(40,0), padx=5)

    for i in range (1,8):
        label_new_3 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_3.grid(row=3, column=i,pady=(40,0), padx=5)
        
    for i in range (1,8):
        label_new_4 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_4.grid(row=4, column=i,pady=(40,0), padx=5)
        
    label.place(x=10, y=60,width=0, height=0)
    

def tuning_paramter():
    global label_new, label_new_2, label_new_3, label_new_4
    
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
    
    label_new = tk.Label(content_frame, text="Enter Email", width=10, font=("arial",12))  
    label_new.grid(row=1, column=1,pady=(20,0), padx=5)
    label_new.place(x=19, y=160)  
    label_new.config(text='Test 1', image=None)
    
    en3= tk.Entry(content_frame)  
    en3.place(x=200, y=160)  
        

    label_new_2 =tk.LabelFrame(content_frame, text="Dataset Preview 2",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A", height=50, width=2800)
    label_new_2.grid(row=2, column=1,pady=(10,0), padx=5)
    label_new_2.config(text='Test 2', image=None)


    label_new_3 = tk.LabelFrame(content_frame, text="Dataset Preview 2",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A", height=50, width=2800)
    label_new_3.grid(row=3, column=1,pady=(10,0), padx=5)
    label_new_3.config(text='Test 3', image=None)
        
    label_new_4 = tk.LabelFrame(content_frame, text="Dataset Preview 2",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A", height=50, width=2800)
    label_new_4.grid(row=4, column=1,pady=(10,0), padx=5)
    label_new_4.config(text='Test 4', image=None)


    label.place(x=10, y=60,width=0, height=0)
    

def result_preview_img():
    global label_new, label_new_2, label_new_3, label_new_4
    label_new.destroy()
    label_new_2.destroy()
    label_new_3.destroy()
    label_new_4.destroy()
    
    img = ImageTk.PhotoImage(Image.open("GUI/assets/license-plate.png"))
    # Mengganti gambar pada label dengan gambar baru
    
    for i in range (1,8):
        label_new = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new.grid(row=1, column=i,pady=(80,0), padx=5)
        label_new.config(image=img, text=None)
        label_new.image = img
        
    for i in range (1,8):
        label_new_2 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_2.grid(row=2, column=i,pady=(40,0), padx=5)
        label_new_2.config(image=img, text=None)
        label_new_2.image = img

    for i in range (1,8):
        label_new_3 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_3.grid(row=3, column=i,pady=(40,0), padx=5)
        label_new_3.config(image=img, text=None)
        label_new_3.image = img
        
    for i in range (1,8):
        label_new_4 = tk.Label(content_frame, image = img, height=150, width=150, background="#1A1A1A", padx=10)
        label_new_4.grid(row=4, column=i,pady=(40,0), padx=5)
        label_new_4.config(image=img, text=None)
        label_new_4.image = img
        
    label.place(x=10, y=60,width=0, height=0)
    
    

nav_frame = tk.Frame(ws, bg="#1A1A1A")
nav_frame.grid(row=0, column=0)
nav_frame.place(height=860, width=600)

content_frame = tk.Frame(ws, bg="#1A1A1A")
content_frame.grid(row=0, column=1 )
content_frame.place(height=860, width=1400, x=350)

box_nav = tk.LabelFrame(nav_frame, bg="#1A1A1A", height=250)
box_nav.grid(row=0, column=0)


# Choose File Button
button_file = tk.Button(nav_frame, text='Pilih File',
                        font=("Helvetica", 14),
                        width=20,pady=5, command=create_preview_img)
button_file.grid(row=1, column=0,pady=5,padx=80)

# Training Button
button_train = tk.Button(nav_frame, text='Training Parameter',
                            font=("Helvetica", 14),
                        width=20, pady=5, command=tuning_paramter)
button_train.grid(row=2, column=0,pady=5)

# Result Button
button_result = tk.Button(nav_frame, text='Training Result',
                        font=("Helvetica", 14),
                        width=20, pady=5, command=result_preview_img)
button_result.grid(row=3, column=0,pady=5)

# Home Button
button_home = tk.Button(nav_frame, text='Home',
                        font=("Helvetica", 14),
                        width=20, pady=5,  command=lambda: prevPage(ws))
button_home.grid(row=4, column=0,pady=5, sticky="s")

# ------------------------------------------------------------------------
# Label Title
labelframe = tk.LabelFrame(content_frame, text="Dataset Preview",
                        font=("Helvetica", 16), fg="white",
                            background="#1A1A1A", height=50, width=2800)
labelframe.grid(row=0, column=0,pady=5)
labelframe.place(x=10, y=10)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("GUI/assets/folder.png"))

# Create a Label Widget to display the text or Image
label = tk.Label(content_frame, image = img, height=900, width=1400, background="#1A1A1A")
label.grid(row=1, column=0,pady=5)
label.place(x=10, y=60)

# if button clicked

# ws.bind("<Escape>", lambda event: exit_fullscreen(event, ws))
ws.mainloop()
    
    
    
# create_train_page()