class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None

    def say(self):
        print("value:"+self.val, "addr:"+self.next)

# 链表实现stack
# 栈顶在头节点：peak:n5->n4->n3->n2->n1
# 这样有利于pop操作
class LinkedListStack:
    def __init__(self):
        self.__peek: ListNode | None = None
        self.__size: int = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return not self.__size

    def push(self, val: int):
        node = ListNode(val)
        node.next = self.__peek
        self.__peek = node
        self.__size += 1

    def peek(self) -> int:
        if not self.__peek:
            return None
        return self.__peek.val

    def pop(self) -> int:
        num: int = self.peek()
        self.__peek = self.__peek.next
        self.__size -= 1
        return num
# 栈顶在链表的顶部，输出list时，需要反向一次，list顺序才是正确的。
    def to_list(self) -> list[int]:
        arr = []
        node = self.__peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr

# 数组实现stack
class ArrayStack:
    def __init__(self):
        self.__stack:list[int]=[]

    def size(self)->int:
        return len(self.__stack)

    def is_empty(self)->bool:
        return self.__stack==[]

    def push(self,val:int):
        self.__stack.append(val)

    def peek(self)->int:
        if self.is_empty():
            raise IndexError("empty")
        return self.__stack[-1]

    def pop(self)->int:
        if self.is_empty():
            raise IndexError("empty")
        return self.__stack.pop()

    def to_list(self)->list[int]:
        return self.__stack