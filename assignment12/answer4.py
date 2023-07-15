class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_loop(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

    return None

def remove_loop(head):
    if head is None or head.next is None:
        return head

    loop_node = detect_loop(head)

    if loop_node is not None:
        start_node = head

        while start_node.next != loop_node.next:
            start_node = start_node.next
            loop_node = loop_node.next

        loop_node.next = None  # Unlink the last node which forms the loop

    return head
# Create the linked list 1->3->4
head = ListNode(1)
node1 = ListNode(3)
node2 = ListNode(4)
head.next = node1
node1.next = node2
node2.next = node1  # Create the loop

# Remove the loop from the linked list
head = remove_loop(head)

# Print the modified linked list
current = head
while current is not None:
    print(current.val, end=" ")
    current = current.next
