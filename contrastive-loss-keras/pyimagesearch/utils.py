# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------
#   FUNCTIONS
# -----------------------------
def make_pairs(images, labels):
    # Initialize two empty lists to hold the (image, image) pairs and labels to indicate
    # if a pair is positive or negative
    pairImages = []
    pairLabels = []
    # Calculate the total number of classes present in the dataset and then build a list of indexes for each class
    # label that provides the indexes for all examples with a given label
    numClasses = len(np.unique(labels))
    idx = [np.where(labels == i)[0] for i in range(0, numClasses)]
    # Loop over all images
    for idxA in range(len(images)):
        # Grab the current image and label belonging to the current iteration
        currentImage = images[idxA]
        label = labels[idxA]
        # Randomly pick an image that belongs to the *same* class label
        idxB = np.random.choice(idx[label])
        posImage = images[idxB]
        # Prepare a positive pair and update the images and labels list, respectively
        pairImages.append([currentImage, posImage])
        pairLabels.append([1])
        # Grab the indices for each of the class labels *not* equal t the current label and randomly pick an image
        # corresponding to a label *not* equal to the current label
        negIdx = np.where(labels != label)[0]
        negImage = images[np.random.choice(negIdx)]
        # Prepare a negative pair of images and update the lists
        pairImages.append([currentImage, negImage])
        pairLabels.append([0])
    # Return a 2-tuple of the image pairs and labels
    return np.array(pairImages), np.array(pairLabels)


def euclidean_distance(vectors):
    # Unpack the vectors into separate lists
    (featsA, featsB) = vectors
    # Compute the sum of squared distances between the vectors
    sumSquared = K.sum(K.square(featsA - featsB), axis=1, keepdims=True)
    # Return the euclidean distance between the vectors
    return K.sqrt(K.maximum(sumSquared, K.epsilon()))


def plot_training(H, plotPath):
    # Construct a plot that plots and saves the training history in a given path
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(H.history["loss"], label="train_loss")
    plt.plot(H.history["val_loss"], label="val_loss")
    plt.title("Training Loss")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss")
    plt.legend(loc="lower left")
    plt.savefig(plotPath)
