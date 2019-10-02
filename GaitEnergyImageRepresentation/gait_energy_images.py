import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import os

def gait_energy_image(path):
    success = 1
    video_frames = []
    allow = False
    for image in os.listdir(path): 
        image = cv2.imread(os.path.join(path,image))
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        video_frames.append(img)
    cv2.destroyAllWindows()
    Gt = np.zeros(video_frames[0].shape)
    for i in range(len(video_frames)):
        Bt = video_frames[i]
        Bt = Bt.astype(int)
        Gt = Gt+Bt
    Gt = Gt/len(video_frames)
    return Gt

def main(args):
	gei = gait_energy_image(args.input)
	plt.imsave(args.output,gei,cmap='gray')


if __name__=='__main__':
  parser = argparse.ArgumentParser(description="training settings")
  parser.add_argument('--input',type = str, help='input_folder_path_of_depth_images')
  parser.add_argument('--output',type = str, default='*.jpg', help='output_path_of_video')
  args = parser.parse_args()
  main(args)
