class MyList:
    def __init__(self):
        self.__capacity=10
        self.__nums=[0]*self.__capacity
        self.__size=0
        self.__extend_ratio=2

    def size(self):
        return self.__size

    def capacity(self):
        return self.__capacity

    def get(self,index):
        if index<0 or index>self.__size:
            raise IndexError("越界")
        return self.__nums[index]

    def set(self,num,index):
        if index<0 or index>self.__size:
            raise IndexError("越界")
        self.__nums[index]=num

    def extend_capacity(self):
        self.__nums+=[0]*self.__capacity*(self.__extend_ratio-1)
        self.__capacity=len(self.__nums)

    def add(self,num):
        if self.__size==self.__capacity:
            self.extend_capacity()
        self.__nums[self.__size]=num
        self.__size+=1

    def insert(self,num,index):
        if index<0 or index> self.__size:
            raise IndexError("越界")
        if self.__size==self.__capacity:
            self.extend_capacity()
# size-1：最后一个元素；index-1：倒序生成index比index大1，需要-1，才能定位到index
        for j in range(self.__size-1,index-1,-1):
            self.__nums[j+1]=self.__nums[j]
        self.__nums[index]=num
        self.__size+=1

    def remove(self,index):
        if index<0 or index> self.__size:
            raise IndexError("越界")
        for i in range(index,self.__size):
            self.__nums[i]=self.__nums[i+1]
        self.__size-=1

    def to_array(self):
        return self.__nums[:self.__size]

#test
mylist=MyList()
for i in range(31,2,-1):
    mylist.add(i)

print(mylist.to_array())
mylist.add(10)
print(mylist.to_array())
mylist.set(11,2)
print(mylist.to_array())
mylist.insert(120,2)
print(mylist.to_array())
mylist.insert(121,2)
print(mylist.to_array())
mylist.remove(1)
print(mylist.to_array())
mylist.insert(131,9)
print(mylist.to_array())
print(mylist.capacity())
print(mylist.size())