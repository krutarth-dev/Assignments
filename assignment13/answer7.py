class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None:
        return None

    current = head
    prev = None

    # Reverse the next and prev pointers of each node
    while current:
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node

    # Update the head to the last node
    head = prev

    return head

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

new_head = reverse_doubly_linked_list(head)

current = new_head
while current:
    print(current.data, end="<->")
    current = current.next

