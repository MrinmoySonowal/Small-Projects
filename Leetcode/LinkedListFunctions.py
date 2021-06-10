from SinglyLinkedList import Node


def delete_node(node: Node, index: int):
    """
    Function to delete the element at a certain index
    :param node: Linked List in consideration
    :param index: Index of the element to delete in the linked List ( must be greater than 0)
    :raises IndexError: When index is not in range 0 to n-1, where n is the length of the linked list
    """
    if index < 0:
        raise IndexError("Index must be greater than 0")

    if index == 0:
        node = node.next
        return

    i = 0
    n = node
    while i < index - 1 and (n is not None):
        n = n.next
        i += 1
    if n.next is not None:
        n.next = n.next.next
    else:
        raise IndexError("Out of index")


def delete_node_from_end(node: Node, index: int):
    delete_node(node, length_linked_list(node) - index)


def length_linked_list(head: Node) -> int:
    """
    :param head: Head of linked list node
    :return: Size of the linked list
    """
    if head is None:
        return 0
    i = 0
    n = head
    while n is not None:
        n = n.next
        i += 1
    return i


a = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
print(length_linked_list(a))
delete_node_from_end(a, 1)
print(a)
