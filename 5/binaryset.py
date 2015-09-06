class Set:
    def __init__( self ):
        self._theElements = list()

    def __len__( self ):
        return len( self._theElements )

    def __contains__( self, element ):
        ndx = self._findPosition( element )
        return ndx < len( self ) and self._theElements[ndx] == element

    def add( self, element ):
        if element not in self:
            ndx = self._findPosition( element )
            self._theElements.insert( ndx, element )

    def remove( self, element ):
        assert element in self, 'Element is not in set.'
        ndx = self._findPosition( element )
        self._theElements.pop(ndx)

    def __iter__( self ):
        return _SetIterator( self._theElements )

    def __str__( self ):
        return str(self._theElements)
    
    def __eq__( self, SetB ):
        if len( self ) != len( SetB ):
            return False
        else:
            for i in range( self ):
                if self._theElements[i] != SetB._theElements[i]:
                    return False
            return True
    def isSubsetOf( self, SetB ):
        


        
    def union( self, SetB ):
        theNewSet = Set()
        a = 0
        b = 0
        while a < len( self ) and b < len( SetB ):
            if self._theElements[a] <= SetB._theElements[b]:
                theNewSet._theElements.append(self._theElements[a])
                a += 1
            else:
                theNewSet._theElements.append(SetB._theElements[b])
                b += 1

        while a < len( self ):
            theNewSet._theElements.append(self._theElements[a])
            a += 1

        while b < len( SetB ):
            theNewSet._theElements.append(self._theElements[b])
            b += 1

        return theNewSet
    
    def _findPosition( self, element ):
        low = 0
        high = len( self ) - 1
        while low <= high:
            mid = ( low + high ) // 2
            if self._theElements[mid] == element:
                return mid
            elif element < self._theElements[mid]:
                high = mid -1
            else:
                low = mid + 1

        return low
                

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
