# 队列的实现
# 使用list实现队列：
# head：list最后一个元素，出队(pop)的位置，使用list.pop实现
# tail：list第一个元素，入队(push)的位置，使用list.insert实现
class Queue:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

if __name__=="__main__":
    queue=Queue()
    queue.push('first')
    queue.push('second')
    queue.push('third')
    queue.push('forth')
    print(queue.size())
    print(queue.items)
    print(queue.pop())
    print(queue.items)
    print(queue.pop())
    print(queue.items)
    print(queue.size())