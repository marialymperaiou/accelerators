import math

#accelerator data
E = 6500e9				#beam energy GeV
V = 10e6				#accelerator voltage MeV
h = 35000				#accelerator harmonic number

#physical data
E0 = 0.938e9			#proton rest energy GeV
#c = 2.997925e8			#speed of light
e_charge = 1 			#proton charge (important: put it in eV!!)
pi = 3.14159265359

gi = E/E0					#gamma value
print 'Gamma: ',gi
temp = 1/(math.pow(gi,2))
bi = math.sqrt(1 - temp)	#beta value
print 'Beta: ',bi

up = e_charge*V*h
down = 2*pi*(math.pow(bi,2))*E

g_tr = 39.73288916			#find GAMATR from MADX output
temp2 = 1/(math.pow(g_tr,2))
eta = abs(temp-temp2)		#find eta
print 'Eta: ', eta
#cos(phi) = 0 as we have no acceleration

Q = math.sqrt(up*eta/down)
print 'Synchrotron tune: ', Q
