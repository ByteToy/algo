class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]

if __name__=="__main__":
    stack=Stack()
    stack.push("one")
    stack.push("two")
    print(stack.size())
    print(stack.items)
    stack.push("three")
    stack.push("four")
    print(stack.size())
    print(stack.items)
    print(stack.pop())
    print(stack.size())
    print(stack.items)