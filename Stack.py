class Stack:
    def __init__(self):
        self.stackList=[]
        self.stackSize=0
    def push(self,item):
        self.stackList.append(item)
        self.stackSize+=1
    def pop(self):
        try:
            if self.stackSize==0:
                raise Exception("Stack is Empty, returning None")
            temp=self.stackList.pop()
            self.stackSize-=1
            return temp
        except Exception as e:
            print(str(e))
    def size(self):
        return self.stackSize
    def isEmpty(self):
        if self.stackSize==0:
            return True
        else:
            return False
    def top(self):
        try:
            if self.stackSize==0:
                raise Exception("Stack is Empty, returning None")
            return self.stackList[-1]
        except Exception as e:
            print(str(e))