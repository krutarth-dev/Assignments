class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_alternate_k_nodes(head, k):
    if head is None or k <= 1:
        return head

    current = head
    next_node = None
    prev = None
    count = 0

    # Reverse k nodes
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    # Skip k nodes
    count = 0
    while current and count < k - 1:
        current = current.next
        count += 1

    # Recursive call on the next alternate group
    if current:
        current.next = reverse_alternate_k_nodes(current.next, k)

    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

k = 3

new_head = reverse_alternate_k_nodes(head, k)

current = new_head
while current:
    print(current.data, end=" ")
    current = current.next

