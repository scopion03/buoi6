class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None

    ptrA = headA
    ptrB = headB

    while ptrA is not ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA

    return ptrA

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


intersect_val = 7
headA = ListNode(3, ListNode(1, ListNode(5, ListNode(9, ListNode(intersect_val)))))
headB = ListNode(2, ListNode(4, ListNode(6, ListNode(intersect_val, ListNode(2, ListNode(1))))))

ptr = headA
while ptr.next:
    ptr = ptr.next
ptr.next = headB.next.next.next  

intersection_node = getIntersectionNode(headA, headB)
if intersection_node:
    print(f"Nút giao nhau: {intersection_node.val}")
else:
    print("Không có nút giao nhau")

print("Danh sách A:")
printList(headA)
print("Danh sách B:")
printList(headB)
