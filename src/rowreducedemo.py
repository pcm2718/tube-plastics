from rowreduce import RowReduce
from matrix import Matrix, NullMatrix, IdentityMatrix

rowreduce = RowReduce()
mat_a = Matrix(3, 3, [2, 1, -1, -3, -1, 2, -2, 1, 2])
vec_b = Matrix(3, 1, [8, -11, -3])

reduced_system = rowreduce.row_reduce(mat_a, vec_b)
vec_x = rowreduce.back_substitute(reduced_system['A'], reduced_system['b'])

print ""
print ""
print "Original System: Ax = b"
print ""
print "Test Matrix (A):"
print mat_a
print ""
print "Test Vector (b):"
print vec_b
print ""
print ""
print "Reduced System: A~x = b~"
print ""
print "A~ ="
print reduced_system['A']
print ""
print "b~ ="
print reduced_system['b']
print ""
print ""
print "Solution: x"
print ""
print "x ="
print vec_x
print ""
print ""
