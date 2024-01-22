import argparse
import os
from pathlib import Path
import shutil

class YOLOv5Trainer:
    def __init__(self, img_size, batch_size, epochs, data_path, weights_path):
        self.img_size = img_size
        self.batch_size = batch_size
        self.epochs = epochs
        self.data_path = data_path
        self.weights_path = weights_path

    def train_yolov5(self):
        if os.path.exists('yolov5/runs/train/exp'):
            shutil.rmtree('yolov5/runs/train/exp')
        
        command = (
            f"python yolov5/train.py --img {self.img_size} "
            f"--batch {self.batch_size} --epochs {self.epochs} "
            f"--data {self.data_path} --weights {self.weights_path}"
        )
        print("Training YOLOv5 with command:")
        print(command)
        
        # Uncomment the line below to actually run the training command
        os.system(command)
        

if __name__ == "__main__":
    # Example usage
    trainer = YOLOv5Trainer(
        img_size=640,
        batch_size=16,
        epochs=3,
        data_path="D:/python/license-plate-application/roboflowdata/data.yaml",
        weights_path="yolov5/yolov5s.pt",
    )
    trainer.train_yolov5()
