# License Plate Detector using YOLOv5 and OCR 🚗🔍

This project aims to detect license plates in images using the YOLOv5 (You Only Look Once) object detection algorithm for plate segmentation. After segmentation, Optical Character Recognition (OCR) is applied to recognize the characters on the detected license plates.

## Requirements

- Python 3.6 or later
- YOLOv5 🚀
- Easy OCR (Optical Character Recognition) 📖
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/inoyamanaka/License-Plate-App.git
    cd license-plate-detector
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Download YOLOv5 weights:

    ```
    # From the project root directory
    mkdir weights
    cd weights
    wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
    ```

4. Download pre-trained OCR model:

    ```
    # From the project root directory
    mkdir ocr-model
    # Download the OCR model weights and place them in the 'ocr-model' directory
    ```
# License Plate Detector 🚗🔍


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/license-plate-detector.git
    ```

2. Navigate to the project directory:

    ```bash
    cd license-plate-detector
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open Command Prompt (Windows) or Terminal (Linux/macOS).

2. Navigate to the project directory:

    ```bash
    cd path/to/license-plate-detector
    ```

3. Run the license plate detector program:

    ```bash
    GUI/pages/main_page.py
    ```

    Replace `path/to/license-plate-detector` with the actual path to your project directory.

4. Follow the on-screen instructions to input images or configure the program settings.

5. View the results! 🎉 Detected license plates and recognized characters will be displayed on the screen or directed to the appropriate output.


## Customization

- For customizing YOLOv5 settings, refer to the YOLOv5 documentation: https://github.com/ultralytics/yolov5

- For customizing OCR settings, refer to the Tesseract OCR documentation: https://github.com/tesseract-ocr/tesseract

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
