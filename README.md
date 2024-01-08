# License Plate Detector using YOLOv5 and OCR

This project aims to detect license plates in images using the YOLOv5 (You Only Look Once) object detection algorithm for plate segmentation. After segmentation, Optical Character Recognition (OCR) is applied to recognize the characters on the detected license plates.

## Requirements

- Python 3.6 or later
- YOLOv5
- Tesseract OCR
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

## Usage

1. Run the license plate detector:

    ```
    python detect_license_plate.py --input image.jpg
    ```

    Replace `image.jpg` with the path to your input image.

2. View the results:

    The detected license plates and recognized characters will be displayed on the console.

## Customization

- For customizing YOLOv5 settings, refer to the YOLOv5 documentation: https://github.com/ultralytics/yolov5

- For customizing OCR settings, refer to the Tesseract OCR documentation: https://github.com/tesseract-ocr/tesseract

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
