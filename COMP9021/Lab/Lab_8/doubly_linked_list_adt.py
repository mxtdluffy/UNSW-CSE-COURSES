# A Doubly Linked List abstract data type
#
# Written by Eric Martin for COMP9021


from copy import deepcopy


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    # Creates a linked list possibly from a list of values.
    def __init__(self, L = None, key = lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node

    def print(self, separator = ', '):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.print(separator = ' : ')
        2 : 0 : 1 : 3 : 7
        '''
        # Replace pass above withn your code
        if not self.head:
            return
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next_node
        print(separator.join(nodes))

    def duplicate(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL_copy = LL.duplicate()    
        >>> LL_copy.print()
        2, 0, 1, 3, 7
        '''
        # Replace pass above withn your code
        if not self.head:
            return
        node = self.head
        node_copy = Node(deepcopy(node.value))
        L = DoublyLinkedList(key = self.key)
        L.head = node_copy
        node = node.next_node
        while node:
            node_copy.next_node = Node(deepcooy(node.value))
            node_copy.next_node.previous_node = node_copy
            node_copy = node_copy.next_node
            node = node.next_node
        return L

    def length(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.length())
        5
        '''
        # Replace pass above withn your code
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_node
        return count

    def apply_function(self, function):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.apply_function(lambda x: 2 * x)
        >>> LL.print()
        4, 0, 2, 6, 14
        '''
        # Replace pass above withn your code
        node = self.head
        while node:
            node.value = function(node.value)
            node = node.next_node

    def is_sorted(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.is_sorted())
        False
        '''
        # Replace pass above withn your code
        node = self.head
        while node and node.next_node:
            if self.key(node.value) > self.key(node.next_node.value):
                return False
            node = node.next_node
        return True

    def extend(self, LL):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(LL.duplicate())
        >>> LL.print()
        2, 0, 1, 3, 7, 2, 0, 1, 3, 7
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(DoublyLinkedList([]))
        >>> LL.print()
        2, 0, 1, 3, 7
        '''
        # Replace pass above withn your code
        if not LL.head:
            return
        if not self.head:
            self.head = LL.head
            return

        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = LL.head
        LL.head.previous_node = node 

    def reverse(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7, 2, 0, 1, 3, 7])
        >>> LL.reverse()
        >>> LL.print()
        7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        # Replace pass above withn your code
        if not self.head:
            return
        node = self.head.next_node
        self.head.next_node = None
        self.head.previous_node = node
        while node:
            next_node = node.next_node
            node.next_node = self.head
            self.head.previous_node = node
            self.head = node
            node = next_node

    def index_of_value(self, value):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.index_of_value(2))
        4
        >>> print(LL.index_of_value(5))
        -1
        '''
        # Replace pass above withn your code
        index = 0
        node = self.head
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next_node
        return -1

    def value_at(self, index):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.value_at(4))
        2
        >>> print(LL.value_at(10))
        None
        '''
        # Replace pass above withn your code
        if index < 0:
            return
        node = self.head
        while node and index:
            node = node.next_node
            index -= 1
        if node:
            return node.value
        return
        

    def prepend(self, LL):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> LL.prepend(DoublyLinkedList([20, 21, 22]))
        >>> LL.print()
        20, 21, 22, 7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        # Replace pass above withn your code
        LL_length = LL.length()
        if LL_length == 0:
            return
        value = LL.value_at(0)
        node = Node(value)
        first_node = node
        for i in range(1, LL_length):
            value = LL.value_at(i)
            new_node = Node(value)
            node.next_node = new_node
            new_node.previous_node = node
            node = node.next_node
        node.next_node = self.head
        self.head.previous_node = node
        self.head = first_node
            
    def append(self, value):
        '''
        >>> LL = DoublyLinkedList()
        >>> LL.append(10)
        >>> LL.print()
        10
        >>> LL.append(15)
        >>> LL.print()
        10, 15
        '''
        # Replace pass above withn your code
        if not self.head:
            self.head = Node(value)
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        new_node = Node(value)
        node.next_node = new_node
        new_node.previous_node = node

    def insert_value_at(self, value, index):
        '''
        >>> LL = DoublyLinkedList([10, 15])
        >>> LL.insert_value_at(5, 0)
        >>> LL.insert_value_at(25, 3)
        >>> LL.insert_value_at(20, 3)
        >>> LL.print()
        5, 10, 15, 20, 25
        '''
        # Replace pass above withn your code
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if index <= 0:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            return
        node = self.head

    def insert_value_before(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([5, 10, 15, 20, 25])
        >>> LL.insert_value_before(0, 5)
        True
        >>> LL.insert_value_before(30, 35)
        False
        >>> LL.insert_value_before(22, 25)
        True
        >>> LL.insert_value_before(7, 10)
        True
        >>> LL.print()
        0, 5, 7, 10, 15, 20, 22, 25
        '''
        # Replace pass above withn your code
        if not self.head:
            return False
        if self.head.value == value_2:
            self.insert_value_at(value_1, 0)
            return True
        node = self.head
        while node.next_node and node.next_node.value != value_2:
            node = node.next_node
        if not node.next_node:
            return False
        new_node = Node(value_1)
        new_node.next_node = node.next_node
        node.next_node.previous_node = new_node
        node.next_node = new_node
        new_node.previous_node = node

    def insert_value_after(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([0, 5, 7, 10, 15, 20, 22, 25])
        >>> LL.insert_value_after(3, 1)
        False
        >>> LL.insert_value_after(2, 0)
        True
        >>> LL.insert_value_after(12, 10)
        True
        >>> LL.insert_value_after(27, 25)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27
        
        '''
        # Replace pass above withn your code
        if not self.head:
            return False
        node = self.head
        while node and node.value != value_2:
            node = node.next_node
        if not node:
            return False
        new_node = Node(value_1)
        new_node.next_node = node.next_node
        node.next_node.previous_node = new_node
        node.next_node = new_node
        new_node.previous_node = node
        return True

    def insert_sorted_value(self, value):
        '''
        >>> LL = DoublyLinkedList([0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27])
        >>> LL.insert_sorted_value(-5)
        >>> LL.insert_sorted_value(17)
        >>> LL.insert_sorted_value(30)
        >>> LL.print()
        -5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30
        
        '''
        # Replace pass above withn your code
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value <= self.key(self.head.value):
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            return
        node = self.head
        while node.next_node and value > self.key(node.next_node.value):
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node.previous_node = new_node
        node.next_node = new_node
        new_node.previous_node = node

    def delete_value(self, value):
        '''
        >>> LL = DoublyLinkedList([-5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30])
        >>> LL.delete_value(-5)
        True
        >>> LL.delete_value(30)
        True
        >>> LL.delete_value(15)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 17, 20, 22, 25, 27
        
        '''
        # Replace pass above withn your code
        if not self.head:
            return False
        if self.head.value == value:
            self.head.next_node.previous_node = None
            self.head = self.head.next_node
            return True
        node = self.head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node:
            node.next_node = node.next_node.next_node
            node.next_node.next_node.previous_node = node
            return True
        return False
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

