

loadPackage Polyhedra
loadPackage "NormalToricVarieties"




matWR = matrix "0,0; 1, 1"

WR = image matWR

LR = ker matWR

matLR = gens LR

hilbertBasis(transpose matL, InputType => "lattice")


LRpos = matrix "1,-1,0; 1,0,1"

hilbertBasis(transpose LRpos, InputType => "lattice")

------------

matWS = matrix "0; 1"

WS = image matWS

LS = ker matWS

matLS = gens LS

hilbertBasis(transpose matLS, InputType => "lattice")


LRpos = matrix "1,-1,0; 1,0,1"

hilbertBasis(transpose LRpos, InputType => "lattice")

