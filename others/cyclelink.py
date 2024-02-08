class LinkNode:
    def __init__(self, val):
        self.item = val
        self.next = None

class CycleLinkList:
    def __init__(self):
        self.__head: LinkNode = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        # 这里count的从1开始，注意while循环的终止条件，此时cur到最后一个元素即跳出循环，而count没有即会+1
        count = 1
        # 游标又回到头部节点，即链表遍历完毕，返回链表长度
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            print("linklist id empty")
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        # 此时cur位于最后一个节点，他的next指向__head，但是在while循环中并未打印
        print(cur.item)

    def search(self,val):
        if self.is_empty():
            return False
        cur=self.__head
        while cur.next!=self.__head:
            if cur.item==val:
                return True
            cur=cur.next

        if cur.item==val:
            return True
        return False

    def addHead(self, val):
        node = LinkNode(val)
        # 链表为空，head指向node，同时node指向自己
        if self.is_empty():
            self.__head = node
            node.next = node

        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        # 下面两个顺序没有先后
        cur.next = node
        self.__head = node

    def addTail(self,val):
        node=LinkNode(val)
        if self.is_empty():
            self.__head=node
            node.next=node

        cur=self.__head
        while cur.next!=self.__head:
            cur=cur.next
        # node节点链接首尾，head位置不变，这里与在头部插入不同
        cur.next=node
        node.next=self.__head

    def insert(self,pos,val):
        if pos<=0:
            self.addHead(val)
        elif pos>=self.length():
            self.addTail(val)
        else:
            node = LinkNode(val)
            cur=self.__head
            count=0
            while count<(pos-1):
                count+=1
                cur=cur.next
            node.next=cur.next
            cur.next=node

    def remove(self,val):
        cur=self.__head
        pre=None
        if self.is_empty():
            return False
        while cur.next!=self.__head:
            if cur.item==val:
                # 如果需要删除的元素是在头部，则需要再定义一个游标变量rear，循环至尾部，然后让head指向下一个元素，让
                if cur==self.__head:
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    # 由于头部节点已经删除，需要将head向后移动一位，并将尾部（rear）指向新的头部
                    self.__head=cur.next
                    rear.next=self.__head
                else:
                    pre.next=cur.next
                return True
            else:
                pre=cur
                cur=cur.next

        # 跳出循环后，cur位于链表尾部，开始比较尾部是否为要删除数据
        if cur.item==val:
            # 判断链表是否只有一个元素，即cur==__head
            if cur==self.__head:
                self.__head=None
            else:
                pre.next=cur.next
            return True
        # 没有找到元素，返回False
        return False


if __name__ == "__main__":
    cyclelist = CycleLinkList()
    print(cyclelist.is_empty())
    cyclelist.addHead("one")
    cyclelist.addHead("two")
    cyclelist.addHead("three")
    cyclelist.travel()
    print(cyclelist.length())
    # print(cyclelist.is_empty())
    cyclelist.addTail("zero")
    cyclelist.travel()
    print(cyclelist.length())
    cyclelist.insert(1,"1")
    cyclelist.travel()
    print(cyclelist.length())
    print(cyclelist.remove("zero"))
    cyclelist.travel()
    print(cyclelist.length())
    print(cyclelist.search("12"))

