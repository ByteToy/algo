from C04 import LinkedListStack

# LinkedListStack
print("=============LinkedListStack======")
linkstack= LinkedListStack.LinkedListStack()
linkstack.push(1)
linkstack.push(2)
linkstack.push(3)
linkstack.push(51)
linkstack.push(29)

print("peek:",linkstack.peek())
stacklist=linkstack.to_list()
print(stacklist)

linkstack.push(93)
linkstack.push(229)

print("peek:",linkstack.peek())
stacklist=linkstack.to_list()
print(stacklist)

print("pop:",linkstack.pop())
linkstack.push(1000)
stacklist=linkstack.to_list()
print(stacklist)

# ArrayStack test
print("======ArrayStack=======")
linkstack= LinkedListStack.ArrayStack()
linkstack.push(1)
linkstack.push(2)
linkstack.push(3)
linkstack.push(51)
linkstack.push(29)

print("peek:",linkstack.peek())
stacklist=linkstack.to_list()
print(stacklist)

linkstack.push(93)
linkstack.push(229)

print("peek:",linkstack.peek())
stacklist=linkstack.to_list()
print(stacklist)

print("pop:",linkstack.pop())
linkstack.push(1000)
stacklist=linkstack.to_list()
print(stacklist)