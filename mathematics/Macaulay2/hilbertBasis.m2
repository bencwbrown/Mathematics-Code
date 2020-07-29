loadPackage Polyhedra

-- Example 8.5 from Miller & Sturmfels, page 151

M = matrix "1,1,1,0; 1,3,5,0; 5,2,3,1"

H = hilbertBasis(M, InputType => "lattice")

-- i5 : hilbertBasis(M, InputType => "lattice")

-- o5 = | 1 1 1 0 |
--     | 0 0 8 2 |
--     | 3 0 1 1 |
--     | 8 0 0 2 |
--     | 6 1 0 1 |
--     | 4 2 0 0 |
--     | 0 1 6 1 |
--     | 1 0 3 1 |
--     | 0 2 4 0 |

--              9        4
-- o5 : Matrix ZZ  <--- ZZ

N = matrix "1,0,1,-1,0; 1,1,0,-1,0; 1,0,0,2,1"


-- Example on Atiyah Flop in Miller & Sturmfels,

L = matrix "1,-1,0,0; 1,0,1,0; 1,0,0,1"

A = ker L

-- Hilbert basis for degree-0 part of coordinate ring

H = hilbertBasis(L, InputType => "lattice")

-- Lattice and Hilbert basis for degree +1 part

L1 = matrix "1,-1,0,0,0; 1,0,1,0,0; 1,0,0,1,0; 1,0,0,0,1"
H1 = hilbertBasis(L1, InputType => "lattice")

-- -- Lattice and Hilbert basis for degree -1 part

L2 = matrix "1,-1,0,0,0; 1,0,1,0,0; 1,0,0,1,0; 0,0,-1,0,-1"
H2 = hilbertBasis(L2, InputType => "lattice")
