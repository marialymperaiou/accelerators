import numpy as np 
import math

########### INPUT ###########
#Design of the machine#

arc_number = 8															#number of arcs in the ring
arc_cells = 28															#number of cells per arc
straight_sections = 8													#number of straight sections in the ring
straight_cells = 4														#number of cells per straight section
total_cells = (arc_number*arc_cells)+(straight_sections*straight_cells)	#total number of cells in the ring
print 'total number of cells in the ring = '
print total_cells
print '\n'

cell_length = 100
circumference = total_cells*cell_length
print 'circumference = '
print circumference
print '\n'
m = 60.1																#phase advance per cell. Choose close to 60, but not exactly 60! (otherwise resonances...)	
tune = (m*total_cells)/360
cell_dipoles = 	2														#number of dipoles per cell
no_dipoles = (straight_cells + 2)*straight_sections*cell_dipoles		#number of cells with no dipoles
total_dipoles = (total_cells*cell_dipoles) - no_dipoles					#number of dipoles in the ring

#sextupole strength
ksf =3.17441e-04
ksd =-4.07306e-04

#tune
Qpx = 43.0
Qpy = 43.0
frac_q_x = 0.11 														#Give slightly different fractional numbers to avoid coupling
frac_q_y = 0.21
Qx_total = Qpx+frac_q_x
Qy_total = Qpy+frac_q_y

#number of turns for tracking
TURNS=1000

#Define chromaticities. Usual values are up to 40 (maximum!)
Qx = []
Qy = []
f = open('chromaticities.txt','r')
for line in f:
    chromaticity=line.split()
    Qx.append(float(chromaticity[0]))
    Qy.append(float(chromaticity[1]))
DQ1 = Qx[0]															#give values from 0-9. These correspond to chromaticities = 0,1,5,10,15,20,25,30,35,40.
DQ2 = Qy[0]									

#Define dipoles, quadrupoles and sextupoles as multipoles
elements = """
MBS:multipole, knl:={d_angle};
qfType:multipole, knl:={0,kf};
qdType:multipole, knl:={0,kd};
sfType:multipole, knl:={0,0,ksf};
sdType:multipole, knl:={0,0,ksd};
CAV: RFCAVITY, L := 0.;

"""

fodo = """
fodo:SEQUENCE, REFER=entry, L=circumference; 

"""

con = """
beam, particle=proton, sequence=fodo, energy=6500;
use, sequence=fodo;
"""

matching_begin= """
match, sequence = fodo; 
"""

matching_end = """
vary, name = kf, step=0.00001;
vary, name = kd, step=0.00001;
vary, name = ksf, step=0.00001;
vary, name = ksd, step=0.00001;
lmdif, calls=50, tolerance=1e-6;		//method adopted
ENDMATCH;
"""

twiss = """
twiss,save,centre,file=twiss_master.out;
"""

plots = """
survey,file=survey_master.cas;
"""

#Tracking here!
track = """

start, x= 2e-3, px=0, y= 2e-3, py=0, t= 0, pt = 1e-6;            
start, x= 3e-3, px=0, y= 3e-3, py=0, t= 0, pt = 3e-5;            
start, x= 4e-3, px=0, y= 4e-3, py=0, t= 0, pt = 6e-5;            
start, x= 5e-3, px=0, y= 5e-3, py=0, t= 0, pt = 8e-5;           
start, x= 6e-3, px=0, y= 6e-3, py=0, t= 0, pt = 1e-4;           
start, x= 7e-3, px=0, y= 7e-3, py=0, t= 0, pt = 1.3e-4;           
start, x= 8e-3, px=0, y= 8e-3, py=0, t= 0, pt = 1.6e-4;        
start, x= 9e-3, px=0, y= 9e-3, py=0, t= 0, pt = 1.8e-4;           
start, x= 10e-3, px=0, y= 10e-3, py=0, t= 0, pt = 2.1e-4;           
start, x= 11e-3, px=0, y= 11e-3, py=0, t= 0, pt = 3e-4; 

"""

