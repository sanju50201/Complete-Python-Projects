# create a class for the Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a class for the Linked List


class LinkedList:
    def __init__(self):
        self.head = None

    # method to append a node to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    # method to display the node
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    # method to search for a node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    # method to delete a node
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


# instantiating the class
linked_list = LinkedList()

# add some nodes to the list
linked_list.append(1)
linked_list.append(6)
linked_list.append(9)
linked_list.append(4)
linked_list.append(19)
linked_list.append(14)

linked_list.remove(9)

print(f"The search element is present? {linked_list.search(14)}")

# display the contents in the list
linked_list.display()
