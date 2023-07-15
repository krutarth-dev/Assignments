class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_alternate(head1, head2):
    current1 = head1
    current2 = head2

    while current1 is not None and current2 is not None:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    # Update the head of the second list to be None
    head2 = None

    return head1

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage
head1 = ListNode(5)
head1.next = ListNode(7)
head1.next.next = ListNode(17)
head1.next.next.next = ListNode(13)
head1.next.next.next.next = ListNode(11)

head2 = ListNode(12)
head2.next = ListNode(10)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(6)

head1 = insert_alternate(head1, head2)

print("First list after insertion:")
print_linked_list(head1)

print("Second list after insertion:")
print_linked_list(head2)

