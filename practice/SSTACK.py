class Stack:
    def __init__(self):
        self.items=[]
    def push(self,a):
        self.items.append(a)
    def pop(self):
        if len(self.items)<1:
            print("stack is empty")
            return false
        result = self.items.pop()
        return result
    def isempty(self):
        if len(self.items)<1:
            return true
    def istwo(self):
        if len(self.items)==2:
            return true