__author__ = 'O.Augusto'
__filename__ = "run_all.py"

from policy_evaluator import PolicyEvaluator
from BayesUCB import BayesUCB
from EpsilonGreedy import EpsilonGreedy
#from LinUCB import LinUCB
from ThompsonSampling import ThompsonSampling
from UCB1 import UCB1
from UCB2 import UCB2
from RandomChoice import RandomChoice
import copy

#num_runs = 1
cell = 1
num_cluster = [5]#[5,10,17,25,50,100]

for x in num_cluster:
	context = {
	'mab'          : copy.copy(BayesUCB()),
	'log_file'     : 'log.txt',
	'column'       : cell,
	'cluster'      : x
	}
	#print x, j
	if __name__ == '__main__':
		evaluator = PolicyEvaluator(context)#, num_runs)
		evaluator.run()
	cell += 1
		
