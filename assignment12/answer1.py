class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_middle_node(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    # Delete the second middle node for even length list
    if fast is None:
        prev.next = slow.next
    else:
        slow.next = slow.next.next

    return head
# Create the linked list 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Delete the middle node(s)
head = delete_middle_node(head)

# Print the modified linked list
current = head
while current is not None:
    print(current.val, end=" ")
    current = current.next
