R = QQ[z1, z2, z3, w1, w2, w3];

A = ideal( z1, z2, z3 );

B = ideal( w1, w2, w3 );

A3 = A^3    -- For the cut at a = 3;

%%%%%%%%%%%%%%%%%

B1 = A0 * B

gens B1

numgens B1
