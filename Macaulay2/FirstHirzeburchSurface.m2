loadPackage Polyhedra
loadPackage "NormalToricVarieties"

A = matrix "1,1,-1,0; 0,0,1,1"
L = transpose matrix "-1,1,0,0; 1,0,1,-1"

hilbertBasis(L, InputType => "lattice")

L12 = matrix "-1,1,0,0,0; 1,0,1,-1,0; 3,0,2,0,1"

hilbertBasis(L12, InputType => "lattice")











L = matrix "-1,1,0,0; 1,0,1,-1"

transpose L

hilbertBasis(L, InputType => "lattice")

L11 = matrix "-1,1,0,0,0; 1,0,1,-1,0; 1,0,0,1,1"

hilbertBasis(L11, InputType => "lattice")


# Should get CP2, with trivial cut:

B = matrix "1,1,1,0; 0,0,0,1"

M = gens ker B

hilbertBasis(transpose M, InputType => "lattice")

######### a = (1,1)

M11 = matrix "-1,1,0,0,0; -1,0,1,0,0; 1,0,0,1,1"

hilbertBasis(M11, InputType => "lattice")

######### a = (1,10)

M110 = matrix "-1,1,0,0,0; -1,0,1,0,0; 1,0,0,10,1"

hilbertBasis(M110, InputType => "lattice")




