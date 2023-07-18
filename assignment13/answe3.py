class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_k_nodes(head, k):
    if head is None or k == 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while True:
        count = 0
        current = prev.next
        tail = prev

        while current:
            count += 1
            current = current.next

            if count % k == 0:
                tail = reverse_list(tail.next, current.next)
                break

        if not current:
            break

        prev = tail

    return dummy.next


def reverse_list(head, next_node):
    prev = None
    current = head

    while current != next_node:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    head.next = next_node

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 3

new_head = reverse_k_nodes(head, k)

current = new_head
while current:
    print(current.data, end=" ")
    current = current.next

