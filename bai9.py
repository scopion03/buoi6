class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


head1 = ListNode(1, ListNode(1, ListNode(2)))
printList(deleteDuplicates(head1))  # Output: 1 2

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
printList(deleteDuplicates(head2))  