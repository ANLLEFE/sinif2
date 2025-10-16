class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  
    def append(self, data):
       
        new_node = Node(data)
        
       
        if self.head is None:
            self.head = new_node
            return
        
       
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
    
    def print_list(self):
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
       
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        current = self.head
        
        
        while current:
            next_temp = current.next  
            current.next = prev     
            prev = current          
            current = next_temp      
        
        self.head = prev  

if __name__ == "__main__":
    
    llist = LinkedList()
    
    
    llist.append(2)
    llist.append(3)
    llist.append(5)
    
    print("Orijinal liste:")
    llist.print_list()
    
    llist.reverse()
    
    print("\nTers çevrilmiş liste:")
    llist.print_list()
