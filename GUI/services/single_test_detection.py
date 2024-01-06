import os
import yolov5
import cv2
import easyocr
import numpy as np
from scipy import ndimage
import re
import math

class LicensePlateProcessor:
    def __init__(self, model_path='keremberke/yolov5m-license-plate'):
        self.reader = easyocr.Reader(['en'])
        self.model = yolov5.load(model_path)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 3
        self.font_thickness = 5
        self.font_color = (0, 255, 0)
        self.plate_character = ''

    def reverse_and_keep_letters(self, input_str):
        reversed_str = input_str[::-1]
        result_str = ''
        found_letter = False

        for char in reversed_str:
            if char.isalpha():
                found_letter = True
            if found_letter or char.isalpha():
                result_str += char

        return (result_str[::-1].upper()).replace(" ", "")

    def find_longest_alphanumeric_list(self, text):
        longest_element = max(text, key=lambda s: sum(c.isalnum() for c in s))
        return longest_element
    
    def get_character(self):
        return self.plate_character


    def process_image(self, img_path, filename):
        try:
            img = img_path
            results = self.model(img, size=640)
            results = self.model(img, augment=True)

            predictions = results.pred[0]
            boxes = predictions[:, :4]
            scores = predictions[:, 4]

            data = np.array(boxes)
            perbedaan_x = data[:, 2] - data[:, 0]
            indeks_tertinggi = np.argmax(perbedaan_x)
            image = cv2.imread(img)

            x1, y1, x2, y2 = boxes[indeks_tertinggi]

            cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
            grayscale = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
            tepi = cv2.Canny(grayscale, 50, 150, apertureSize=3)
            garis = cv2.HoughLinesP(tepi, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
            angles = []

            try:
                for [[x1, y1, x2, y2]] in garis:
                    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
                    angles.append(angle)
            except:
                angles.append(0)

            median_angle = np.median(angles)
            print(median_angle)

            if abs(median_angle) > 60:
                median_angle = 0

            img_rotated = ndimage.rotate(cropped_image, median_angle)

            gray = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2GRAY)
            jumlah_pixel_putih = cv2.inRange(gray, 200, 255).sum()
            jumlah_pixel_hitam = cv2.inRange(gray, 0, 50).sum()

            result = self.reader.readtext(img_rotated,
                                          decoder='beamsearch',
                                          min_size=20,
                                          add_margin=0.5,
                                          adjust_contrast=0.8,
                                          bbox_min_size=5, detail=0, paragraph=True, text_threshold=0.8, max_candidates=1)

            reversed_output = [self.reverse_and_keep_letters(item) for item in result]
            result_rr = self.find_longest_alphanumeric_list(reversed_output)
            self.plate_character = result_rr

            x1, y1, x2, y2 = boxes[indeks_tertinggi]

            imgDraw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), self.font_color,
                                    self.font_thickness)

            imgDraw3 = cv2.putText(imgDraw, result_rr, (int(x1), int(y1) - 10), self.font, self.font_scale,
                                   self.font_color, self.font_thickness)

            cv2.imwrite(f"GUI/outputs/single/cropped_img/cropped_image_{filename}", cropped_image)
            cv2.imwrite(f'GUI/outputs/single/angle_fix_img/gambar_lurus_{filename}', img_rotated)
            cv2.imwrite(f"GUI/outputs/single/final_img/text_draw_{filename}", imgDraw3)
            
        except Exception as e:
            print("Error in processing image:", img_path)
            print(e)



