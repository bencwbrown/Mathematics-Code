
from sympy import *
from sympy.vector import Vector
from sympy.vector import CoordSys3D
N = CoordSys3D('N')

t, k, a = symbols( 't k a' )
init_printing(use_unicode=True)

# Define the vector which is not parallel to any edge vector, which will tend to zero:

Phi = t*(N.i + 2*N.j + 3*N.k)

# Basis vectors for convenience:

v1 = N.i

v2 = N.j

v3 = N.k

# Set the fixed points of the action; P denotes those that belong
# to the core, and Q those that come from the cut extended core:

def P123(k,a):
    return Vector.zero

def P234(k,a):
    return k*N.i

def P134(k,a):
    return k*N.j

def P124(k,a):
    return k*N.j

# ========================

# Considering one of the "large side" polytopes; i.e. Delta_ijk obtained from having only one G half-space

def Q123_12(k,a):
    return -a*N.k

def Q234_24(k,a):
    return (k+a)*N.i - a*N.k

def Q134_14(k,a):
    return (k+a)*N.j - a*N.k

def Q23_3(k,a):
    return (k+a)*N.i - a*N.j

def Q13_1(k,a):
    return (k+a)*N.j

def Q13_3(k,a):
    return -a*N.i + (k+a)*N.j

# Define the term which is summed over each fixed point,
# representing the character for the representation

def f(P, edge1, edge2, edge3):
    return exp( Phi.dot(P) ) / ( (1 - exp( Phi.dot(edge1) ) ) * ( 1 - exp( Phi.dot(edge2) ) ) * ( 1 - exp( Phi.dot(edge3) ) ) )

# Define the n-th Verlinde sum, to use when checking the validity of the calculations:

def Ver2(k):
    return (k+1)*(k+2)/2

def Ver3(k):
    return (k+1)*(k+2)*(k+3)/6

# Each Tijk_lm is a summand for the polytope Delta_{ijk},
# at the fixed point P_{lm}

# For Delta_{124}:

def T124_123(k,a):
    return f(P123(k,a), v1, -v3, v2)

def T124_234(k,a):
    return f(P234(k,a), v1 - v3, -v1, -v1 + v2)

def T124_134(k,a):
    return f(P134(k,a), v2 - v3, v1 - v2, -v2)

def S124_123(k,a):
    return f(Q123_12(k,a), v1, v2, v3)

def S124_234(k,a):
    return f(Q234_24(k,a), -v1 + v2, -v1, -v1 + v3)

def S124_134(k,a):
    return f(Q134_14(k,a), -v2, v1 - v2, -v2 + v3)

def Sum_124(k,a):
    return T124_123(k,a) + T124_234(k,a) + T124_134(k,a) + S124_123(k,a) + S124_234(k,a) + S124_134(k,a)

# We take the limit of Sum_124 for t -> 0 to obtain the lattice point count in Delta_{124}:

def limSum_124(k,a):
    return limit(Sum_124(k,a), t, 0)

# TO-DO: Finish from here plus double-check all comments in case out of date

# Now consider the polytope Delta_{12}, which is one of the longer, bevelled-eqsue polytopes:

# Define the additional fixed-points:

def Q234_23(k,a):
    return (k+a)*N.i

def Q134_13(k,a):
    return (k+a)*N.j

# Then the terms involved in the sum:

def T12_234(k,a):
    return f(P234(k,a), v1, v1 - v3, -v1 + v2)

def T12_134(k,a):
    return f(P134(k,a), v1 - v2, v2 - v3, v2)

def S12_24(k,a):
    return f(Q234_24(k,a), -v1 + v2, -v1 + v3, v3)

def S12_23(k,a):
    return f(Q234_23(k,a), -v1, -v1 + v2, -v3)

def S12_13(k,a):
    return f(Q134_13(k,a), v1 - v2, -v2, -v3)

def S12_14(k,a):
    return f(Q134_14(k,a), v3, -v2 + v3, v1 - v2)

# Sum the terms:

def Sum_12(k,a):
    return T12_234(k,a) + T12_134(k,a) + S12_24(k,a) + S12_23(k,a) + S12_13(k,a) + S12_14(k,a)

# Then take the limit as t -> 0:

def limSum_12(k,a):
    return limit(Sum_12(k,a), t, 0)

# Finally, consider polytope Delta_{1}, i.e. one of the "end caps":

def Q234_24(k,a):
    return (k+a)*N.i - a*N.k

def Q234_34(k,a):
    return (k+a)*N.i - a*N.j

# Then define the terms of the sum:

def T1_234(k,a):
    return f(P234(k,a), v1, v1 - v2, v1 - v3)

def S1_23(k,a):
    return f(Q234_23(k,a), -v1, -v3, -v2)

def S1_24(k,a):
    return f(Q234_24(k,a), -v1 + v3, -v2 + v3, v3)

def S1_34(k,a):
    return f(Q234_34(k,a), -v1 + v2, v2, v2 - v3)

# And the sum itself for Delta_{1}:

def Sum_1(k,a):
    return T1_234(k,a) + S1_23(k,a) + S1_24(k,a) + S1_34(k,a)

# Take the limit for t -> 0:

def limSum_1(k,a):
    return limit(Sum_1(k,a), t, 0)

# Finally, we also know the number of lattice points in the core, Delta_{1234}:

def limSum_1234(k,a):
    return k**3/6 + k**2 + 11*k/6 + 1

# ORIGINAL THEN DID NOT COUNT OVERLAP - NEED OVERLAP FOR MULTIPLICITY TWO WEIGHTS? 
# I.E. ON OVERLAP?

def limSumOverlap(k,a):
    return (1 * limSum_1234(k,a)) + (4 * limSum_124(k,a)) + (6 * limSum_12(k,a)) + (4*limSum_1(k,a))

# =========================
# 29-05-2020: Final number of lattice points with overlaps taken into account should be a sum involving the following:

def final_1234(k,a):
    return ( ( ( k**3 + 6*k**2 + 11*k) / 6 ) + 1 )

def final_123(k,a):
    return ( (a**2 + a*(3*k + 6) + (3*k**2 + 12*k + 11) ) * a / 6 )

def final_12(k,a):
    return ( (2*a**2 + 3*a*(k+1) - 3*k - 5) * a / 6  )

def final_1(k,a):
    return ( (a**2 - 3*a + 2) * a / 6 )

# ========================

def finalTotal(k,a):
    return 1*final_1234(k,a) + 4*final_123(k,a) + 6*final_12(k,a) + 4*final_1(k,a)

# =========================
# Define functions for the equivariant Verlinde formula for SU(2) for a Riemann surface of g = 2
# from Gukov et al., 2018:

def eqVer_1(k,a):
    return 4 / ((1 - a**2)**3)

def eqVer_2(k,a):
    return ( (2 * (5*a**2 + 6*a + 5)) / (1 - a**2)**3 )

def eqVer_3(k,a):
    return ( (4 * ( 4*a**3 + 9*a**2 + 9*a + 5 )) / (1 - a**2)**3 )

def eqVer_4(k,a):
    return ( (4 * ( 16*a**4 + 49*a**3 + 81*a**2 + 75*a + 35 )) / (1 - a**2)**3 )

