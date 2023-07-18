class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def create_new_linked_list(list1, list2):
    result_head = None
    result_tail = None

    while list1 and list2:
        if list1.data >= list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next

        if result_head is None:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = new_node
            
    while list1:
        new_node = Node(list1.data)
        list1 = list1.next

        if result_head is None:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = new_node

    while list2:
        new_node = Node(list2.data)
        list2 = list2.next

        if result_head is None:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = new_node

    return result_head


list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

new_list = create_new_linked_list(list1, list2)

while new_list:
    print(new_list.data, end="->")
    new_list = new_list.next

