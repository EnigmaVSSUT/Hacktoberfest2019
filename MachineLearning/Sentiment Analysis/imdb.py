import os
# from download import download
import glob

# Directory to save the downloaded data
data_dir = "D:\\Ongoing work\\PROJECTS\\Image Captioning\\NLP-Sentiment Analysis"

# URL for the data-set on the internet
data_url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

# Private helper funcions

def _read_text_file(path):
	# Read and return alll the content of the text file with the given path

	with open(path, 'rt', encoding = 'utf-8') as file:
		# Read a list of string
		lines = file.readlines()

		# Concatenate to a single string.
		text = " ".join(lines)

	# return text
	print(text)

# Public function that is required to download the data-set and save it to memory

def maybe_download_and_extract():
	# Download the imdb data if it doesn't already exist in data_dir

	data_dir = download(data_url, "D:\\Ongoing Work\\Tensorflow\\NLP-Sentiment analysis")
	

def load_data(train  = True):
	# load the data for sentiment analysis.
	'''
		parameter : train = Boolean whether to load the train-set->True or the test-set -> False

		what it gonna return? A list of reviews as text-strings, 
		and a list of the corresponding sentiments where 1.0 is positive and 0.0 is negative.

	'''

	# Part of the path-name for either train or test-set
	train_test_path = "train" if train else "test"
	

	# Base directory where the extracted data is located
	dir_base = os.path.join(data_dir, "aclImdb", train_test_path)

	# Filename-patterns for the data-files
	path_pattern_pos = os.path.join(dir_base, "pos", "*.txt")
	path_pattern_neg = os.path.join(dir_base, "neg", "*.txt")

	# Get list of all the file-paths for the data
	path_pos = glob.glob(path_pattern_pos)
	path_neg = glob.glob(path_pattern_neg)

	# Read all the text_files
	data_pos = [_read_text_file(path) for path in path_pos]
	data_neg = [_read_text_file(path) for path in path_neg]

	# Concatenate the positive and negative data
	x = data_pos + data_neg

	# Create a list of the sentiments for the text-data
	# where 1.0 is for positive sentiment and 0.0 is for negative sentiment

	y = [1.0]*len(data_pos) + [0.0] * len(data_neg)

	return x,y
