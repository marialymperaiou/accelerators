import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc
from naff_transformation import naff_transformation
#Change of tune with chromaticity increase

Qx = []
Qy = []

#take data from the lists
f = open('chromaticities.txt','r')
for line in f:
    chromaticity=line.split()
    Qx.append(float(chromaticity[0]))
    Qy.append(float(chromaticity[1]))

#print Qx
#print Qy

turns_x = []
turns_y = []
f2 = open('tunes.txt','r')
for line in f2:
    t=line.split()
    turns_x.append(float(t[0]))
    turns_y.append(float(t[1]))
#print turns_x
#print turns_y

plt.figure()
plt.plot(Qx[:10], turns_x[:10])
plt.title('Chromaticity vs tune on the x - plane')
plt.xlabel('Chromaticity')
plt.ylabel('Tunes')
plt.grid(True)
ax = plt.gca()
ax.ticklabel_format(useOffset=False)

plt.figure()
plt.plot(Qy[:10], turns_y[:10],'m')
plt.title('Chromaticity vs tune on the y - plane')
plt.xlabel('Chromaticity')
plt.ylabel('Tunes')
plt.grid(True)
ax = plt.gca()
ax.ticklabel_format(useOffset=False)

plt.show()
