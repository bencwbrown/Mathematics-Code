compactMatrixForm = false       -- "Nicer" matrix printing

R = QQ[z1, z2, z3, w1, w2, w3];
I = ideal( z1*w1, z2*w2, z3*w3 );

A = ideal( z1, z2, z3 );

B = ideal( w1, w2, w3 );

-- Useful commands: gens, numgens, basis

-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-- (k,a) = (3,0); => degree 4 in z's, degree 1 in w's;

A3 = A^3      -- Homogeneous degree 3 in the z's;

Cut3_0 = transpose( gens A3 )          -- Weight (k,a) = (3,0) for (K X S1)-action

No3_0 = numgens A3

-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-- (k,a) = (3,1); => degree 4 in z's, degree 1 in w's;

A4 = A^4;                              -- Homogeneous degree 4 in the z's

B4 = B^1;                              -- Homogeneous degree 1 in the w's

C4 = mingens ( (A4 * B4) / I );

Cut3_1 = transpose (gens image C4)     -- Weight (k,a) = (4,1) for (K X S1)-action

No3_1 = numgens( image C4 )

-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-- (k,a) = (3,2); => degree 5 in z's, degree 2 in w's;

A5 = A^5;                              -- Homogeneous degree 5 in the z's

B5 = B^2;                              -- Homogeneous degree 2 in the w's

C5 = mingens ( (A5 * B5) / I );        -- Weight (k,a) = (5,2) for (K X S1)-action

Cut3_2 = transpose (gens image C5)

No3_2 = numgens( image C5 )
