    # KEEP IN MIND THAT THE LINKED LISTS DS, DOESN'T CONTAIN NODES - 
    # THEY HAVE A HEAD POINING TO THE FIRST NODE OR TO A NONE IF NO NODES

class SLLNode:

    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None

    # to be able to see the next object we need to overwrite the dunder method
    def __repr__(self):
        return f"SLLNode object: data={self.data}"
        
    def get_data(self):
        '''Return the self.data attribute. '''
        return self.data

    def set_data(self, new_data):
        '''Replace the existing value of the self.data attribute with new_data parameter.'''
        self.data = new_data

    def get_next(self):
        '''Return the self.next attribute.'''
        return self.next

    def set_next(self, new_next):
        '''Replace the existing value of the self.next attribute with new_next parameter.'''
        self.next = new_next

class SLL:
    def __init__(self):
        self.head = None # when first creating the SLL we don't have any nodes associated with it

    def __repr__(self):
        return f"SLL object: head={self.head}"

    def is_empty(self):
        ''' Returns True if SLL is empty, otherwise False'''
        return self.head is None # can be self.head == None (is = more pythonic)

    def add_front(self, new_data):
        '''Add a node whose data is the new_data argument to the front of the linked list'''
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp # transferring the pointer from None to pointer to a Node

    def size(self):
        '''Traversing the linked list and returns an integer value representing the number of 
        nodes in the Linked List.
        
        The time complexity is O(n) - every node needs to be visited in order to calculate the size of the list.
        '''
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None: # While there are still Nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        pass

    def remove(self, data):
        pass

# Testing is_empty():

# >>> sll = SLL()
# >>> sll.is_empty()
# True
# >>> node = SLLNode()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __init__() missing 1 required positional argument: 'data'
# >>> node = SLLNode(5)
# >>> sll.head = node
# >>> sll.is_empty()
# False

# Testing the add_front():

# >>> sll = SLL()
# >>> sll.add_front('berries')
# >>> sll.head()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'SLLNode' object is not callable
# >>> sll.head
# SLLNode object: data=berries
# >>> sll.add_front('apples')
# >>> sll.head
# SLLNode object: data=apples