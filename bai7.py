class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        prev = None
        seen_data = set()

        while current:
            if current.data in seen_data:
               
                prev.next = current.next
            else:
             
                seen_data.add(current.data)
                prev = current
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

linked_list = LinkedList()
for data in [1, 2, 4, 3, 4, 2]:
    linked_list.insert_at_end(data)  

print(f'Original Linked List - "{linked_list}"')
linked_list.remove_duplicates()
print(f'Result Linked List - "{linked_list}"')
