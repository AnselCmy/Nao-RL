# @Author   : Chen Mingyang
# @Time     : 2018/11/20
# @FileName : test.py

from DQN import *
from Env import *
from params import *

dqn = DQN()
dqn.eval_net = torch.load('./eval_net.pkl')
dqn.target_net = torch.load('./target_net.pkl')

env = Env(TARGET)
curr_state = env.reset()
while True:
    action = dqn.choose_action(curr_state)
    next_state, reward, done = env.step(action)
    a = env.action_map(action)
    print("Joint: {}\tMove: {}\tState: {}".format(a[0], a[1], next_state))
    if done[0]:
        print(done[1])
        break
    curr_state = next_state

