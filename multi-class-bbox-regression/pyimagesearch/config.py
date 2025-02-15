# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
import os

# Define the base path to the input dataset and then use it to derive the path to the input images and annotation files
BASE_PATH = "dataset"
IMAGES_PATH = os.path.sep.join([BASE_PATH, "images"])
ANNOTATIONS_PATH = os.path.sep.join([BASE_PATH, "annotations"])

# Define the path to the base output directory
BASE_OUTPUT = "output"

# Define the path to the output model, label binarizer, plots output directory and the testing image paths
MODEL_PATH = os.path.sep.join([BASE_PATH, "detector.h5"])
LB_PATH = os.path.sep.join([BASE_PATH, "lb.pickle"])
PLOTS_PATH = os.path.sep.join([BASE_OUTPUT, "plots"])
TEST_PATHS = os.path.sep.join([BASE_OUTPUT, "test_paths.txt"])

# Initialize the initial learning rate, number of epochs to train for and the batch size
INIT_LR = 1e-4
NUM_EPOCHS = 20
BATCH_SIZE = 32
