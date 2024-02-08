class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None
        # self.prev:Optional[ListNode]=None

    def say(self):
        print("value", "prev node", "next node")
        print(self.val, self.prev, self.next)


def insert(p: ListNode, n: ListNode):
    n.next = p.next
    p.next = n


def trasverse(head: ListNode):
    while True:
        head.say()
        if head.next != None:
            head = head.next
        else:
            break
    return


def find(head: ListNode, val: int) -> int:
    index: int = 0
    while head:
        if head.val == val:
            return index
        head = head.next
        index += 1
    return -1


# _在python中称作 丢弃变量
# _是一个合法的标识符，也可以作为一个有效的变量使用，但是定义成下划线就是希望不要被使用，除非明确的知道这个数据需要使用
def access(head: ListNode, index: int) -> ListNode | None:
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

# 遍历链表
head = n1
trasverse(head)

# 向链表插入新节点
p = ListNode(10)
insert(n3, p)
head = n1
trasverse(head)

# 查找链表
head = n1
print(find(head, 5))

# 访问列表
head = n1
access(head, 2).say()
