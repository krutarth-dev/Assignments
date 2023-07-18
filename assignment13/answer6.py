class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Determine the head of the merged list
    if head1.data <= head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next

    current = merged_head

    # Merge the remaining nodes
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Append the remaining nodes from either list
    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return merged_head

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

merged_head = merge_sorted_lists(head1, head2)

current = merged_head
while current:
    print(current.data, end="->")
    current = current.next

