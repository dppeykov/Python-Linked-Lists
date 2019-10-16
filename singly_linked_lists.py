class SLLNode:
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

# TO RUN INTERACTIVELY ON THE COMMAND LINE USE: python -i name_of_script.py
node = SLLNode('apple') # initialize the linked list with the first node
print(node.get_data()) # 'apple'
node.set_data('new')
print(node.get_data()) # 'new'
node2 = SLLNode('apple') # creates a new node
print(node2.get_data()) # 'apple'  ----------------------->> at this point we have 2 nodes, not connected to each other
node.set_next(node2) # node2 is linked to node, but the data stays to each node: (node: new ) --> (node2: apple)
print(node.get_next()) # <__main__.SLLNode object at 0x000001E3F3668898> -->> WITHOUT THE DUNDER METHOD (__repr__)
# WWITH THE __repr__ OVERWRITTEN: SLLNode object: data=apple