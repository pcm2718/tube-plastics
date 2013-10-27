from matrix import Matrix, NullMatrix, IdentityMatrix
from cholesky import Cholesky

print ""
print ""
print "Welcome to the Tube Alloys restricted linear algebra package. This software requires the Python 2.7"
print "interpreter. This software has not been tested with any other version of Python, and correct operation"
print "is not gaurenteed with any other version of the Python interpreter."
print ""
print "This package has a simple representation of a matrix, and code for LL^t and LDL^t factorizations."
print ""
print "The underlying Python interpreter can be used for simple math."
print ""
print "To create a matrix, use the following command:"
print "\tmat = Matrix(n, m, [val1, val2, ..., valn])"
print "where n is the height of the matrix, m is the width of the matrix, [val1, val2, ..., valn] is a"
print "comma separated list of values for the matrix, and mat is the name of the variable where you wish"
print "to store the matrix. Individual matrix elements may be accessed with the syntax \"mat[i, j]\","
print "where i is the row and j is the column of the element you wish to access. Remember, matrices are"
print "indexed from 0."
print ""
print "A square Identity Matrix can be created using:"
print "\tmat = IdentityMatrix(dim)"
print "where dim is the height and width of the matrix. A Null Matrix of any dimensions can be generated using:"
print "\tmat = NullMatrix(n, m)"
print "where n is the height and m is the width of the new Null Matrix."
print ""
print "Matrix addition can be performed with the + operator, scalar and matrix addition with the * operator."
print "Vector multiplication can be performed by representing the vector as a matrix."
print "To take the transpose of a matrix, call the transpose function on a matrix as follows:"
print "\tmat.transpose()"
print "This will return the transposed matrix, but will not transpose the original variable."
print ""
print "To perform a decomposition, a variable containing an instance of Cholesky is needed."
print "One such variable is provided at startup as \"decomp\"."
print "To perform a LL^t decomposition on a matrix, simply call the llt_decomp method of decom on a matrix:"
print "\tdecomp.llt_decomp(mat)"
print "Likewise, to perform a LDL^t decomposition, call:"
print "\tdecomp.ldlt_decomp(mat)"
print "The results of the decompositions are returned as a dict, the indexing operator [] may be used to access"
print "individual entries. For instance,"
print "\tdict[\'L\']"
print "\tdict[\'D\']"
print "\tdict[\'L^t\']"
print "may be used to access the L, D and L^t matrices, where dict is the result of a decomposition."
print ""
print "To print a matrix, simply use the \"print\" command on any matrix, like so:"
print "\tprint mat"
print "The print operator may also be used on the dict type returned by the decomposition commands, so"
print "\tprint dict"
print "will print all the results of the decomposition."
print ""
print "For more information about using the Tube Alloys system, consult the source code and the"
print "Python 2.7 documentation."
print ""
print "Copyright Parker Michaelson, 2013. Thanks for using Tube Alloys! :-)"
print ""
print ""

decomp = Cholesky()
