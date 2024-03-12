class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    current = head
    seen = set()
    
    while current and current.next:
        seen.add(current.val)
        if current.next.val in seen:
            current.next = current.next.next
        else:
            current = current.next
            
    return head

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
head = removeDuplicates(head)
printList(head)  
