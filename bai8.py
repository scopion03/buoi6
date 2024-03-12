class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(list1, list2):
    
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list_head = merge_sorted_lists(list1, list2)


def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

print_list(merged_list_head)  
