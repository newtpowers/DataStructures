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
        # iterate through linked list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        # throw error if outside of boundary
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        # trying to remove a head
        if index == 0:
            # the new head of the data is the next node because
            # the head is removed (decapitated haha)
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        # iterate through linkedlist
        while itr:
            # stop at previous element and have it point to the element
            # after the one you want to remove, to remove the unwanted element
            if count == index - 1:
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        # throw error if outside of boundary
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # the previous element's next is this new node's next
                node = Node(data, itr.next)
                # the next element of the current element is the new node
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    # create a linkedlist object
    ll = LinkedList()
    # insert a list of values
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    # insert nodes at the beginning and end
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    # removes banana :(
    ll.remove_at(2)
    # insert the yummy figs
    ll.insert_at(4, "figs")
    ll.prnt()
    print("length", ll.get_length())
