class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode, x: int) -> ListNode:
    before = before_head = ListNode(0)
    after = after_head = ListNode(0)

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    # Kết thúc của danh sách 'after' nên trỏ đến None.
    after.next = None
    
    # Gộp danh sách 'before' và 'after'.
    before.next = after_head.next
    
    return before_head.next

# Hàm để in các giá trị của danh sách liên kết
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Tạo danh sách liên kết và phân chia xung quanh giá trị x
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
head = partition(head, x)
printList(head)  # Kết quả sau khi phân chia: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None
