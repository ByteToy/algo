# 荆州光睿高级中学-信息技术课程-教师：张鸿雁
# 第四单元第三小节课程演示代码
# Bottle：药水瓶
# BottleSet：生成一个药水瓶集合，其中随机设置一个瓶子有毒

import random


class Bottle:
    def __init__(self, num):
        self.num = num
        self.flag: bool = False

    def set_flag(self, flag):
        self.flag = flag

    def get_flag(self):
        return self.flag


class BottleSet:
    def __init__(self, total):
        self.total = total
        self.bottles = []
        for i in range(self.total):
            b = Bottle(i)
            self.bottles.append(b)
        index = random.randint(0, total-1)
        b = self.bottles[index]
        b.set_flag(True)

    def get_bottles(self):
        return self.bottles

    def show_bottles(self):
        for i in range(self.total):
            print("{}号瓶，毒性为{}".format(self.bottles[i].num, self.bottles[i].flag))

class Binary_search:
    def __init__(self,bottles:BottleSet):
        self.bottles=bottles.bottles
        self.b_len=len(self.bottles)
        # for i in range(self.b_len):
        #     print(self.bottles[i].num,self.bottles[i].flag)

    def search(self):
        start_index=0
        end_index=self.b_len
        print(start_index,end_index)
        while start_index<end_index:
            input("input")
            mid_index=(start_index+end_index)//2
            if self.melt(start_index,mid_index):
                print(start_index,mid_index)
                end_index=mid_index
            elif self.melt(mid_index,end_index):
                print(mid_index,end_index)
                start_index=mid_index
            else:
                return self.bottles[mid_index].num
        return -1

    def melt(self,start,end):
        for bottle in self.bottles[start:end]:
            if bottle.flag:
                return True
        return False


if __name__ == "__main__":
    bottles=BottleSet(1000)
    bottles.show_bottles()

    binary_search=Binary_search(bottles)
    print(binary_search.search())
