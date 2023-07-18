class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def delete_node_at_position(head, position):
    if head is None:
        return None

    # Special case: delete the head node
    if position == 1:
        head = head.next
        if head:
            head.prev = None
        return head

    current = head
    count = 1

    # Traverse to the node at the given position
    while current and count < position:
        current = current.next
        count += 1

    # If position is out of range
    if current is None:
        return head

    # Update the pointers of the surrounding nodes
    prev_node = current.prev
    next_node = current.next
    if prev_node:
        prev_node.next = next_node
    if next_node:
        next_node.prev = prev_node

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

position = 3
new_head = delete_node_at_position(head, position)

current = new_head
while current:
    print(current.data, end="<->")
    current = current.next

