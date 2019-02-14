class Node:
  def __init__(self, data):
    self.data = data # assing value
    self.next = None # initialize next as null

class LinkedList:
  def __init__(self):
    self.head = None


if __name__ == '__main__':

  # create empty list
  list_linked = LinkedList)()

  list_linked.head = Node(1)

  second = Node(2)
  list_linked.next = second
  third = Node(3)
  second.next = third
