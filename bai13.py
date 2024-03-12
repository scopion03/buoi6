class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
printList(middleNode(head))  


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
printList(middleNode(head))  