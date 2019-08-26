__author__ = 'O.Augusto'
__filename__ = "RandomChoice.py"

import numpy as np
import random

class RandomChoice(object):
    def __init__(self):
	self.flag_set = False

    def set_arms(self, n_arms):
	self.n = n_arms
        self.counts = [0] * n_arms
        self.values = [0.] * n_arms
	self.flag_set = True

    def choose_arm(self):
	if self.flag_set == False:
		print 'Error: Random Choice not set. Aborting'
		import sys
		sys.exit(1)

        """Choose an random arm """
        # Explore (test all arms)
        return np.random.randint(self.n)

    def update(self, choosen_arm, reward):
	if self.flag_set == False:
		print 'Error: Random Choice not set. Aborting'
		import sys
		sys.exit(1)

        """Update an arm with some reward value"""
        self.counts[choosen_arm] = self.counts[choosen_arm] + 0.1
        n = self.counts[choosen_arm]
        value = np.random.randint(self.n) #self.values[choosen_arm]
        
	# Running product
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[choosen_arm] = new_value
        return
