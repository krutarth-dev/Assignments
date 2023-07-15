class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
# Create the linked list 1->3->4->3 (loop)
head = ListNode(1)
node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(3)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1 
# Check if the linked list has a loop
print(has_cycle(head))  
