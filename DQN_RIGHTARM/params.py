# @Author   : Chen Mingyang
# @Time     : 2018/11/20
# @FileName : params.py

import numpy as np

CUDA = False

BATCH_SIZE = 32
EPISODE = 3000
LR = 0.01                   # learning rate
EPSILON = 0.8               # greedy policy
GAMMA = 0.9                 # reward discount
TARGET_REPLACE_ITER = 100   # target update frequency
MEMORY_CAPACITY = 2000

N_JOINTS = 4
N_ACTIONS_Per_JOINT = 2
ACTIONS_Per_JOINT = [-10, 10]   # action list for each joint
N_ACTIONS = N_JOINTS * N_ACTIONS_Per_JOINT
N_STATES = 3                # the states is position here, like (x, y, z)

PRECISION = 10              # precision for judging if done
TARGET = np.array([197.34, -98.0, 504.68])
