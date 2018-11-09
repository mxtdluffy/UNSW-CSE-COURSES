# Written by Jingyun Shen for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
        self.length = len(L)

    def rearrange(self, step):       
        node = self.head
        for i in range(step - 2):
            node = node.next_node
        newHead = node.next_node
        newNode = newHead
        tmpNode = newHead.next_node
        node.next_node = Node()
        node = node.next_node
        node.next_node = tmpNode
        

        for i in range(self.length - 1):
            for j in range(step - 1):
                node = node.next_node
                if node == None:
                    node = self.head
            if not node.next_node == None:
                newNode.next_node = node.next_node
                newNode = newNode.next_node
                tmpNode = node.next_node
                node.next_node = Node()
                node = node.next_node
                if not tmpNode.next_node == None:
                    node.next_node = tmpNode.next_node
                else:
                    node.next_node = self.head
            else:
                newNode.next_node = self.head
                newNode = newNode.next_node
                tmpNode = self.head.next_node
                self.head = Node()
                node = self.head
                self.head.next_node = tmpNode
            
            if i == self.length - 2:
                newNode.next_node = None
                

        self.head = newHead
        
    
    
