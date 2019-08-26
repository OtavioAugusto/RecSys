__author__ = 'O.Augusto'
__filename__ = "policy_evaluator.py"

# Policy Evaluator implements CTR (Click Through Rate) 

from select_arm import select_arm
#from arm_selection import arm_selection
from bootstrap import bootstrap
from collections import Counter
from collections import defaultdict
from xlrd import open_workbook
from xlutils.copy import copy
import matplotlib.pyplot as plt
import sys
import numpy as np

class PolicyEvaluator(object):
	def __init__(self, context):#, num_runs):
		self.context           = context
		self.mab_alg           = context['mab']
		self.log_file  	       = context['log_file']
		self.column	       = context['column']
		self.ncluster           = context['cluster']
		#self.num_runs          = num_runs

		self.cumulative_reward = [ ]
                '''self.idcluster2idarm     = defaultdict(lambda: None)
		self.idarm2idcluster     = defaultdict(lambda: None)'''
		self.idvideo2idarm = defaultdict(lambda: None)
		self.idarm2idvideo = defaultdict(lambda: None)
                self.contidarm         = 0
                #print 'Policy evaluator started with file %s' % (self.log_file)
		
		#used only for videos
		'''self.count_itens = defaultdict(lambda: 0)
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
		print 'Selected videos %s' % self.contidarm'''
		
		self.contidarm = self.ncluster
		print 'Selected clusters %s' % self.contidarm
                self.mab_alg.set_arms(self.contidarm)

	def run(self):
		tmp_result = []
		rme_result = []
		rle_result = []
		self.mab_alg.set_arms(self.contidarm)
		self.cumulative_reward = [ ]
		
		#Verifying most and less ratings
		me = []
		le = []
		rat = open('vids_very_ratings.txt', 'r')
		lrat = open('vids_less_ratings.txt', 'r')
		acum = rat.readlines()
		acum1 = lrat.readlines()
		rat.close()
		lrat.close()
		#
			
		count_n = 0.0
		intro_file = open(self.log_file, 'r')
		logs = intro_file.readlines()
		intro_file.close()
		for line in logs:
			user_id, item_id = line.strip().split(',')
			cluster = self.mab_alg.choose_arm()
			get_arm = select_arm(cluster, self.ncluster)
			recommendation = get_arm.get_video()
			'''recommendation = self.mab_alg.choose_arm()
                        tmp_id_arm     = self.idarm2idvideo[recommendation]
			if (item_id == tmp_id_arm):'''
			if (item_id == recommendation):
				reward = 1.0
				count_n += 1
				for line in acum: #verifying if video is in most or less ratings
					item_r = line.strip()								
					if recommendation == item_r: 
						rme = 1.0
						me.append(rme)
				for line in acum1:
					item_l = line.strip()
					if recommendation == item_l:
						rle = 1.0
						le.append(rle)
			else:
				reward = 0.0
			self.mab_alg.update(cluster, reward)
			#self.mab_alg.update(recommendation, reward)
			self.cumulative_reward.append(reward)
		rme_result.append([sum(me[0:i]) for i, value in enumerate(me)])
		rle_result.append([sum(le[0:i]) for i, value in enumerate(le)])
		tmp_result.append([sum(self.cumulative_reward[0:i]) for i, value in enumerate(self.cumulative_reward)])
		mean_tmp_result = np.mean(tmp_result, axis=0)
		std_tmp_result = np.std(tmp_result, axis=0)
		final = open('Movielens LDA/clusters/Arrays/BayesUCB/reward_%s_clusters_test'%(self.ncluster),'w')
		final.write(str(tmp_result))
		final.close()
		veryrew = open('Very reward.txt','w')
		veryrew.write(str(rme_result))
		veryrew.close()
		lowrew = open('Low reward.txt','w')
		lowrew.write(str(rle_result))
		lowrew.close()

		# Open an Excel file and add a worksheet.
		rb = open_workbook("Results.xls")
		wb = copy(rb)
		# Write text in cells.
		worksheet = wb.get_sheet(0) #Pay attention for this
		worksheet.write(21, self.column, str(round(np.mean(mean_tmp_result))) + ' - ' + str(np.std(std_tmp_result)))
		wb.save('Results.xls')

		rc = open_workbook("Ratings_frequency.xls")
		wc = copy(rc)
		# Write text in cells.
		wks = wc.get_sheet(0) #Pay attention for this
		wks.write(2, 1, 'Muitas avaliacoes: ' + str(round(np.mean(rme_result))) +
				'Poucas avaliacoes: ' + str(round(np.mean(rle_result))))
		wc.save('Ratings_frequency.xls')
