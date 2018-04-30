import numpy as np
import matplotlib.pyplot as plt

def footprint(file_list, color_list=['b','m','g','r','c','y']):
	plt.figure()
	plt.title('Footprint')
	plt.xlabel('Qx')
	plt.ylabel('Qy')

	for item in file_list:
		dqx = []
		dqy = []
		f = open(file_list[item],'r')
		for line in f:
			t=line.split()
			dqx.append(float(t[0]))
			dqy.append(float(t[1]))
		
		plt.plot(dqx,dqy,color_list[item])
	plt.show()