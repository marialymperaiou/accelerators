import numpy as np
import math
from lum import *

xsect = 81e-31 							# m^2 (inelastic x-sect)
N1 = N2 = 1.25e11						# bunch particles
xing = 150e-6							# half crossing angle phi/2
blength = 0.082 						# (m) bunch length
n_em = 2.50e-6 							# (um) normalized emittance
frev = 11245.5 							# revolution frequency (Hz)
bx = by = 0.30 							# (m) betas
nb = 2556								# number of bunches
hours = 20								# calculate luminosity decay for some time
m_tot = 52								# maximum events

# Calculate luminosity
L_tot = luminosity(N1, N2, n_em, frev, bx, nb, xing, blength)
print 'Luminosity:', L_tot

# Find luminosity evolution over time
Lum, N_part = decay_rate(xsect, N1, N2, n_em, frev, bx, nb, xing, blength, hours, m_tot, pl = True)






