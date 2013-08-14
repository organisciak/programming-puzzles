#from math import pi
import numpy as np

def main():
	N = 10

	num_cells = (N+1) * (N+1)

	xcoords = [-1] + [()] * N + [1]
	# Don't use a y grid, since presumably the rectangles will be the same
	#ycoords = xcoords

	xcoords = [-1, -0.5, 0.5, 1]
	sum_area(xcoords, xcoords)

def overlap():
	pass

def sum_area(xcoords, ycoords):
	# Convert 1d coords to the distances between points
	hlines = [x2-x1 for x2, x1 in zip(xcoords[1:], xcoords[:-1])]
	vlines = [y2-y1 for y2, y1 in zip(ycoords[1:], ycoords[:-1])]
	
	# (W, H) tuples
	cells = [[(w, h) for h in hlines] for w in vlines]

	# Sum area of remaining cells
	s = sum([h*w for w, h in row for row in cells])
	
	return s



def points_on_circle(radius=1, coords=(0,0), granularity=0.1):
	#Values from 0 to 2pi
	a = np.arange(0, 2*np.pi, granularity)

	
if __name__=='__main__':
	main()

# Circle
# center = (0, 0)
# radius = 1


