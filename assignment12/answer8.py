class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_circular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

result = is_circular(head)
print(result)
