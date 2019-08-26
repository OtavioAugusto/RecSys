__author__ = 'O.Augusto'
__filename__ = "UCB1.py"

import math

def ind_max(x):
  m = max(x)
  return x.index(m)

class UCB1(object):
    def __init__(self): #, counts, values):
        #self.counts = counts
        #self.values = values
        #return
	self.flag_set = False

    def set_arms(self, n_arms):
	self.n = n_arms
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]
	self.flag_set = True
        return

    def choose_arm(self):
	if self.flag_set == False:
		print 'Error: UCB not set. Aborting'
		import sys
		sys.exit(1)

        n_arms = len(self.counts)
        for arm in range(n_arms):
            if self.counts[arm] == 0:
                return arm

        ucb_values = [0.0 for arm in range(n_arms)]
        total_counts = sum(self.counts)
        for arm in range(n_arms):
            bonus = math.sqrt((2 * math.log(total_counts)) / float(self.counts[arm]))
            ucb_values[arm] = self.values[arm] + bonus
        return ind_max(ucb_values)

    def update(self, chosen_arm, reward):
	if self.flag_set == False:
		print 'Error: UCB not set. Aborting'
		import sys
		sys.exit(1)

        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        n = self.counts[chosen_arm]

        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
        return
