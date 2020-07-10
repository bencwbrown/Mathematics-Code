
loadPackage Polyhedra
loadPackage "NormalToricVarieties"

L = matrix "1,0;0,1"

transpose L

hilbertBasis(L, InputType => "lattice")

L11 = matrix "-1,1,0,0,0; 1,0,1,-1,0; 1,0,0,1,1"

hilbertBasis(L11, InputType => "lattice")
