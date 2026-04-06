class stack:
    def __init__(self):
        self.items=[]
     
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self. is_empty():
             return self.items.pop() 
        else:
            return "stack is empty"
    def peep(self):
        if not self. is_empty():
            return self.items[-1]
        else:
            return "stack is empty"     
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items)==0
    
s=stack()
s.push(10)
s.push(20)
s.push(40)
s.push(83) 

print("Top elemenmts :",s.peep())    
print("size :",s.size())
print("pop :",s.pop())  
print("size :",s.size())             