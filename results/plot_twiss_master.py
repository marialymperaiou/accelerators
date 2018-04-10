import numpy as np
import matplotlib.pyplot as plt
import metaclass as mtc

fname_twiss = 'twiss_master.out'
ob = mtc.twiss(fname_twiss)

plt.close('all')
plt.figure(figsize=(8,7))

sp1 = plt.subplot(3,1,1)
sp1.plot(ob.S, ob.DX, 'teal', label='DX')
sp1.plot(ob.S, ob.DY, 'purple', label='DY')
plt.title('Dispersion')
plt.xlabel('s')
plt.ylabel('D')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=-0.5)

sp2 = plt.subplot(3,1,2, sharex=sp1)
sp2.plot(ob.S, ob.BETX, 'teal', label='BX')
sp2.plot(ob.S, ob.BETY, 'purple', label='BY')
plt.title('Beta function')
plt.xlabel('s')
plt.ylabel(r'$\beta$')
plt.grid(True)

plt.subplots_adjust(top=0.9, bottom=-0.3, right = 0.85, hspace=0.5, wspace=0.95)
plt.legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=-0.5)


plt.show()
