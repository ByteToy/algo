# 插入排序
# 取出排序后的一个元素，与前面元素相比，插入对应的位置。
def insertion_sort(nums:list[int]):
    n=len(nums)
    for i in range(n):
        # 取出排序后的第一个元素base
        base=nums[i]
        j=i-1
        # 将比自己大的元素向后移动
        while j>=0 and nums[j]>base:
            nums[j+1]=nums[j]
            j-=1
        # 注意下标j+1的含义，在while循环中j已经跑到前一个位置了
        nums[j+1]=base

if __name__=="__main__":
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 55, 72,
            29, 45]
    insertion_sort(nums)
    print(nums)