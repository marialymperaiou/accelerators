import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc

#plots the geometry of the ring, taking data from survey.cas file
fname_twiss = 'survey_master.cas'
ob = mtc.twiss(fname_twiss)

plt.close('all')
plt.figure(figsize=(7,8))

sp1 = plt.subplot(2,1,1)
sp1.plot(ob.X, ob.Z, 'teal')
plt.title('Geometry')
plt.xlabel('Z')
plt.ylabel('X')
plt.grid(True)

sp2 = plt.subplot(2,1,2, sharex=sp1)
sp2.plot(ob.Y, ob.Z, 'teal')
plt.title('Geometry')
plt.xlabel('Z')
plt.ylabel('Y')
plt.grid(True)

plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0.35, wspace=0.35)
#check always for the ring to be closed!

plt.show()



