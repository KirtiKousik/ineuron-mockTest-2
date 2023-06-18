class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        current.next = ListNode(carry)

    return dummy_head.next

# Example-1
# Creating linked list l1: [2, 4, 3]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating linked list l2: [5, 6, 4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next


# Example-2
# Creating linked list l1: [0]
l1 = ListNode(0)

# Creating linked list l2: [0]
l2 = ListNode(0)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next

# Example-3
# Creating linked list l1: [9, 9, 9, 9, 9, 9, 9]
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

# Creating linked list l2: [9, 9, 9, 9]
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next