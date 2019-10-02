This algorithm helps to convert sequence of depth images from a video into its gait energy image representation so as to be used in action recognition deep learning algorithms.

Requirements
1. opencv-python
2. matplotlib
3. numpy
4. argparse
5. python2 or python3

input - will be a folder of depth images
output - will be a gait energy image representation of the sequence of depth images. Depth images must preferably be silhouette images.

It can used as follows by the following command
python gait_energy_images.py --input {input_path} --output {output_path}