# Guide User Interface related
import sys
import os
import tkinter as tk

sys.path.append('D:/python/license-plate-application')
from GUI.pages.home_page import HomePage
from GUI.services.multi_test_detection import MultiLicensePlateProcessor
from GUI.services.single_test_detection import LicensePlateProcessor


processor = LicensePlateProcessor()
multi_processor = MultiLicensePlateProcessor()

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root, processor, multi_processor)