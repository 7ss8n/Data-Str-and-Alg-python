class Set:
    def __init__( self ):
        self._theElements = list()

    def __length__( self ):
        return len(self._theElements)

    def __contains__( self, element ):
        return element in self._theElements

    def add( self, element ):
        if element not in self:
            self._theElements.append( element )

    def remove( self, element ):
        assert element in self, 'element is not in bag'
        self._theElements.remove( element )

    def __str__( self ):
        return str(self._theElements)
        
    def __eq__( self, theRhsSet ):
        return len(self) == len(theRhsSet) and self.isSubsetOf( theRhsSet )

    '''
    def isSubsetOf( self, theRhsSet ):
        result = []
        for element in self:
            result.append( element in theRhsSet )
        return min(result)
    '''

    def isSubsetOf( self, theRhsSet ):
        for element in self:
            if element not in theRhsSet:
                return False
        return True

    def union( self, theRhsSet ):
        theNewSet = Set()
        theNewSet._theElements.extend( self._theElements )
        for element in theRhsSet:
            theNewSet.add( element )
        return theNewSet

    def intersect( self, theRhsSet ):
        theNewSet = Set()
        theNewSet._theElements.extend([item for item in self if item in theRhsSet])
        return theNewSet

    def difference( self, theRhsSet ):
        theNewSet = Set()
        for element in self:
            if element not in theRhsSet:
                theNewSet.add( element )
        return theNewSet
    
    def isEmpty( self ):
        return self._theElements == []

    def __iter__( self ):
        return _SetIterator( self._theElements )

class _SetIterator:
    def __init__( self, theList ):
        self._setItems = theList
        self._curNdx = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNdx < len( self._setItems ):
            item = self._setItems[ self._curNdx ]
            self._curNdx += 1
            return item

        else:
            raise StopIteration
