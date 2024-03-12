class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    left, right = head, prev
    while right:  
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(isPalindrome(head))  

head = ListNode(1, ListNode(2, ListNode(3)))
print(isPalindrome(head))  
