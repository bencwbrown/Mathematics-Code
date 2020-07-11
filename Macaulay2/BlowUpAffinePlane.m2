

loadPackage Polyhedra
loadPackage "NormalToricVarieties"


matA = matrix "1, 1, -1"

A = image matA

L = ker matA

matL = gens L


I = transpose matA

PI = transpose matL

hilbertBasis(transpose matL, InputType => "lattice")





L = transpose matrix "-1,1,0,0; 1,0,1,-1"

hilbertBasis(L, InputType => "lattice")

L12 = matrix "-1,1,0,0,0; 1,0,1,-1,0; 3,0,2,0,1"

hilbertBasis(L12, InputType => "lattice")