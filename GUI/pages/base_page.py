import tkinter as tk
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image  

def next_page(master):
    master.destroy()
    import train_page

def on_training_click():
    print("Training button clicked!")

def on_testing_click(master):
    print("Testing button clicked!")
    master.destroy()
    import test_page
    
def on_crud_click(master):
    master.destroy()
    import crud_page

def exit_fullscreen(event, master):
    master.attributes("-fullscreen", False)

def create_home_page():
    master = tk.Tk()
    master.title("Fullscreen Window")
    master.attributes("-fullscreen", True)  

    frame = tk.Frame(master, bg="#1A1A1A")
    frame.pack(expand=True, fill='both')

    # Gambar
    image_path = "GUI/assets/license-plate.png"  # Ganti dengan path gambar Anda
    img = Image.open(image_path)
    img = img.resize((350, 380),)
    photo = ImageTk.PhotoImage(img)
    
    box_size = 390
    x_position = (master.winfo_screenwidth() - box_size) // 2
    y_position = (master.winfo_screenheight() - box_size) // 2

    box = tk.Canvas(frame, width=box_size, height=box_size - 40, bg="white")
    box.grid(row=0, column=0, pady=90, columnspan=2, rowspan=2, padx=x_position)
    
    # Menambahkan gambar ke dalam Canvas
    box.create_image(box_size // 2, box_size // 2, anchor=tk.CENTER, image=photo)

    # Button Training
    button_training = tk.Button(frame, text="Training", command=lambda: next_page(master), 
                                bg="#D9D9D9",  
                                fg="black",    
                                font=("Helvetica", 14),
                                width=20, pady=5,  
                                relief=tk.FLAT)
    button_training.grid(row=2, column=0, columnspan=2, rowspan=2)

    # Button Testing
    button_testing = tk.Button(frame, text="Testing", command=lambda: on_testing_click(master), 
                                bg="#D9D9D9",  
                                fg="black",    
                                font=("Helvetica", 14),
                                padx=0, pady=5,  
                                width=20,
                                relief=tk.FLAT)
    button_testing.grid(row=4, column=0, pady=10 ,columnspan=2, rowspan=2)
    
    # Button Settings
    button_training = tk.Button(frame, text="Settings", command=on_training_click, 
                                bg="#D9D9D9",  
                                fg="black",    
                                font=("Helvetica", 14),
                                padx=0, pady=5,  
                                width=20,
                                relief=tk.FLAT)
    button_training.grid(row=6, column=0, columnspan=2, rowspan=2)

    # Button Crud
    button_testing = tk.Button(frame, text="List License", command=lambda: on_crud_click(master), 
                                bg="#D9D9D9",  
                                fg="black",    
                                font=("Helvetica", 14),
                                padx=0, pady=5,  
                                width=20,
                                relief=tk.FLAT)
    button_testing.grid(row=8, column=0, pady=10 ,columnspan=2, rowspan=2)
    
    # Label Made By
    label_bottom_left = tk.Label(frame, text="By Herlambang Kurniawan", fg="white", bg="#1A1A1A")
    label_bottom_left.grid(row=10, column=0, sticky=tk.SW, padx=10, pady=180,)

    master.bind("<Escape>", lambda event: exit_fullscreen(event, master))

    master.mainloop()

# Panggil fungsi untuk membuat aplikasi fullscreen
create_home_page()
