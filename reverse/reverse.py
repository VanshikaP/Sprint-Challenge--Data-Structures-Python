class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node


    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    
    def remove_from_tail(self):
        if self.head is None:
            return None
        if self.head.next_node is None:
            self.head = None
            self.tail = None
        else:
            currentNode = self.head
            while currentNode.next_node.next_node is not None:
                currentNode = currentNode.next_node

            new_tail_node = currentNode
            tail_node = currentNode.next_node
            new_tail_node.next_node = None
            return tail_node.value
    

    def reverse_list(self, node, prev):
        if self.head is None:
            return
        
        elif self.head.next_node is None:
            return
        # base case - 2 elements
        elif self.head.next_node.next_node is None:
            head_node = self.head
            tail_node = self.head.next_node
            self.head = tail_node
            self.head.next_node = head_node
            self.head.next_node.next_node = None
        else:
            tail_value = self.remove_from_tail()
            self.reverse_list(self.head, None)
            self.add_to_head(tail_value)
        
        

    


