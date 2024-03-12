class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

linked_list = LinkedList()

middle_node = linked_list.find_middle()
if middle_node:
    print(f'Middle node data: {middle_node.data}')
else:
    print('List is empty')
