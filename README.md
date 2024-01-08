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

# Running the License Plate Detector

To use the license plate detector program, follow these steps:

1. **Open Command Prompt or Terminal:**
   Make sure to open Command Prompt (Windows) or Terminal (Linux/macOS) in the directory containing the executable.

2. **Run the Program:**
   Enter the following command to run the license plate detector program:

    ```
    cd path/to/dist
    main_page.exe
    ```

    Be sure to replace `path/to/dist` with the path to the directory containing the executable file (`main_page.exe`).

3. **Follow Program Instructions:**
   The program may prompt for input or execute specific actions based on your application design. Follow the on-screen instructions.

4. **View Results:**
   The detected license plates and recognized characters will be displayed on the screen or directed to the appropriate output.

Ensure that you have provided clear steps and necessary information to ensure users can run the program smoothly. Include additional information such as required Python versions, and make sure users have installed the necessary dependencies before running the program.


## Customization

- For customizing YOLOv5 settings, refer to the YOLOv5 documentation: https://github.com/ultralytics/yolov5

- For customizing OCR settings, refer to the Tesseract OCR documentation: https://github.com/tesseract-ocr/tesseract

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
