from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
import IPython.display as disp

N = CoordSys3D('N')

t = symbols( 't' )
m, n, d = symbols('m n d', positive=True, integer=True)
init_printing(use_latex='mathjax')

# Basis for the edge/weight vectors for the points 

v1 = N.i
v2 = N.j

# Define the vector which is not parallel to any edge vector, which generates a dense subgroup of the torus, and which we will let it tend to zero:

Xi = t*(2*v1 + 7*v2)

# Define the term which is summed over each fixed point, representing the character for the representation (NON-ORBIFOLD POINT!):

def P(P, edge1, edge2, edge3, edge4):
    return exp( Xi.dot(P) ) / ( (1 - exp( Xi.dot(edge1) ) ) * ( 1 - exp( Xi.dot(edge2) ) ) * ( 1 - exp( Xi.dot(edge3) ) ) * ( 1 - exp( Xi.dot(edge4) ) ) )

# Define the term which is summed over each fixed point, representing the character for the representation (ORBIFOLD POINT!):

def gExp(g, P):
    return exp( 2*pi*I*g.dot(P) )

def gOrbiSum(Q, q, g, edge1, edge2, edge3, edge4):
    return ( Rational(1,q) * exp( Xi.dot(Q) ) ) / ( (1 - ( gExp(g,edge1) * exp( Xi.dot(edge1) ) ) ) * (1 - ( gExp(g,edge2) * exp(Xi.dot(edge2) ) ) ) * (1 - ( gExp(g,edge3) * exp( Xi.dot(edge3) ) ) ) * (1 - ( gExp(g,edge4) * exp( Xi.dot(edge4) ) ) ) ) 