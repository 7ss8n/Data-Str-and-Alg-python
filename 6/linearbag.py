class Bag:
    def __init__( self ):
        self._items = list()

    def __length__( self ):
        return len(self._items)

    def __contains__( self, item ):
        return item in self._items

    def add( self, item ):
        self._items.append( item )

    def remove( self, item ):
        assert item in self, 'The item is Not in bag.'
        self._itmes.remove( item )
    def __str__( self ):
        return str(self._items)

    def __iter__( self ):
        return _BagIterator( self._items )

class _BagIterator :
    def __init__( self, theList ):
        self._data = theList
        self._pointer = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._pointer < len ( self._data ):
            item = self._data[ self._pointer ]
            self._pointer += 1
            return item
        else:
            raise StopIteration


        
