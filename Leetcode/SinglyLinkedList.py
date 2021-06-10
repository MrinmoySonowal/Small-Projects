class Node:
    def __init__(self, val, next_node):
        """
        Constructor for a singly linked list head
        :param val: Value of current head
        :param next_node: Next head of the linked list
        """
        self.val = val
        self.next = next_node

    def __str__(self):
        """
        To string method for Linked List
        :return: The linked list in the format val_1->val_2->...->val_n->None
                for a linked list of size n
        """
        return str(self.val) + '->' + str(self.next)
