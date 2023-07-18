class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    current = head

    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

new_head = remove_duplicates(head)

current = new_head
while current:
    print(current.data, end="->")
    current = current.next

