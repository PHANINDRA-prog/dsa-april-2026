class Node:
  def __init__(self,info,next = None):
    self.data = info
    self.next = next


class SinglyLinkedList:
  def __init__(self):
    self.head = Node(0,None)
    self.tail = Node(0,None)

    self.head.next = self.tail
  

  def insert(self,value,pos):
    node = Node(value)
    if pos == 0:
      temp = self.head.next
      self.head.next = node
      node.next = temp
    
    elif pos == "end":
      prev = self.head.next
      while (prev.next != self.tail):
        prev = prev.next
      prev.next = node
      node.next = self.tail
    
    else:
      curr = self.head.next
      while (curr != self.tail):
        if (curr.data == pos):
          temp = curr.next
          curr.next = node
          node.next = temp
          break
        else:
          curr = curr.next
    

  def delete(self,value):
    if (self.head.next.next == None):
      print("List is Empty")
      return
    curr = self.head.next
    prev = self.head
    if curr.data == value:
      self.head.next = curr.next
      return
    
    while (curr != self.tail):
      if (curr.data == value):
        prev.next = curr.next
        break
      else:
        prev = prev.next
        curr = curr.next

  

  def printLinkedList(self):
    if (self.head.next.next == None):
      print("List is Empty")
      return
    curr = self.head.next
    while (curr.next != self.tail):
      print(curr.data, end = "->")
      curr = curr.next
    print(curr.data)




a = SinglyLinkedList()
a.insert(1,0)
a.insert(2,1)
a.insert(3,2)
a.insert(4,"end")
a.printLinkedList()
a.delete(3)
a.printLinkedList()
a.delete(1)
a.delete(2)
a.printLinkedList()
a.delete(4)
a.printLinkedList()




class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = Node(0)

        # Empty List
        self.head.next = self.head

    def insert(self, value, pos):
        node = Node(value)

        # Insert at beginning
        if pos == 0:
            temp = self.head.next
            self.head.next = node
            node.next = temp

        # Insert at end
        elif pos == "end":
            prev = self.head

            while prev.next != self.head:
                prev = prev.next

            prev.next = node
            node.next = self.head

        # Insert after a value
        else:
            curr = self.head.next

            while curr != self.head:
                if curr.data == pos:
                    temp = curr.next
                    curr.next = node
                    node.next = temp
                    break
                else:
                    curr = curr.next

    def delete(self, value):

        if self.head.next == self.head:
            print("List is Empty")
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:

            if curr.data == value:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

    def printLinkedList(self):

        if self.head.next == self.head:
            print("List is Empty")
            return

        curr = self.head.next

        while curr != self.head:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("(back to dummy)")


a = CircularSinglyLinkedList()

a.insert(1, 0)
a.insert(2, 1)
a.insert(3, 2)
a.insert(4, "end")

a.printLinkedList()

a.delete(3)
a.printLinkedList()

a.delete(1)
a.printLinkedList()

a.delete(2)
a.printLinkedList()

a.delete(4)
a.printLinkedList()

        