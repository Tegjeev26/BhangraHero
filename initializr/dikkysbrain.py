import math

def distance(p1, p2):
	(x1, y1, z1, t1) = p1
	(x2, y2, z2, t2) = p2
	dx = (x1-x2)**2
	dy = (y1-y2)**2
	dz = (z1-z2)**2
	return math.sqrt(dx, dy, dz)

def pvector(p1, p2):
	(x1, y1, z1, t1) = p1
	(x2, y2, z2, t2) = p2
	return (x2-x1, y2-y1, z2-z1)

def derivative(v1, v2, t):
	(x1, y1, z1) = v1
	(x2, y2, z2) = v2
	return ((x2-x1)/t, (y2-y1)/t, (z2-z1)/t)

def dot(v1, v2):
	(x1, y1, z1) = v1
	(x2, y2, z2) = v2
	return (x1*x2 + y1*y2 + z1*z2)

def cross(v1, v2):
	(x1, y1, z1) = v1
	(x2, y2, z2) = v2
	i = y1*z2 - y2*z1
	j = -(x1*z2 - x2*z1)
	k = x1*y2 - x2*y1
	return (i, j, k)

def magnitude(v):
	(x1, y1, z1) = v
	return math.sqrt(x1**2 + y1**2 = z1**2)

def normalize(v):
	(x1, y1, z1) = v
	m = magnitude(v)
	return (x1/m, y1/m, z1/m)




