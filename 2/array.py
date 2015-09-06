import ctypes

class Array:
    def __init__( self, size ):
        assert type(size) == int and size > 0, 'Size must be a positive integer!'
        self._size = size
        ArrayType = ctypes.py_object * 5
        self._slots = ArrayType()
        self.clear(None)

    def __len__( self ):
        return self._size

    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), 'Index out of Range!'
        return self._slots[index]

    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), 'Index out of Range!'
        self._slots[index] = value

    def clear( self, value ):
        for i in range( self._size ):
            self._slots[i] = value
            
    def __str__( self ):
        result = '['
        for i in range(len(self)):
           result += str(self._slots[i]) + ', '
        result += ']'
        return result
        
    def __iter__( self ):
        return _ArrayIterator( self._slots )

class _ArrayIterator:
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNdx < len( self._arrayRef ):
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

class Array2D:
    def __init__( self, nrows, ncols):
        self._allrows = Array(nrows)
        for i in range(nrows):
            self._allrows[i] = Array(ncols)

    def numRows( self ):
        return len(self._allrows)

    def numCols( self ):
        return len(self._allrows[0])
    
    def clear( self, value ):
        for i in range(self.numRows()):
            self._allrows[i].clear(value)
            
    def __getitem__( self, IndexTuple ):
        assert len(IndexTuple) == 2, 'Invalid # of array subscripts.'
        rowIndex = IndexTuple[0]
        colIndex = IndexTuple[1]
        assert rowIndex >= 0 and rowIndex < self.numRows() and\
               colIndex >=0 and colIndex < self.numCols(),\
               'Index out of Range!'
        return self._allrows[rowIndex][colIndex]

    def __setitem__( self, IndexTuple, value ):
        assert len(IndexTuple) == 2, 'Invalid # of array subscripts.'
        rowIndex = IndexTuple[0]
        colIndex = IndexTuple[1]
        assert rowIndex >= 0 and rowIndex < self.numRows() and\
               colIndex >=0 and colIndex < self.numCols(),\
               'Index out of Range!'
        self._allrows[rowIndex][colIndex] = value

    def __str__( self ):
        result = ''
        for i in range(self.numRows()):
            result += str(self._allrows[i])
        return result
'''
class Matrix:
    def __init__( self, nrows, ncols):
        self._data = Array2D(nrows, ncols)
        self.clear(0)
        
    def numRows( self ):
        return self._data.numRows()
    
    def numCols( self ):
        return self._data.numCols()

    def __getitem__( self, IndexTuple ):
        return self._data[IndexTuple[0], IndexTuple[1]]

    def __setitem__( self, IndexTuple, value):
        self._data[IndexTuple[0], IndexTuple[1]] = value

    def clear( self, value ):
        self._data.clear(0)
    
    def scaleBy( self, scalar):
        for i in range( self.numRows()):
            for j in range( self.numCols()):
                self._allrows[i, j] *= scalar
'''
class Matrix(Array2D):
    def __init__( self, nrows, ncols ):
        Array2D.__init__(self, nrows, ncols)
        self.clear(0)

    def scaleBy( self, scalar):
        for i in range( self.numRows()):
            for j in range( self.numCols()):
                self[i, j] *= scalar

    def transpose( self ):
        newMatrix = Array2D(self.numCols(), self.numRows())
        for i in range( self.numRows()):
            for j in range( self.numCols()):
                newMatrix[j, i] = self[i, j]
        return newMatrix

    def __add__( self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                'Matrix size must agree'
        newMatrix = Array2D(self.numRows(), self.numCols())
        for i in range( self.numRows()):
            for j in range( self.numCols()):
                newMatrix[i, j] = rhsMatrix[i, j] + self[i, j]
        return newMatrix
    
    def __sub__( self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                'Matrix size must agree'
        newMatrix = Array2D(self.numRows(), self.numCols())
        for i in range( self.numRows()):
            for j in range( self.numCols()):
                newMatrix[i, j] = rhsMatrix[i, j] - self[i, j]
        return newMatrix

    def __mul__( self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(), \
                'Matrix size must agree'
        newMatrix = Array2D(self.numRows(), rhsMatrix.numCols())
        for i in range( self.numRows()):
            for j in range( rhsMatrix.numCols()):
                newMatrix[i, j] = sum([self[i, k] * rhsMatrix[k, j] for k in range(self.numCols())])
        return newMatrix
