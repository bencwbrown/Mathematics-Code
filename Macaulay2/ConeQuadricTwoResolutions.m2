loadPackage Polyhedra

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
