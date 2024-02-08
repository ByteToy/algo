class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None

    def say(self):
        print("value:" + self.val, "addr:" + self.next)


# 链表队列指针结构：
# front:n5->n4->n3->n2->n1:rear
class LinkedListQueue:
    def __init__(self):
        self.__front: ListNode | None = None
        self.__rear: ListNode | None = None
        self.__size: int = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return not self.__front

    def push(self, val: int):
        node = ListNode(val)
        if self.__front is None:
            self.__front = node
            self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node
        self.__size+=1
    def pop(self) -> int:
        if self.size() == 0:
            print("queue is empty")
            return False
        else:
            num = self.__front.val
            self.__front = self.__front.next
            self.__size -= 1
            return num

    def to_list(self) -> list[int]:
        queue = []
        index = self.__front
        while index:
            queue.append(index.val)
            index = index.next
        return queue

