from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

Phi = t*(N.i + 2*N.j)

P12 = Vector.zero
P23 = k*N.i
P13 = k*N.j

a12_1 = N.i
a12_2 = N.j

a23_1 = -N.i + N.j
a23_2 = -N.i 

a13_1 = -N.j
a13_2 = N.i - N.j

def f(P, a1, a2):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(a1) ) ) * ( 1 - exp( Phi.dot(a2) ) ) )

# T1 = exp(0) / ( (1 - exp(t)) * (1 - exp(2*t)) )
# T2 = exp(k*t) / ( (1 - exp(t)) * (1 - exp(-t)) )
# T3 = exp(2*k*t) / ( (1 - exp(-2*t)) * (1 - exp(-t)) )

T1 = f(P12, a12_1, a12_2)
T2 = f(P23, a23_1, a23_2)
T3 = f(P13, a13_1, a13_2)

Delta123 = T1 + T2 + T3

n123 = limit(Delta123, t, 0)