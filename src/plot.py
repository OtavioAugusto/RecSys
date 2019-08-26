import matplotlib.pyplot as plt
import sys
import numpy
import codecs	
import re

num_cluster = [1]#,5,10,25,50,100]

for i in num_cluster:
	#ax = plt.subplot(111)
	converted = []
	#reward = [0, 0.0, 1.0, 2.0, 3.0]
	reward = open('Movielens test2/clusters/Arrays/RandomChoice/reward_%s_clusters'%(i),'r')
	acum = reward.readlines()
	for line in acum:
    		if line.startswith(codecs.BOM_UTF8):
        		line = line[len(codecs.BOM_UTF8):]
    		x = line.split(', ')
		print x
		converted.append(x)
	#print converted
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																	
	#plt.rcParams['agg.path.chunksize'] = 1000000
	plt.plot(converted, label=str(i)+' clusters')
	plt.ylabel('Reward')
	plt.xlabel('Time')
	#plt.yscale('linear')
	plt.title('Cumulative Reward RandomChoice') #Pay attention for this
	plt.grid(True)
	#box = ax.get_position()
	#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
	plt.legend(loc=0)
	plt.show(block=False)
	plt.savefig('Movielens test2/clusters/Arrays/RandomChoice/cumulative_reward_RandomChoice.png')
	print 'Plot complete'
print 'End of run'
