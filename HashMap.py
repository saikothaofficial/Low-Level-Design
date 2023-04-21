class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None



def showList(node):
    while node:
        print('(',node.key,node.value,')',end = '-> ')
        node = node.next
    print()            
        


class HashMap:
    def __init__(self):
        self.size = 100
        self.map = [None]*self.size
    
    def put(self,key,value):
        index = key % self.size
        curr = self.map[index]
        if curr == None:
            self.map[index] = Node(key,value)
        else:
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next == None:break
                curr = curr.next
            curr.next = Node(key,value)
    
    def get(self,key):
        index = key % self.size
        curr = self.map[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
    
    
    def remove(self,key):
        index = key % self.size
        curr = self.map[index]
        if not curr:return
        if curr.key == key:
            self.map[index] = curr.next
        else:
            prev = curr
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                curr = curr.next
                prev = prev.next
    
    def show(self):
        for i in range(len(self.map)):
            if self.map[i] != None:
                showList(self.map[i])
                
                


d = HashMap()
d.put(10,20)
d.put(20,20)
d.put(45,20)
d.put(85,20)
d.put(185,30)
d.show()
print(d.get(185))


            
                
            
            
        
