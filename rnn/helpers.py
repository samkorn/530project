# https://github.com/spro/practical-pytorch

import unidecode
import string
import random
import time
import math
import torch
from torch.autograd import Variable
import tensorflow as tf
import numpy as np

# Reading and un-unicode-encoding data

#all_characters = string.printable
#n_characters = len(all_characters)

def read_file(filename):
    file = unidecode.unidecode(open(filename).read())
    return file, len(file)

# Turning a numpy.array into a tensor
def convert_to_tensor(vector):
    tf.convert_to_tensor(data_np, np.float32)
    

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)