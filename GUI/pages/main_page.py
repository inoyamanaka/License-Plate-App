# Guide User Interface related
import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile, askdirectory
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from prettytable import PrettyTable
from tkinter import messagebox
from tkinter.tix import IMAGETEXT

# Image Preprocessing and OCR related
import yolov5
import cv2
import easyocr
import numpy as np
from scipy import ndimage
import re
import math

sys.path.append('D:/python/license-plate-application')
from GUI.pages.home_page import HomePage
from GUI.services.multi_test_detection import MultiLicensePlateProcessor
from GUI.services.single_test_detection import LicensePlateProcessor


processor = LicensePlateProcessor()
multi_processor = MultiLicensePlateProcessor()

if __name__ == "__main__":
    root = tk.tkinter.Tk()
    app = HomePage(root, processor, multi_processor)