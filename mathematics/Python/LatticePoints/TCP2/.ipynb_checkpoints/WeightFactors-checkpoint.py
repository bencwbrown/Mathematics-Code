
from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

# Define the vector which is not parallel to any edge vector, which will tend to zero:

Phi = t*(N.i + 2*N.j)

# Set the fixed points of the action; P denotes those that belong
# to the core, and Q those that come from the cut extended core:

def P12(k,a):
    return Vector.zero

def P23(k,a):
    return k*N.i

def P13(k,a):
    return k*N.j

def Q12_1(k,a):
    return -a*N.j

def Q12_2(k,a):
    return -a*N.i

def Q23_2(k,a):
    return (k+a)*N.i

def Q23_3(k,a):
    return (k+a)*N.i - a*N.j

def Q13_1(k,a):
    return (k+a)*N.j

def Q13_3(k,a):
    return -a*N.i + (k+a)*N.j

# Basis for the edge/weight vectors for the points 

v1 = N.i

v2 = N.j

# Define the term which is summed over each fixed point,
# representing the character for the representation

def f(P, edge1, edge2):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(edge1) ) ) * ( 1 - exp( Phi.dot(edge2) ) ) )

def g(P, edge1, edge2, edge3, edge4):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(edge1) ) ) * ( 1 - exp( Phi.dot(edge2) ) ) * ( 1 - exp( Phi.dot(edge3) ) ) * ( 1 - exp( Phi.dot(edge4) ) ) )

# For each of the right-angled triangles:

def Delta1(k,a):
    return f(P23(k,a), -v1, -v1 + v2 ) * ( f(0*v1 + 0*v2, v1, v1 - v2) + f(a*v1, -v1, -v2) + f(a*v1 - a*v2, v2, -v1 + v2) )

def Delta2(k,a):
    return f(P13(k,a), v1 - v2, -v2 ) * ( f(0*v1 + 0*v2, v2, -v1 + v2) + f(a*v2, -v1, -v2) + f(-a*v1 + a*v2, v1, v1 - v2) )

def Delta3(k,a):
    return f(P12(k,a), v1 , v2 ) * ( f(0*v1 + 0*v2, -v1, -v2) + f(-a*v1, v1, v1 - v2) + f(-a*v2, v2, -v1 + v2) )


def Sum(k,a):
    return Delta1(k,a) + Delta2(k,a) + Delta3(k,a) 

# Take the limit as t -> 0 to get the Euler characteristic(?)

def Euler(k,a):
    return limit(Sum(k,a),t,0)


# OLD
#
#
#
#
#
#
#
#
# Each Tijk_lm is a summand for the polytope Delta_{ijk},
# at the fixed point P_{lm}

# For Delta_{123} (i.e. the core):

def T123_12(k,a):
    return f(P12(k,a), v1, v2)

def T123_23(k,a):
    return f(P23(k,a), -v1 + v2, -v1)

def T123_13(k,a):
    return f(P13(k,a), -v2, v1 - v2)

def Sum_123(k,a):
    return T123_12(k,a) + T123_23(k,a) + T123_13(k,a)

# We take the limit of Sum_123 for t -> 0 to obtain the lattice point count in Delta_{123}:

def limSum_123(k,a):
    return limit(Sum_123(k,a), t, 0)

# For Delta_{12} (and other two index sub-polytopes):

def T12_23(k,a):
    return f(P23(k,a), v1, -v1 + v2)

def S12_232(k,a):
    return f(Q23_2(k,a), -v1 + v2, -v1)

def S12_131(k,a):
    return f(Q13_1(k,a), -v2, v1 - v2)

def T12_13(k,a):
    return f(P13(k,a), v1 - v2, v2)

def Sum_12(k,a):
    return T12_23(k,a) + S12_232(k,a) + S12_131(k,a) + T12_13(k,a)

def limSum_12(k,a):
    return limit(Sum_12(k,a), t, 0)

# For Delta_{1} (and other single index sub-polytopes):

def T1_23(k,a):
    return f(P23(k,a), v1 - v2, v1)

def S1_233(k,a):
    return f(Q23_3(k,a), v2, v2 - v1)

def S1_232(k,a):
    return f(Q23_2(k,a), -v1, -v2)

def Sum_1(k,a):
    return T1_23(k,a) + S1_233(k,a) + S1_232(k,a)

def limSum_1(k,a):
    return limit(Sum_1(k,a), t, 0)

# --- IGNORE THIS SECTION

# For the whole polyptych, ignoring the contribution from the
# overlapping boundaries between the components for now, 
# we have that the lattice point (over)count is:

#def limSumOverlap(k,a):
#    return (1 * limSum_123(k,a)) + (3 * limSum_12(k,a)) + (3 * limSum_1(k,a))

# In the above sum, we over count by ( 3*(k + 1) + 6*(a + 1) - 3 ),
# where the (k+1)-terms come from the walls of the interior core, and
# the (a+1)-terms come from the walls between the intersections of the 
# exterior parts of the extended core. The last (-3)-term then results
# by adding back in the interior fixed points, which lie in the intersections
# of four polytopes of the polypych:

#def limSumFinal(k,a):
#    return limSumOverlap(k,a) - ( 3*(k+1) + 6*(a+1) - 3 )

# --- END OF IGNORE

def limSumOverlap(k,a):
    return (1 * limSum_123(k,a)) + (3 * limSum_12(k,a)) + (3 * limSum_1(k,a))
