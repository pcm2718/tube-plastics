import sys

class Matrix:

    # Constructor, assumes that the matrix is square if only one dimension argument is provided.
    def __init__(self, n, m=None, values=[]):
        if n == None:
            self.n = 1
            self.m = len(Values)
        elif m == None:
            self.n = n
            self.m = len(values)/self.n
        else:
            self.n = n
            self.m = m

        if len(values) != self.m*self.n:
            raise ValueError("Values array does not match specified dimensions.")

        values = map(lambda x : float(x), values)
        self.values = values[0:self.n*self.m]



    def __str__(self):
        retstr = ""

        retstr += "\n\n"
        retstr += "[\n"

        for i in range(0, self.n):
            for j in range(0, self.m):
                retstr += '{: 14,.6f}'.format(self.values[self.m*i + j])
                retstr += ' , '
            retstr += "\n"

        retstr += "]\n"

        return retstr



    def __repr__(self):
        return self.__str__()


    # Retrive a matrix entry with the syntax mat[i, j].
    def __getitem__(self, a):
        return self.values[a[0]*self.m + a[1]]



    # Set a matrix entry with the syntax mat[i, j] = b.
    def __setitem__(self, a):
        self.values[(a[0] % self.n)*self.m + a[1] % self.m] = b



    # Defines matrix addition, self is assumed to be the matrix on the left, but this is irrelevant as addition is commutative. 
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("Cannot add, matrix dimensions do not match.")

            return Matrix(self.n, self.m, [self.values[k] + other.values[k] for k in range(0, self.n*self.m)])

        else:
            raise TypeError("Cannot add matrix and object of type " + str(type(other)))



    # Defines matrix subtraction, self is assumed to be the matrix on the left.
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("Cannot subtract, matrix dimensions do not match.")

            return Matrix(self.n, self.m, [self.values[k] - other.values[k] for k in range(0, self.n*self.m)])

        else:
            raise TypeError("Cannot subtract matrix and object of type " + str(type(other)))



    # This function defines matrix multiplication by both scalars and other matricies. It assumes the instance of matrix calling it is on the left side of the
    # the matrix multiplication.
    def __mul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                raise ValueError("Cannot multiply, matrix dimensions are incompatable.")

            return Matrix(self.n, self.n, [sum(map(lambda x : x[0]*x[1], zip(self.get_row(k/self.n), other.get_col(k)))) for k in range(0, self.n*self.n)])

        else:
            raise TypeError("Cannot multiply matrix and object of type " + str(type(other)))
   

            
    # This function defines multiplication by a matrix in a manner identical to the one above, except that this function assumes that the instance of Matrix
    # calling it is on the right side of the multiplication. In theory it should only be called to handle the case where a vector is left multiplied by a scalar.
    def __rmul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                raise ValueError("Cannot multiply, matrix dimensions are incompatable.")

            return Matrix(self.m, self.m, [sum(map(lambda x : x[0]*x[1], zip(other.get_row(k/other.n), self.get_col(k)))) for k in range(0, self.m*self.m)])

        else:
            raise TypeError("Cannot multiply matrix and object of type " + str(type(other)))



    # Return the transposed matrix.
    def transpose(self):
        return Matrix(self.m, self.n, [self.values[(k%self.n)*self.m + (k/self.n)] for k in range(0, self.n*self.m)])



    # Get a row, indexed from 0, wraping around either side of the matrix.
    def get_row(self, row):
        row = row % self.n
        return self.values[row*self.m:(row+1)*self.m]



    # Get a column, indexed from 0, wraping around the top and bottom of the matrix.
    def get_col(self, col):
        col = col % self.m
        return [self.values[i*self.m + col] for i in range(0, self.n)]



    # Swap two rows, indexed from 0, and return the resulting Matrix.
    def row_swap(self, row_1, row_2):
        row_1 = row_1 % self.n
        row_2 = row_2 % self.n
        mat = Matrix(self.m, self.n, self.values)
        temp = mat.values[row_1*mat.m:(row_1+1)*self.m]
        mat.values[row_1*mat.m:(row_1+1)*self.m] = mat.values[row_2*mat.m:(row_2+1)*self.m]
        mat.values[row_2*mat.m:(row_2+1)*self.m] = temp
        return mat



    # Multiply a row, indexed from 0, by a scalar, and return new Matrix.
    def row_mult(self, row, sca):
        row = row % self.n
        mat = Matrix(self.m, self.n, self.values)
        mat.values[row*self.m:(row+1)*self.m] = [sca * x for x in mat.values[row*mat.m:(row+1)*mat.m]]
        return mat



    # Perform linear row combination, and return the new Matrix.
    def row_comb(self, row_dest, row_from, sca_from):
        row_dest = row_dest % self.n
        row_from = row_from % self.n
        mat = Matrix(self.m, self.n, self.values)
        mat.values[row_dest*mat.m:(row_dest+1)*mat.m] = map(lambda x : x[0] + sca_from*x[1], zip(mat.values[row_dest*mat.m:(row_dest+1)*mat.m], mat.values[row_from*mat.m:(row_from+1)*mat.m]))
        return mat



    # Not yet implemented.
    def is_triangular(self):
        pass



    # Not yet implemented.
    def is_upper(self):
        pass



    # Not yet implemented.
    def is_lower(self):
        pass



# This class is a subclass of Matrix, always creating a null matrix on initializaiton.
class NullMatrix(Matrix):

    def __init__(self, n, m=None):
        if m == None:
            m = n
        Matrix.__init__(self, n, m, [0]*n*m)



# This class is a subclass designed to improve the ease of use of identity matricies.
class IdentityMatrix(Matrix):

    def __init__(self, dim):
        values = [0]*(dim ** 2)
        for i in range(0, dim):
            values[i*dim + i] = 1
        Matrix.__init__(self, dim, dim, values)



# This class is a subclass designed to represent a row vector of size n by extending the Matrix class.
# I'll add this later.



# This class is a subclass designed to represent a column vector of size n by extending the Matrix class.
# I'll add this later.
