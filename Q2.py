class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def findNthToLast(head, n):
    pointer1 = head
    pointer2 = head
    
    for i in range(n):
        if pointer2 is None:
            print("Danh sách có ít phần tử hơn n")
            return None
        pointer2 = pointer2.next
        
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    return pointer1.value

# Ví dụ sử dụng:
# Tạo một danh sách liên kết: 1 -> 2 -> 0 -> 3 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

n = 2 # Thay đổi giá trị này để thử nghiệm với các giá trị khác của n

# Tìm phần tử thứ n từ cuối
print(findNthToLast(head, n))
