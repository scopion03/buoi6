class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = ListNode(1)
current = head
for i in range(2, 6):
    current.next = ListNode(i)
    current = current.next

reversed_list = reverse_linked_list(head)

current = reversed_list
while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
