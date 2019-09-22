
import matplotlib.pyplot as plt
import random
import sobol_seq
import numpy as np
import chaospy as cp


fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True,figsize=(15,6))
#fig.suptitle("Plots of 2D Random Number Generators")
N = [1000, 5000, 10000, 20000, 50000]

for i in range(len(N)):
	x = [ random.random() for k in range(N[i]) ]
	y = [ random.random() for k in range(N[i]) ]
	axes = plt.subplot(2,5,i + 1)
	plt.xlim(0.0,1.0)
	plt.ylim(0.0,1.0)
	axes.set_title('N=' + str(N[i]))
	axes.set_aspect('equal')
	plt.scatter(x,y,s=1)
	if i == 0:
		axes.set_ylabel('Pseudo-Random',rotation=90,size='large')
	else:
		axes.get_yaxis().set_ticklabels([])
	axes.get_xaxis().set_ticklabels([])

for i in range(len(N)):
	z = sobol_seq.i4_sobol_generate(2,N[i])
	x = z[:,0]
	y = z[:,1]
	axes = plt.subplot(2,5,i + len(N) + 1)
	plt.xlim(0.0,1.0)
	plt.ylim(0.0,1.0)
	axes.set_aspect('equal')
	plt.scatter(x,y,s=1)
	if i == 0:
		axes.set_ylabel('Quasi-Random',rotation=90,size='large')
	else:
		axes.get_yaxis().set_ticklabels([])

fig.tight_layout()
plt.subplots_adjust(wspace=0.1,hspace=0.1)
plt.show()

#-----------------------------------------------

fig, ax = plt.subplots(nrows=3, ncols=5,sharex=True,sharey=True,figsize=(15,9))
#fig.suptitle("Quasi-Random Sampling of Uniform, Normal, and Chi-Squared Distributions")
N = [1000, 5000, 10000, 20000, 50000]
nbins = 50
ax0 = None
ax1 = None
ax2 = None
for i in range(len(N)):
	x = [ random.random() for k in range(N[i]) ]
	if i == 0:
		axes = plt.subplot(3,5,i + 1)
		ax0 = axes
	else:
		axes = plt.subplot(3,5,i + 1, sharey = ax0, sharex = ax0)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	axes.set_title('N=' + str(N[i]))
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Uniform(0,1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])
	#axes.get_xaxis().set_ticklabels([])

for i in range(len(N)):
	x = [ np.random.normal() for k in range(N[i]) ]
	if i == 0:
		axes = plt.subplot(3,5,i + len(N) + 1)
		ax1 = axes
	else:
		axes = plt.subplot(3,5,i + len(N) + 1, sharey = ax1, sharex = ax1)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Normal(0,1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])
	#axes.get_xaxis().set_ticklabels([])

for i in range(len(N)):
	x = [ np.random.chisquare(1) for k in range(N[i]) ]
	if i == 0:
		axes = plt.subplot(3,5,i + len(N) + len(N) + 1)
		ax2 = axes
	else:
		axes = plt.subplot(3,5,i + len(N) + len(N) + 1, sharey = ax2, sharex = ax2)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Chi-Squared(1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])

fig.tight_layout()
plt.subplots_adjust(wspace=0.25,hspace=0.25)
plt.show()

#---------------------------------------------------------


fig, ax = plt.subplots(nrows=3, ncols=5,sharex=True,sharey=True,figsize=(15,9))
#fig.suptitle("Quasi-Random Sampling of Uniform, Normal, and Chi-Squared Distributions")
N = [1000, 5000, 10000, 20000, 50000]
nbins = 50
ax0 = None
ax1 = None
ax2 = None
for i in range(len(N)):
	dist = cp.Uniform(0,1)
	x = list( dist.sample(N[i], rule="S") )
	if i == 0:
		axes = plt.subplot(3,5,i + 1)
		ax0 = axes
	else:
		axes = plt.subplot(3,5,i + 1, sharey = ax0, sharex = ax0)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	axes.set_title('N=' + str(N[i]))
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Uniform(0,1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])
	#axes.get_xaxis().set_ticklabels([])

for i in range(len(N)):
	dist = cp.Normal(0,1)
	x = list( dist.sample(N[i], rule="S") )
	if i == 0:
		axes = plt.subplot(3,5,i + len(N) + 1)
		ax1 = axes
	else:
		axes = plt.subplot(3,5,i + len(N) + 1, sharey = ax1, sharex = ax1)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Normal(0,1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])
	#axes.get_xaxis().set_ticklabels([])

for i in range(len(N)):
	dist = cp.ChiSquared(1)
	x = list( dist.sample(N[i], rule="S") )
	if i == 0:
		axes = plt.subplot(3,5,i + len(N) + len(N) + 1)
		ax2 = axes
	else:
		axes = plt.subplot(3,5,i + len(N) + len(N) + 1, sharey = ax2, sharex = ax2)
	#plt.xlim(0.0,1.0)
	#plt.ylim(0.0,1.0)
	#axes.set_aspect('equal')
	plt.hist(x,density=1,bins=nbins)
	if i == 0:
		axes.set_ylabel('Chi-Squared(1)',rotation=90,size='large')
	#else:
	#	axes.get_yaxis().set_ticklabels([])

fig.tight_layout()
plt.subplots_adjust(wspace=0.25,hspace=0.25)
plt.show()