#Generate MADX file
fname = 'madx_master_lattice.txt'
#WRITE IN MADX FILE
with open(fname, 'w') as fid:
	fid.write('arc_number = %f;\n'%(float(arc_number)))
	fid.write('arc_cells = %d;\n'%(int(arc_cells)))
	fid.write('straight_sections = %f;\n'%(float(straight_sections)))
	fid.write('straight_cells = %d;\n'%(int(straight_cells)))
	fid.write('total_cells = (arc_number*arc_cells)+(straight_sections*straight_cells);\n')
	fid.write('cell_length = %f;\n'%(float(cell_length)))
	fid.write('circumference = total_cells*cell_length;\n')
	fid.write('\n')
	fid.write('m = %f;\n'%(float(m)))
	fid.write('tune = %f;\n'%(float(tune)))
	fid.write('cell_dipoles = %f;\n'%(float(cell_dipoles)))
	fid.write('no_dipoles = %f;\n'%(float(no_dipoles)))
	fid.write('total_dipoles = %f;\n'%(float(total_dipoles)))
	fid.write('d_angle := 2*pi/total_dipoles;\n')
	fid.write('\n')
	fid.write('kf := (4*sin(m/2))/cell_length;\n')
	fid.write('kd := -(4*sin(m/2))/cell_length;\n')
	fid.write('\n')
	fid.write('ksf := %f;\n'%(float(ksf)))
	fid.write('ksd := %f;\n'%(float(ksd)))
	fid.write(elements)
	fid.write(fodo)

	#build lattice
	loc=0.0 										#position of the 1st element
	dip=1											#dipole counter
	drift = float(cell_dipoles + 2)*total_cells		#number of drift spaces
	print 'Number of drift spaces = '
	print drift
	print '\n'
	space = float(circumference/drift)
	print 'space = '
	print space
	print '\n'
	full_cells = abs((arc_cells*arc_number/straight_sections)-4)							#full cells in a row
	print 'full cells in a row = '
	print full_cells
	print '\n'
	half_dipoles = (cell_dipoles/2)
	straight_drift = float(half_dipoles+1)			#in straight sections space between F and D is different due to the missing dipoles. N dipoles result in N+1 drifts
	print 'straight drifts = '
	print straight_drift
	print '\n'
	fid.write('CAV1:CAV, at=0.;\n')
	offset = 1

	#lattice begins in the middle of a straight section
	
	for jj in xrange (straight_sections):
	########################################################################################################################################
		print 'Last half straight section'
		print '\n'
		for rr in xrange (straight_cells/2):
			fid.write('/*cell%d*/\n'%(int(rr+offset)))

			#focus
			fid.write('qf%d:qfType, at=%f;\n'%(int(rr+offset), float(loc)))

			#defocus
			loc=loc+(straight_drift*space)
			fid.write('qd%d:qdType, at=%f;\n'%(int(rr+offset), float(loc)))

			loc=loc+(straight_drift*space)
			fid.write('\n')

		offset = offset+rr+1
		print 'offset rr = %d= '%int(rr)
		print offset
		print '\n'

	########################################################################################################################################
	######## Dispersion suppressor ########
		print 'Begin dispersion suppressor'
		print '\n'
		fid.write('/*cell%d*/\n'%(int(offset)))

		#focus
		fid.write('qf%d:qfType, at=%f;\n'%(int(offset), float(loc)))

		for kk in xrange (int(half_dipoles)):
		#bend
			loc=loc+space
			fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
			dip=dip+1

		#defocus
		loc=loc+space
		fid.write('qd%d:qdType, at=%f;\n'%(int(offset), float(loc)))

		for kk in xrange (int(half_dipoles)):
		#bend
			loc=loc+space
			fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
			dip=dip+1

		loc=loc+space
		fid.write('\n')

	###############################################################

		offset = offset+1 
		print 'offset kk = %d= '%int(kk)
		print offset
		print '\n'

		fid.write('/*cell%d*/\n'%(int(offset)))

		#focus
		fid.write('qf%d:qfType, at=%f;\n'%(int(offset), float(loc)))

		#defocus
		loc=loc+(straight_drift*space)
		fid.write('qd%d:qdType, at=%f;\n'%(int(offset), float(loc)))

		loc=loc+(straight_drift*space)
		offset = offset+1 
		fid.write('\n')
		print 'End dispersion suppressor'
		print '\n'
	######## End of dispersion suppressor ########
	########################################################################################################################################

		for ii in xrange(int(full_cells)):
			fid.write('/*cell%d*/\n'%(int(ii+offset)))

			#focus
			fid.write('qf%d:qfType, at=%f;\n'%(int(ii+offset), float(loc)))

			#add sextupole next to quadrupole
			fid.write('sf%d:sfType, at=%f;\n'%(int(ii+offset), float(loc))) 

			for kk in xrange (int(half_dipoles)):
			#bend
				loc=loc+space
				fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
				dip=dip+1

			#defocus
			loc=loc+space
			fid.write('qd%d:qdType, at=%f;\n'%(int(ii+offset), float(loc)))
			#add sextupole next to quadrupole
			fid.write('sd%d:sdType, at=%f;\n'%(int(ii+offset), float(loc)))

			for kk in xrange (int(half_dipoles)):
			#bend
				loc=loc+space
				fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
				dip=dip+1

			loc=loc+space
			fid.write('\n')

		print 'offset jj = %d ii = %d= '%(int(jj),int(ii))
		print offset
		print '\n'

		########################################################################################################################################
		######## Dispersion suppressor ########
		print 'Begin dispersion suppressor'
		print '\n'
		offset = offset+ii+1 
		print 'offset jj = %d ii = %d= '%(int(jj),int(ii))
		print offset
		print '\n'
		fid.write('/*cell%d*/\n'%(int(offset)))
		
		#focus
		fid.write('qf%d:qfType, at=%f;\n'%(int(offset), float(loc)))

		#defocus
		loc=loc+(straight_drift*space)
		fid.write('qd%d:qdType, at=%f;\n'%(int(offset), float(loc)))

		loc=loc+(straight_drift*space)
		fid.write('\n')
		###############################################################
		offset = offset+1 
		print 'offset jj = %d ii = %d= '%(int(jj),int(ii))
		print offset
		print '\n'
		fid.write('/*cell%d*/\n'%(int(offset)))

		#focus
		fid.write('qf%d:qfType, at=%f;\n'%(int(offset), float(loc)))

		for kk in xrange (int(half_dipoles)):
		#bend
			loc=loc+space
			fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
			dip=dip+1

		#defocus
		loc=loc+space
		fid.write('qd%d:qdType, at=%f;\n'%(int(offset), float(loc)))

		for kk in xrange (int(half_dipoles)):
		#bend
			loc=loc+space
			fid.write('DIP%d:MBS, at=%f;\n'%(int(dip), float(loc)))
			dip=dip+1

		loc=loc+space
		fid.write('\n')
		print 'End dispersion suppressor'
		print '\n'
		######## End of dispersion suppressor ########
		########################################################################################################################################
		print 'Begin half straight section '
		print '\n'
		#first half of the drift space
		offset = offset+1
		print 'offset jj = %d ii = %d= '%(int(jj),int(ii))
		print offset
		print '\n'
		for rr in xrange(straight_cells/2):
			fid.write('/*cell%d*/\n'%(int(rr+offset)))

			#focus
			fid.write('qf%d:qfType, at=%f;\n'%(int(rr+offset), float(loc)))

			#defocus
			loc=loc+(straight_drift*space)
			fid.write('qd%d:qdType, at=%f;\n'%(int(rr+offset), float(loc)))

			loc=loc+(straight_drift*space)
			fid.write('\n')

		offset = offset+rr+1
		print 'offset rr = %d= '%int(rr)
		print offset
		print '\n'

		########################################################################################################################################

	fid.write('ENDSEQUENCE;\n')
	#Set RF cavities
	fid.write('CAV1, volt=0.1, lag=0.5, harmon=35000;\n')
	fid.write(con)
	fid.write(matching_begin)
	fid.write('global, sequence = fodo, DQ1 =%f;\n'%(float(DQ1)))
	fid.write('global, sequence = fodo, DQ2 =%f;\n'%(float(DQ2)))
	fid.write('global, sequence = fodo, Q1 =%f;\n'%(float(Qx_total)))
	fid.write('global, sequence = fodo, Q2 =%f;'%(float(Qy_total)))
	fid.write(matching_end)

	fid.write(plots)
	fid.write(twiss)

	#change voltage!
	fid.write('CAV1, volt=10, lag=0.5, harmon=35000;\n')
	
	#tracking
	fid.write('track,file=track_master%d.out,dump;'%(DQ1))
	fid.write(track)
	fid.write('run,turns=%d;\n'%(TURNS))
	fid.write('endtrack;\n')
	fid.write('stop;\n')