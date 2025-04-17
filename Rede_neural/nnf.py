"""
This script demonstrates the usage of the NNFS library to train a neural network
using the Metropolis algorithm. It visualizes the predictions and error evolution.
"""

import matplotlib.pyplot as plt
import numpy as np
import nnfs

# commom parameters
layers = 3
neurons = 5
seed = 42
max_epochs = 100000
