class LinkNode:
    def __init__(self, val):
        self.item = val
        self.next = None


class LinkList:
    def __init__(self):
        self.__head: LinkNode = None

    def addHead(self, val):
        node = LinkNode(val)
        node.next = self.__head
        self.__head = node

    # 注意，这里的while中与traval函数不同。next为None，表明无后续节点，已经遍历到最后一个节点
    # travel函数则是判断node为None，表明本节点无数据，退出循环
    # ==比较的是值，is not None比较的是地址
    def addtail(self, val):
        node = LinkNode(val)
        if self.__head is None:
            self.__head = node
        else:
            cur: LinkNode = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def search(self, val):
        cur = self.__head
        while cur is not None:
            if cur.item == val:
                # print(cur.item,id(cur))
                return True
            cur = cur.next
        print("Not found {}".format(val))
        return False

    def find(self, pos):
        cur = self.__head
        count = 0
        if pos >= 0 and pos < self.length():
            while count < pos:
                cur = cur.next
                count += 1
            return cur.item
        else:
            return None

    def remove(self, val):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == val:
                # 判断删除的元素是否为第一个元素（head）
                if cur == self.__head:
                    print("find:{}".format(val))
                    self.__head = cur.next
                else:
                    # 如果不是第一个元素，则将上一个元素指向下下个元素
                    pre.next = cur.next
                return True
            # 一个迭代，将pre指向当前元素，cur进入下一个元素
            else:
                pre = cur
                cur = cur.next
        return False

    def insert(self, pos, val):
        if pos <= 0:
            self.addHead(val)
        elif pos >= self.length():
            self.addtail(val)
        else:
            cur = self.__head
            count = 0
            # 注意计数方式，count从0开始，即要即算到pos-1位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node = LinkNode(val)
            node.next = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end='\t')
            cur = cur.next
        print()

    def length(self):
        count = 0
        cur = self.__head
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def is_empty(self):
        return self.__head is None


if __name__ == "__main__":
    link_list = LinkList()
    print(link_list.is_empty())
    link_list.addHead('One')
    link_list.addHead('Two')
    link_list.addHead('Three')
    print(link_list.length())
    link_list.travel()
    link_list.addtail('Zero')
    print(link_list.length())
    link_list.travel()
    print(link_list.search('Zero'))
    link_list.travel()
    print(link_list.remove('Three'))
    print(link_list.length())
    print(link_list.remove('Five'))
    link_list.travel()
    link_list.insert(100, "last")
    link_list.insert(-11, "first")
    print(link_list.length())
    link_list.travel()
    link_list.insert(3, 'insert3')
    print(link_list.length())
    link_list.travel()
    # print(link_list.is_empty())
    # print(link_list.find(2))
    print(link_list.remove("last"))
    print(link_list.length())
    link_list.travel()
    print(link_list.find(3))