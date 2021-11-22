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

    def insert_at_end(self, data):
        # none means a null or empty element
        if self.head is None:
            self.head = Node(data, None)
            return

        # if your linked list is not blank, iterate through
        # list and at end, put the element
        itr = self.head
        # if it has a value, you aren't at the end
        while itr.next:
            itr = itr.next
        # if the last element is null, at last element
        # now point it to the new node
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        #iterate through linked list
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    # create a linkedlist object
    ll = LinkedList()
    # insert a list of values
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    # insert nodes at the beginning and end
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.prnt()
