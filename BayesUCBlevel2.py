__author__ = 'O.Augusto'
__filename__ = "BayesUCBlevel2.py"

import sys
from collections import defaultdict
#from Posterior import Posterior
from Beta import Beta
import numpy as np

class BayesUCBlevel2():
	def __init__(self):
		self.flag_set = False

	def set_arms(self, n_arms):
		self.posterior_dist = Beta
		self.t         = 1.0
		self.arms      = n_arms
		self.posterior = defaultdict(lambda: None)
		for arm_id in range(self.arms):
			self.posterior[arm_id] = self.posterior_dist()
		for arm_id in range(self.arms):
			self.posterior[arm_id].reset()
		self.flag_set = True
		return

	def compute_index(self, arm_id):
		if self.flag_set == False:
			print 'Error: BayesUCB not set. Aborting'
			import sys
			sys.exit(1)

		return self.posterior[arm_id].quantile(1 - (1. / self.t))

	def choose_arm(self):
		if self.flag_set == False:
			print 'Error: BayesUCB not set. Aborting'
			import sys
			sys.exit(1)
		
		index = dict()
		for arm_id in range(self.arms):
			index[arm_id] = self.compute_index(arm_id)
		best_arm = np.argmax(index.values())
		#best_arm_id = [arm_id for arm_id in range(len(index.keys())) if index[arm_id] == best_arm][0]
		return best_arm

	def update(self, chosen_arm, reward):
		if self.flag_set == False:
			print 'Error: BayesUCB not set. Aborting'
			import sys
			sys.exit(1)

		if chosen_arm not in range(self.arms):
			print 'Error in BayesUCB. Invalid chosen arm. Aborting.'
			sys.exit(1)

		self.posterior[chosen_arm].update(reward)
		self.t += 1
		return
