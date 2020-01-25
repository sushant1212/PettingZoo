#!/usr/bin/env python3

import numpy as np
from .multi_walker_base import MultiWalkerEnv

env = MultiWalkerEnv()
env.reset()
done = False

while not done:
    env.render()
    a = np.array([env.agents[0].action_space.sample() for _ in range(env.n_walkers)])
    o, r, done, _ = env.step(a)
    if done:
        print("done is ", done)
        break
