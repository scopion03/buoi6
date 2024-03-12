class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_by_index(self, index):
       
        if self.head is None or index < 0:
            return None
 
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node

       
        current = self.head
        for i in range(index - 1):
           
            if current.next is None:
                return None
            current = current.next

        if current.next is None:
            return None

        deleted_node = current.next
        current.next = current.next.next
        return deleted_node

linked_list = LinkedList()

deleted_node = linked_list.delete_by_index(1)
if deleted_node:
    print(f'Deleted node with data: {deleted_node.data}')
else:
    print('Index out of bounds or list is empty')
