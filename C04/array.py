import random

arr:list[int]=[0]*5
nums:list[int]=[1,2,3,4,5,6,7]

def access_random(nums:list[int])->int:
    random_index=random.randint(0,len(nums)-1)
    random_num=nums[random_index]
    return random_num

def extend(nums:list[int],enlarge:int)->list[int]:
    res=[0]*(len(nums)+enlarge)
    for i in range(len(nums)):
        res[i]=nums[i]
    return res

def insert(nums:list[int],num:int,index:int):
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    nums[index]=num

def remove(nums:list[int],index:int):
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]
    nums[i+1]=0

def find(nums:list[int],num:int)->int:
    for i in range(len(nums)-1):
        if num==nums[i]:
            return i
    return -1

print(nums)
print(access_random(nums))
print(extend(nums,10))
insert(nums,8,2)
print(nums)
remove(nums,3)
print(nums)
print(find(nums,9))