class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_last_occurrence(head, key):
    if head is None:
        return None

    current = head
    last_occurrence = None

    # Find the last occurrence of the key
    while current:
        if current.data == key:
            last_occurrence = current
        current = current.next

    # If key is not found, return the original linked list
    if last_occurrence is None:
        return head

    # If the last occurrence is the head node
    if last_occurrence == head:
        head = head.next
    else:
        # Find the node before the last occurrence
        prev = head
        while prev.next != last_occurrence:
            prev = prev.next

        # Delete the last occurrence
        prev.next = last_occurrence.next

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(5)

key = 2

new_head = delete_last_occurrence(head, key)

current = new_head
while current:
    print(current.data, end=" ")
    current = current.next

