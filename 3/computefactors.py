def com( *dim ):
    self = [1] * len(dim)
    for j in range(len(dim)):
        for d in dim[j+1:]:
            print d
            self[j] *= d
    return self
