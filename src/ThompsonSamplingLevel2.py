__author__ = 'O.Augusto'
__filename__ = "ThompsonSamplingLevel2.py"

from collections import defaultdict
from numpy.random import beta
from operator import itemgetter

class ThompsonSamplingLevel2(object):
	def __init__(self):
		self.flag_set = False

	def set_arms(self, n_arms):
		self.param_alpha   = defaultdict(lambda: None)
		self.param_beta    = defaultdict(lambda: None)
		self.num_successes = defaultdict(lambda: None)
		self.num_fails     = defaultdict(lambda: None)
		#self.counts = [0 for col in range(n_arms)]
		for arm in range(n_arms):
			self.param_alpha[arm]   = 1.0
			self.param_beta[arm]    = 1.0
			self.num_successes[arm] = 0.0
			self.num_fails[arm]     = 0.0
		self.n_arms = n_arms

		self.counts = defaultdict(lambda: None)
		for arm in range(self.n_arms):
			self.counts[arm] = 0
		self.flag_set = True
		return

	def choose_arm(self):
		if self.flag_set == False:
			print 'Error: Thompson Sampling not set. Aborting'
			import sys
			sys.exit(1)

		scores = [(arm_id, beta(self.num_successes[arm_id] + self.param_alpha[arm_id],
                       self.num_fails[arm_id] + self.param_beta[arm_id]))
                       for arm_id in range(self.n_arms)]
		
		scores = sorted(scores, key=itemgetter(0))
		ranking = sorted(scores, key=itemgetter(1), reverse=True)
		selected_arm = ranking[0][0]
		return selected_arm

	def update(self, chosen_arm, reward):
		if self.flag_set == False:
			print 'Error: Thompson Sampling not set. Aborting'
			import sys
			sys.exit(1)		

		if chosen_arm not in range(self.n_arms):
			print '--- self.n_arms'
			print self.n_arms
			print '--- chosen arm'
			print chosen_arm
			print 'Error in thompson sampling. Invalid chosen arm. Aborting'
			sys.exit(1)

		if reward == 1.0:
			self.num_successes[chosen_arm] += 1.0
		elif reward == 0:
			self.num_fails[chosen_arm] += 1.0
		else:
			print 'Error in thompson sampling. Invalid reward. Aborting'
			sys.exit(1)
		return

