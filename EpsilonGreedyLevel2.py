__author__ = 'O.Augusto'
__filename__ = "EpsilonGreedyLevel2.py"

import numpy as np
import random

class EpsilonGreedyLevel2(object):
    def __init__(self):
	self.flag_set = False

    def set_arms(self, n_arms):
	self.n = n_arms
        self.counts = [0] * n_arms   # number of likes
        self.values = [0.] * n_arms  # number of likes
	self.flag_set = True

    def choose_arm(self):
	if self.flag_set == False:
		print 'Error: Epsilon-greedy not set. Aborting'
		import sys
		sys.exit(1)

        """Choose an arm for testing"""
        epsilon = 1.0
        if np.random.random() > epsilon:
            # Exploit (use best arm)
            return np.argmax(self.values)
        else:
            # Explore (test all arms)
            return np.random.randint(self.n)

    def update(self, arm, reward):
	if self.flag_set == False:
		print 'Error: Epsilon-greedy not set. Aborting'
		import sys
		sys.exit(1)

        """Update an arm with some reward value"""  # Example: like = 1; no like = 0
	#print arm, type(arm)
        self.counts[arm] = self.counts[arm] + 1
        n = self.counts[arm]
        value = self.values[arm]
        # Running product
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[arm] = new_value
        return
