o1 : Package

i2 : L = matrix "1,0,1,-1; 0,1,1,-1"

o2 = | 1 0 1 -1 |
     | 0 1 1 -1 |

              2        4
o2 : Matrix ZZ  <--- ZZ

i3 : transpose L

o3 = | 1  0  |
     | 0  1  |
     | 1  1  |
     | -1 -1 |

              4        2
o3 : Matrix ZZ  <--- ZZ

i4 : hilbertBasis(L, InputType => "lattice")

o4 = 0

              1
o4 : Matrix ZZ  <--- 0

i5 : LA = matrix "1,0,1,-1,0; 0,1,1,-1,0; 1,0,0,2,1"

o5 = | 1 0 1 -1 0 |
     | 0 1 1 -1 0 |
     | 1 0 0 2  1 |

              3        5
o5 : Matrix ZZ  <--- ZZ

i6 : hilbertBasis(LA, InputType => "lattice")

o6 = | 3 0 2 0 1 |
     | 0 3 2 0 1 |
     | 1 0 0 2 1 |
     | 2 0 1 1 1 |
     | 2 1 2 0 1 |
     | 0 1 0 2 1 |
     | 1 1 1 1 1 |
     | 1 2 2 0 1 |
     | 0 2 1 1 1 |

              9        5
o6 : Matrix ZZ  <--- ZZ

i7 :
