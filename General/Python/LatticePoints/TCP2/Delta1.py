from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

Phi = t*(N.i + 2*N.j)

P23 = k*N.i
P23_2 = (k+a)*N.i - a*N.j
P23_3 = (k+a)*N.i

a23_1 = N.i - N.j
a23_2 = N.i

b2_1 = N.j
b2_2 = -N.i + N.j

b3_1 = -N.i
b3_2 = -N.j

def f(P, a1, a2):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(a1) ) ) * ( 1 - exp( Phi.dot(a2) ) ) )

T1 = f(P23, a23_1, a23_2)
T2 = f(P23_2, b2_1, b2_2)
T3 = f(P23_3, b3_1, b3_2)

Delta1 = T1 + T2 + T3

n1 = limit(Delta1, t, 0)