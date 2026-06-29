class Node:
  def __init__(self,data,prev=None,next=None):
    self.prev = prev
    self.data = data
    self.next = next
  

class DoublyLinkedList:
  def __init__(self):
    self.head = Node(0)
    self.tail = Node(0)

    self.head.next = self.tail
    self.tail.prev = self.head
  

  def insert(self,value,pos):
    node = Node(value)
    if pos == 0:
      temp = self.head.next
      self.head.next = node
      node.prev = self.head
      node.next = temp
      temp.prev = node
    
    elif pos == "end":
      prev = self.tail.prev
      self.tail.prev = node
      node.next = self.tail
      node.prev = prev
      prev.next = node
    
    else:
      curr = self.head.next
      while (curr != self.tail):
        if (curr.data == pos):
          temp = curr.next
          curr.next = node
          node.prev = curr
          node.next = temp
          temp.prev = node
          break
        else:
          curr = curr.next
    
  def remove(self,value):
    if self.head.next == self.tail:
      print("Empty Linked List")
      return
    
    curr = self.head.next
    while (curr != self.tail):
      if (curr.data == value):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        break
      else:
        curr = curr.next
  
  def printLinkedList(self):
    if self.head.next == self.tail:
      print("Empty Linked List")
      return
    
    curr = self.head.next
    while (curr.next != self.tail):
      print(curr.data , end = "<->")
      curr = curr.next
    print(curr.data)
    

