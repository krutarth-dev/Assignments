class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_nth_from_end(head, n):
    main_ptr = head
    ref_ptr = head

    # Move the reference pointer N nodes ahead
    for _ in range(n):
        if ref_ptr is None:
            return None  # N is greater than the length of the linked list
        ref_ptr = ref_ptr.next

    # Move both pointers until the reference pointer reaches the end
    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.val
# Create the linked list 1->2->3->4->5->6->7->8->9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

# Find the 2nd node from the end
n = 2
result = get_nth_from_end(head, n)
print(result)  # Output: 8
