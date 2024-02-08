# 队列的实现
# 使用list实现队列：
# head：list最后一个元素，出队(pop)的位置，使用list.pop实现
# tail：list第一个元素，入队(push)的位置，使用list.insert实现
class DoubleQueue:
    def __init__(self):
        self.items=[]

    def push_tail(self, item):
        self.items.insert(0,item)

    def pop_tail(self):
        return self.items.pop(0)

    def push_head(self,item):
        self.items.append(item)
    def pop_head(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

if __name__=="__main__":
    queue=DoubleQueue()
    queue.push_tail('first')
    queue.push_tail('second')
    queue.push_tail('third')
    queue.push_tail('forth')
    print(queue.size())
    print(queue.items)
    print(queue.pop_head())
    print(queue.items)
    queue.push_tail("five")
    print(queue.items)
    print(queue.pop_tail())
    print(queue.items)
    queue.push_head("zero")
    print(queue.items)
    print(queue.size())
    print(queue.is_empty())