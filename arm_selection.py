__author__ = 'O.Augusto'
__filename__ = "arm_selection.py"

import policy_evaluator
from numpy.random import multinomial

class arm_selection(object):
	def __init__(self, cluster, model, num_model):
		self.cluster   = cluster
		self.model     = model
		self.num_model = num_model

	def get_video(self):
		video = open('/home/piim/Documentos/RecSys2016/clusters/%s%s/video_prob_cluster_%s.txt' %(self.model, self.num_model, self.cluster),'r')
		num_arms_selected  = 0
		probability_values = []
		item = []
		for line in video:
			item_id, prob_value = line.strip().split(',')
			#item_id = int(item_id)
			prob_value = float(prob_value)
			num_arms_selected += 1
			probability_values.append(prob_value)
			item.append(item_id)
		#print sum(probability_values), len(probability_values)
		arms         = multinomial(num_arms_selected, probability_values, size=1)
		position_arm = arms.argmax()
		selected_arm = item[position_arm]
		#print 'Selected arm:', selected_arm
		return selected_arm

# TEST
"""
x=0
pegararm = arm_selection(x)
video = pegararm.get_video()
print video
"""
