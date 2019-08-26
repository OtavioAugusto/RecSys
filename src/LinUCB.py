__author__ = 'O.Augusto'
__filename__ = "LinUCB.py"

import math
import numpy as np
from collections import defaultdict

class LinUCB(object):
	def __init__(self):
		self.flag_set = False

	def set_arms(self, n_arms):
		self.n = n_arms
		self.ALPHA = 0.1
		self.counts = [0 for col in range(n_arms)]
		self.num_dimensions = 6
		self.A = defaultdict(lambda: None)
		self.b = defaultdict(lambda: None)
		for arm_id in range(n_arms):
			self.A[arm_id] = np.identity(self.num_dimensions)
			self.b[arm_id] = np.zeros((self.num_dimensions, 1))
	
		self.flag_set = True		

	def choose_arm(self):
		if self.flag_set == False:
			print 'Error: LinUCB not set. Aborting'
			import sys
			sys.exit(1)

		theta = defaultdict(lambda: None)
		p = []
		for arm_id in range(self.n):
			inv_A = np.linalg.inv(self.A[arm_id])
			theta[arm_id] = np.dot(inv_A,
                             self.b[arm_id])
			x = np.array([[float(v) for i,v in sorted(user_features.iteritems())]]).T

			# estimated mu
			tx = float(np.dot(theta[arm_id].T, x))
			# confidence interval
			cb = self.ALPHA * math.sqrt(np.dot(np.dot(x.T, inv_A), x))

			p.append((arm_id, tx + cb))

		return p
		

	def update(self, chosen_arm, reward):
		if self.flag_set == False:
			print 'Error: LinUCB not set. Aborting'
			import sys
			sys.exit(1)

		x = np.array([[float(v) for i,v in sorted(user_features.iteritems())]]).T
		self.A[chosen_arm] += np.dot(x, x.T)
		self.b[chosen_arm] += (reward * x)
		return
