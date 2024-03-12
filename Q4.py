class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def addTwoNumbers(l1, l2):
    head = ListNode(0)
    current = head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        carry, out = divmod(val1 + val2 + carry, 10)
        
        current.next = ListNode(out)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return head.next

# Ví dụ sử dụng:
# Tạo hai danh sách liên kết đại diện cho số 617 và 295
list1 = ListNode(7)
list1.next = ListNode(1)
list1.next.next = ListNode(6)

list2 = ListNode(5)
list2.next = ListNode(9)
list2.next.next = ListNode(2)

# Cộng hai danh sách liên kết và in ra kết quả
result = addTwoNumbers(list1, list2)
while result:
    print(result.value, end=" -> ")
    result = result.next
print("None")
