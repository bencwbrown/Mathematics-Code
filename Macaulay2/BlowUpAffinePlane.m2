blowUpIdeal = (I) -> ( r := numgens I;
S := ring I;
n := numgens S;
K := coefficientRing S;
tR := K[t, gens S, vars(0..r-1),
MonomialOrder => Eliminate 1];
f := map(tR, S, submatrix(vars tR, {1..n}));
F := f(gens I);
J := ideal apply(1..r, j -> (gens tR)_(n+j)-t*F_(0,(j-1))); L := ideal selectInSubring(1, gens gb J);
R := K[gens S, vars(0..r-1)];
g := map(R, tR, 0 | vars R);
trim g(L));