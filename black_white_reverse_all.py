import os
import cv2
from PIL import Image
import numpy as np
# https://stackoverflow.com/questions/2498875/how-to-invert-colors-of-image-with-pil-python-imaging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, required=True)
args = parser.parse_args()


perception_dir = '<Generated Water Segmentation Path>'
new_dir = 'SemanticBinarySegmentation'
folder = args.folder # 'f2bd36b3-c378-43c0-94c5-02f6584af2db'
segmentation_dir = 'SemanticSegmentation'

folder_path = args.folder # os.path.join(perception_dir, folder)

datasets = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
print(datasets)

for dataset in datasets:
    entry_path = os.path.join(folder_path, dataset) 

    seg_dirs = [d for d in os.listdir(entry_path) if os.path.isdir(os.path.join(entry_path, d)) and d.startswith(segmentation_dir)]
    # print(seg_dirs)
    # seg_dir = dirs[0] # args.seg_dir # 'SemanticSegmentation50319505-b3aa-4616-8779-b630e5f1ed33'

    for seg_dir in seg_dirs:
        full_path =  os.path.join(entry_path, seg_dir)
        print("full path: ", full_path)

        for file in os.listdir(full_path):

            filename = os.path.join(full_path, file)
            
            rgb_image = Image.open(filename).convert("1")
            inverted_image = Image.eval(rgb_image, lambda x: 255 - x)
            inverted_image.save(filename)

   
print('all images inverted')     


