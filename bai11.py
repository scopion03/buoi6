class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
printList(reverseList(head))  # Output: 5 4 3 2 1
