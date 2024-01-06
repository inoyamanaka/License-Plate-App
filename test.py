import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
import yolov5
import easyocr
import re
import os

# load model
model = yolov5.load('keremberke/yolov5n-license-plate')# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image
reader = easyocr.Reader(['id', 'en'])


# Path ke folder yang berisi file-file gambar
folder_path = 'D:/Dataset/Plat kendaraan/K1'

# Mendapatkan daftar file dalam folder
file_list = os.listdir(folder_path)

for file_name in file_list:
    # print(file_name)
    img_path = os.path.join(folder_path, file_name)
    print(img_path)
    img = img_path
    img_cv = cv2.imread(img_path)

    # inference with test time augmentation
    results = model(img, augment=True)

    predictions = results.pred[0]
    boxes = predictions[:, :4] 
    scores = predictions[:, 2]
    categories = predictions[:, 5]

    for i in range(len(boxes)):
        x1, y1, x2, y2 = boxes[i]  # Ambil koordinat x1, y1, x2, y2 dari kotak ke-i
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

         # Geser area cropping ke atas sejauh pixel_shift piksel
        # y1_shifted = max(0, y1 - 100)  # Jangan kurangi nilai y1 menjadi negatif
        # y2_shifted = y2 + 10

        # Crop gambar sesuai dengan koordinat kotak yang sudah digeser ke atas
        cropped_img = img_cv[y1:y2, x1:x2]
        cv2.imwrite(f"cropped_image_{i}.jpg", cropped_img)


    # Load gambar hasil deteksi YOLOv5
    image = cv2.imread('cropped_image_0.jpg')

    # Tentukan sudut rotasi berdasarkan sudut kemiringan plat
    angle = -15
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)


    # Tentukan persentase bagian atas dan bawah yang ingin dipotong
    top_percent = 20 
    bottom_percent = 20 

    # Hitung jumlah pixel yang akan dipotong dari bagian atas dan bawah
    top_cut = int(height * (top_percent / 100))
    bottom_cut = int(height * (bottom_percent / 100))

    # Potong bagian atas dan bawah gambar
    cropped_image = rotated_image[top_cut:-bottom_cut, :]
    cv2.imwrite(f"cropped_image_{i}.jpg", cropped_image)

    output = reader.readtext('cropped_image_0.jpg')
    output = sorted(output, key=lambda x: x[0][0])

    # Menyimpan hasil gabungan ke dalam variabel
    result_string = " ".join(output[i][1] for i in range(0,len(output)))
    result_string = result_string.upper()

    filtered_text = "K1_" + re.sub(r"[^a-zA-Z0-9]", "", result_string)
    print(filtered_text)

    cv2.imwrite(f"output/K2/{filtered_text}.jpg", img_cv)
    


# set image
# img = 'test1.jpg'
# img_cv = cv2.imread("test1.jpg")
# gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (5,5), 0) 
# edged = cv2.Canny(blur, 20, 200) 

# # perform inference
# results = model(img_cv, size=640)

# inference with test time augmentation
# results = model(img, augment=True)

# predictions = results.pred[0]
# boxes = predictions[:, :4] 
# scores = predictions[:, 2]
# categories = predictions[:, 5]

# for i in range(len(boxes)):
#     x1, y1, x2, y2 = boxes[i]  # Ambil koordinat x1, y1, x2, y2 dari kotak ke-i
#     x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

#      # Geser area cropping ke atas sejauh pixel_shift piksel
#     y1_shifted = max(0, y1)  # Jangan kurangi nilai y1 menjadi negatif
#     y2_shifted = y2 + 10

#     # Crop gambar sesuai dengan koordinat kotak yang sudah digeser ke atas
#     cropped_img = img_cv[y1:y2, x1:x2]
#     cv2.imwrite(f"cropped_image_0.jpg", cropped_img)


# # Load gambar hasil deteksi YOLOv5
# image = cv2.imread('cropped_image_0.jpg')

# # Tentukan sudut rotasi berdasarkan sudut kemiringan plat
# angle = -15
# height, width = image.shape[:2]
# center = (width // 2, height // 2)
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
# rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)


# # Tentukan persentase bagian atas dan bawah yang ingin dipotong
# top_percent = 1
# bottom_percent = 1

# # Hitung jumlah pixel yang akan dipotong dari bagian atas dan bawah
# top_cut = int(height * (top_percent / 100))
# bottom_cut = int(height * (bottom_percent / 100))

# # Potong bagian atas dan bawah gambar
# cropped_image = rotated_image[top_cut:-bottom_cut, :]
# cv2.imwrite(f"cropped_image_0.jpg", cropped_image)

# output = reader.readtext('cropped_image_0.jpg')
# output = sorted(output, key=lambda x: x[0][0])

# # Menyimpan hasil gabungan ke dalam variabel
# result_string = " ".join(output[i][1] for i in range(0,len(output)))
# result_string = result_string.upper()

# filtered_text = "K1_" + re.sub(r"[^a-zA-Z0-9]", "", result_string)
# print(filtered_text)
