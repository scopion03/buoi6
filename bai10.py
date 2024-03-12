class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_elements(self, val):
        dummy = Node(0)  
        dummy.next = self.head
        current = dummy

        while current.next:
            if current.next.data == val:
                current.next = current.next.next  
            else:
                current = current.next  
        self.head = dummy.next  

linked_list = LinkedList()

linked_list.remove_elements(2) 