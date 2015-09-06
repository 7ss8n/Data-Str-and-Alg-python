'''
class Bag:
    def __init__( self ):
        self._items = list()

    def __len__( self ):
        return len(self._items)

    def __contains__( self, item ):
        return item in self._items

    def add( self, item ):
        self._items.append( item )

    def remove( self, item ):
        assert item in self, 'The item is Not in bag.'
        self._items.remove( item )

    def __iter__( self, item ):
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
'''
class _BagListItem:
    def __init__( self, item ):
        self.data = item
        self.next = None
        
class Bag:
    def __init__( self ):
        self._head = None
        self._size = 0
        
    def __len__( self ):
        return self._size

    def __contains__( self, item ):
        curNode = self._head
        while curNode is not None and curNode.data != item:
            curNode = curNode.next
        return curNode is not None
        
    def add( self, item ):
        newNode = _BagListItem( item )
        newNode.next = self._head
        self._head = newNode
        self._size +=1

    def remove( self, item ):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next

        assert curNode is not None, 'The item must be in the bag.'

        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.data

    
    def __str__( self ):
        return str([item for item in self])
        
    def __iter__( self ):
        return _BagIterator( self._head )

class _BagIterator:
    def __init__( self, listHead ):
        self._curNode = listHead

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.data
            self._curNode = self._curNode.next
            return item
        
        
        
