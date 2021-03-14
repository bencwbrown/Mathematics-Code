from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

Phi = t*(N.i + 2*N.j)

P23 = k*N.i
Q23 = (k+a)*N.i
Q13 = (k+a)*N.j
P13 = k*N.j

a23_1 = N.i
a23_2 = -N.i + N.j

b23_1 = -N.i + N.j
b23_2 = -N.i

b13_1 = -N.j
b13_2 = N.i - N.j 

a13_1 = N.i - N.j
a13_2 = N.j

def f(P, a1, a2):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(a1) ) ) * ( 1 - exp( Phi.dot(a2) ) ) )

T23 = f(P23, a23_1, a23_2)
S23 = f(Q23, b23_1, b23_2)
S13 = f(Q13, b13_1, b13_2)
T13 = f(P13, a13_1, a13_2)

Delta12 = T23 + S23 + S13 + T13

