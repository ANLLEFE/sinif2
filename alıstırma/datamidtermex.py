class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 
    
    def insert(self, newNode):
        # head => anil -> None
         if self.head is None:
             self.head = newNode
         else:
            #head => anil -> berkay -> None || head => anil -> arda 
            
             lastNode = self.head 
             while True: 
                 if lastNode.next is None: 
                     break 
                 lastNode = lastNode.next
             lastNode.next= newNode 
    def printlist(self):
        # head => anil -> berkay -> arda -> None
        currentNode = self.head 
        print(currentNode.data)
        currentNode = currentNode.next
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

# Node = data, next 
firstNode = Node("Anil")
linkedList = Linkedlist()
linkedList.insert(firstNode)
secondNode = Node("Berkay")
linkedList.insert(secondNode)
thirdNode = Node("Arda")
linkedList.insert(thirdNode)
linkedList.printlist()
