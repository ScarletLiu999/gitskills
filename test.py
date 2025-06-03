import cv2

img = cv2.imread('./data/CP-SLAM_dataset/desk2_part1/results/depth00000.png', cv2.IMREAD_UNCHANGED)
print(img.dtype) 

