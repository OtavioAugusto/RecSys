__author__ = 'O.Augusto'
__filename__ = "select_arm.py"

# Policy Evaluator implements LTR (Like Through Rate) 

from RandomChoiceLevel2 import RandomChoiceLevel2
from UCB1level2 import UCB1level2
from ThompsonSamplingLevel2 import ThompsonSamplingLevel2
from BayesUCBlevel2 import BayesUCBlevel2
from EpsilonGreedyLevel2 import EpsilonGreedyLevel2
from UCB2Level2 import UCB2Level2
import copy
import policy_evaluator
from collections import Counter
from collections import defaultdict
import sys
import numpy as np
import os

class select_arm(object):
	def __init__(self, cluster, ncluster):
		self.cluster   = cluster
		self.ncluster  = ncluster
		self.mab_alg   = copy.copy(BayesUCBlevel2())
		self.log_file  = 'Movielens LDA/clusters/%s/movie_cluster_%s.txt' %(self.ncluster, self.cluster)
                self.idvideo2idarm = defaultdict(lambda: None)
		self.idarm2idvideo = defaultdict(lambda: None)
                self.contidarm = 0
		self.before    = defaultdict(lambda: None)

		if os.stat(self.log_file).st_size == 0:
			self.contidarm = 1
		
                #print 'Policy evaluator started with log file %s' % (self.log_file)

		self.count_itens = defaultdict(lambda: 0)
		intro_file = open(self.log_file, 'r')
		logs = intro_file.readlines()
		logs2 = logs
		intro_file.close()
		for line in logs:
			arm_id, inf_value = line.strip().split(',')
			self.count_itens[arm_id] += 1
		
                for line in logs2:
			arm_id, inf_value = line.strip().split(',')
			if arm_id not in self.idvideo2idarm:
                        	self.idvideo2idarm[arm_id] = self.contidarm
 				self.idarm2idvideo[self.contidarm] = arm_id
                              	self.contidarm += 1

		#print 'Selected videos %s' % self.contidarm 	
                self.mab_alg.set_arms(self.contidarm)
		self.before = self.mab_alg.choose_arm()
		self.count_n = 0		

	def get_video(self):
		self.mab_alg.set_arms(self.contidarm)
		recommendation = self.mab_alg.choose_arm()
                tmp_id_arm     = self.idarm2idvideo[recommendation]
		#print 'Selected arm:', tmp_id_arm
		if (self.before == recommendation):
			reward = 1.0
			self.count_n += 1
		else:
			reward = 0.0
		self.mab_alg.update(recommendation, reward)
		self.before = recommendation
		return tmp_id_arm
		

'''
#TEST
x=2
num_model=100
#mab_alg = copy.copy(RandomChoiceLevel2())
pegararm = select_arm(x,num_model)
video = pegararm.get_video()
print video'''

