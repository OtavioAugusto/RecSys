import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


#data="/home/piim/Documentos/RecSys2017/Movielens LDA/log.txt"
data="/home/piim/Documentos/MovieLens/ml-1m/ratings.dat"
di   = defaultdict(lambda: 0.0)
for line in open(data,"r"):
	q        = line.strip().split("::")
	item     = q[1]
	di[item] = di[item] + 1.0

d = sorted([di[i] for i in di.keys()])
print "num movies", len(di.keys())
print d[:10]
print d[-10:]

s = 0.0
for i in d:
	s += i

num_items = len(d)
print 'sum ', s
x = [float(sum(d[:i])/s) for i in range(1,num_items+1)]
y = [float(float(e)/float(num_items)) for e in range(1,num_items+1)]

print 'x---', len(x)
print x[:10]
print x[-10:]

print 'y---', len(y)
print y[:10]
print y[-10:]

ax = plt.subplot()
f = plt.figure()
#plt.yscale('log')
#plt.yticks((0,0.001,0.01,1.0,10.0))
plt.plot(x,y)
plt.show(block=False)
f.savefig("a.pdf")
