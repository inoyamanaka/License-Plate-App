import os
import yolov5
import cv2
import easyocr
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
import imutils
import re
import math

# DEFINE ALL VARIABEL
reader = easyocr.Reader(['en'])

# load model
model = yolov5.load('keremberke/yolov5m-license-plate')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image

# Font style
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
font_thickness = 5
font_color = (0, 255, 0)
# Menentukan ukuran padding (misalnya, 10 piksel)
padding_size = 10
new_size = (950, 330)

index = 1

# Start to detect 
folder_path = 'output/K2/'

# Mendapatkan daftar file dalam folder
file_list = os.listdir(folder_path)
# set image

def reverse_and_keep_letters(input_str):
    reversed_str = input_str[::-1]
    result_str = ''
    found_letter = False

    for char in reversed_str:
        if char.isalpha():
            found_letter = True
        if found_letter or char.isalpha():
            result_str += char

    result_str = ''.join(c for c in reversed(input_str.upper()) if c.isalnum())
    return result_str[::-1].replace(" ", "")

def find_longest_alphanumeric_list(text):
    longest_element = max(text, key=lambda s: sum(c.isalnum() for c in s))
    return longest_element

for file_name in file_list:
    try:
        img = f'{folder_path}/{file_name}'

        # perform inference
        results = model(img, size=640)

        # inference with test time augmentation
        results = model(img, augment=True)

        # parse results
        predictions = results.pred[0]
        boxes = predictions[:, :4]
        scores = predictions[:, 4]
        categories = predictions[:, 5]

        # Data
        data = np.array(boxes)

        # Menghitung perbedaan x2 - x1
        perbedaan_x = data[:, 2] - data[:, 0]

        # Mencari indeks dengan nilai perbedaan x terbesar
        indeks_tertinggi = np.argmax(perbedaan_x)

        image = cv2.imread(img)

        # Koordinat x1, y1, x2, y2
        x1, y1, x2, y2 = boxes[indeks_tertinggi]

        # Crop gambar dari koordinat yang diberikan
        # Menentukan koordinat baru untuk citra yang telah dicrop
        y1_new = max(0, int(y1) - padding_size)
        y2_new = min(image.shape[0], int(y2) + padding_size)
        x1_new = max(0, int(x1) - padding_size)
        x2_new = min(image.shape[1], int(x2) + padding_size)
        cropped_image = image[int(y1_new):int(y2_new), int(x1_new):int(x2_new)]
        
        
        resized_image = cv2.resize(cropped_image, dsize=new_size, interpolation=cv2.INTER_AREA)
        
        resized_image = cv2.filter2D(resized_image, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
        
        resized_image = cv2.fastNlMeansDenoisingColored(resized_image, None, 10, 10, 7, 15)
        


        # Konversi gambar ke grayscale
        grayscale = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Deteksi tepi pada gambar
        tepi = cv2.Canny(grayscale, 50, 150, apertureSize=3)

        # Temukan garis pada gambar menggunakan transformasi Hough Line
        garis = cv2.HoughLinesP(tepi, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

        angles = []

        try:
            for [[x1, y1, x2, y2]] in garis:
                angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
                angles.append(angle)
        except:
            angles.append(0)
            
        
        median_angle = np.median(angles)
        
        if abs(median_angle) > 60:
            median_angle = 0
        
        img_rotated = ndimage.rotate(resized_image, median_angle)

        # Tampilkan gambar yang telah diluruskan (opsional)

        threshold_value = 125
        # load the input image and convert it to grayscale
        gray = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2GRAY)
        # Deteksi warna dominan
        jumlah_pixel_putih = cv2.inRange(gray, 200, 255).sum()
        jumlah_pixel_hitam = cv2.inRange(gray, 0, 50).sum()

        result = reader.readtext(img_rotated,
                             decoder='beamsearch',
                             min_size = 20,
                             add_margin=0.1,
                    
                            adjust_contrast=0.8,
                            contrast_ths=0.3,
                  
                             bbox_min_size = 5, detail=0, paragraph = True, text_threshold=0.2)
        
       
        # Menghapus karakter pada urutan ke sembilan dan seterusnya jika bukan huruf
        # Mengurutkan hasil berdasarkan koordinat paling kiri
        result_urut = sorted(result, key=lambda x: x[0][0][0])
        # text_to_write = "".join([res[1] for res in result_urut])
        
        reversed_output = [reverse_and_keep_letters(item) for item in result_urut]
        result_rr = find_longest_alphanumeric_list(reversed_output)
        
    
        input_string = re.sub(r"\s", "", result_rr)
        
        output_string = ''.join([
            'G' if i == 0 and char == '6' else
            'Z' if i == 0 and char == '2' else
            'B' if i == 0 and char == '8' else
            char if char.isalpha() or i not in range(7, 15) else '4' if char == 'L' and input_string[i + 1].isdigit() else ''
            for i, char in enumerate(input_string[:10])
        ])
        
        # Menghilangkan huruf terakhir jika itu adalah 'I', 'L', atau 'H'
        # if output_string[-1] in ['T', 'U']:
        #     output_string = output_string[:-1]
            
        if output_string[-1] == 'O':
            output_string[-1] = 'Q' 
            
        

        # Koordinat dari tensor yang diberikan
        x1, y1, x2, y2 = boxes[indeks_tertinggi]

        # Gambar rectangle
        imgDraw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), font_color, font_thickness)  # font_color adalah warna merah

        # Tulis kata
        imgDraw3 = cv2.putText(imgDraw,output_string, (int(x1), int(y1) - 10), font, font_scale, font_color, font_thickness) 

        # Simpan gambar yang telah dimodifikasi
        cv2.imwrite(f"result/cropped/hasil_cropped{index}.jpg", cropped_image)
        cv2.imwrite(f'result/fix_position/Gambar Lurus{index}.jpg', img_rotated)
        cv2.imwrite(f"result/draw_text/K2/K2_{output_string}.jpg", imgDraw3)
        
        index +=1 
    except:
        print(file_name)