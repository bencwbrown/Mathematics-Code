
from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

# Define the vector which is not parallel to any edge vector, which will tend to zero:

Phi = t*(N.i + 2*N.j + 3*N.k)

# Set the fixed points of the action; P denotes those that belong
# to the core, and Q those that come from the cut extended core:

P123 = Vector.zero
P234 = k*N.i
P134 = k*N.j
P124 = k*N.k

Q12_1 = -a*N.j
Q12_2 = -a*N.i

Q23_2 = (k+a)*N.i
Q23_3 = (k+a)*N.i - a*N.j

Q13_1 = (k+a)*N.j
Q13_3 = -a*N.i + (k+a)*N.j

# Basis for the edge/weight vectors for the points 

v1 = N.i
v2 = N.j

# Define the term which is summed over each fixed point,
# representing the character for the representation

def f(P, a1, a2):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(a1) ) ) * ( 1 - exp( Phi.dot(a2) ) ) )

# Each Tijk_lm is a summand for the polytope Delta_{ijk},
# at the fixed point P_{lm}

# For Delta_{123} (i.e. the core):

T123_12 = f(P12, v1, v2)
T123_23 = f(P23, -v1 + v2, -v1)
T123_13 = f(P13, -v2, v1 - v2)

Sum_123 = T123_12 + T123_23 + T123_13

# We take the limit of Sum_123 for t -> 0 to obtain the lattice point count in Delta_{123}:

limSum_123 = limit(Sum_123, t, 0)

# For Delta_{12}:

T12_23 = f(P23, v1, -v1 + v2)
S12_232 = f(Q23_2, -v1 + v2, -v1)
S12_131 = f(Q13_1, -v2, v1 - v2)
T12_13 = f(P13, v1 - v2, v2)

Sum_12 = T12_23 + S12_232 + S12_131 + T12_13

limSum_12 = limit(Sum_12, t, 0)

# For Delta_{13}:

T13_12 = f(P12, -v2, v1)
T13_23 = f(P23, -v1, v1 - v2) 
S13_121 = f(Q12_1, v1, v2)
S13_233 = f(Q23_3, -v1 + v2, -v1)

Sum_13 = T13_12 + T13_23 + S13_121 + S13_233

limSum_13 = limit(Sum_13, t, 0)             # This actual equals limSum_12

# For Delta_{1}:

T1_23 = f(P23, v1 - v2, v1)
S1_233 = f(Q23_3, v2, v2 - v1)
S1_232 = f(Q23_2, -v1, -v2)

Sum_1 = T1_23 + S1_233 + S1_232

limSum_1 = limit(Sum_1, t, 0)

# For the whole polyptych, ignoring the contribution from the
# overlapping boundaries between the components for now, 
# we have that the lattice point (over)count is:

limSumOverlap = (1 * limSum_123) + (3 * limSum_12) + (3 * limSum_1)

# In the above sum, we over count by ( 3*(k + 1) + 6*(a + 1) - 3 ),
# where the (k+1)-terms come from the walls of the interior core, and
# the (a+1)-terms come from the walls between the intersections of the 
# exterior parts of the extended core. The last (-3)-term then results
# by adding back in the interior fixed points, which lie in the intersections
# of four polytopes of the polypych:

limSumFinal = limSumOverlap - ( 3*(k+1) + 6*(a+1) - 3 )
