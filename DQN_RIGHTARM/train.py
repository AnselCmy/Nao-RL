# @Author   : Chen Mingyang
# @Time     : 2018/11/20
# @FileName : train.py

from DQN import DQN
from Env import Env
import numpy as np
from params import *
import torch

dqn = DQN()
env = Env(TARGET)

for i_episode in range(EPISODE):
    curr_state = env.reset()
    ep_r = 0
    while True:
        action = dqn.choose_action(curr_state)
        next_state, reward, done = env.step(action)
        dqn.store_transition(curr_state, action, reward, next_state)
        # print(curr_state, action, reward, next_state)
        ep_r += reward
        if dqn.memory_counter > MEMORY_CAPACITY:
            dqn.learn()
            if done[0]:
                print('Ep: ', i_episode,
                      '| Ep_r: ', round(ep_r, 2),
                      '| pos: ', env.get_state().numpy())
        if done[0]:
            break
        curr_state = next_state

torch.save(dqn.eval_net, 'eval_net.pkl')
torch.save(dqn.target_net, 'target_net.pkl')
