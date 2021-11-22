class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

# taking data value and inserting that at the beginning of the linkedlist
    def insert_at_beginning(self, data):
        # create node with value data, next element for the node
        # will be current head
        node = Node(data, self.head)
        self.head = node

    def prnt(self):
        if self.head is None:
            print("Linked list is empty")
            return

        # assign head to head
        itr = self.head
        # create an empty linkedListString
        linkedListString = ''
        while itr:
            # add each node to the string
            linkedListString += str(itr.data) + '-->'
            # follow the link to the linked list
            itr = itr.next
        print(linkedListString)

if __name__ == '__main__':
    # create a linkedlist object
    ll = LinkedList()
    # insert two nodes at the beginning for the list
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.prnt()
