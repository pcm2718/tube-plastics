class RowReduce:

    def __init__(self):
        pass



    def row_reduce(self, mat_a, vec_b):
        pass



    def back_substitute(self, mat_a, vec_b):

        for i in range(0, mat_a.n):
            for j in range(0, i):
                if (mat_a[i, j] != 0):
                    raise ValueError('Only upper triangluar matricies are valid targets for back substitution.')
