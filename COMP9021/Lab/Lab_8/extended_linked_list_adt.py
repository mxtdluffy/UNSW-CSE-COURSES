
from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        # Replace pass above with your code
        cur_node = self.head
        value_array = []
        if not self.head:
            return
        cur_value = cur_node.value
        value_array.append(cur_value)
        while cur_node.next_node:
            cur_value = cur_node.next_node.value
            if cur_value in value_array:
                tmp_node = cur_node.next_node
                while tmp_node.next_node:
                    if tmp_node.next_node.value in value_array:
                        tmp_node = tmp_node.next_node
                    else:
                        break
                if tmp_node.next_node:
                    cur_node.next_node = tmp_node.next_node
                    cur_node = cur_node.next_node
                    value_array.append(cur_node.value)
                else:
                    cur_node.next_node = None
            

            else:
                value_array.append(cur_value)
                cur_node = cur_node.next_node




