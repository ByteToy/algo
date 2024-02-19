# 冒泡排序
#
def bubble_sort(nums:list[int]):
    n=len(nums)
    # 外层循环从列表尾部先开始，目的：为内层循环设置最大的范围；
    # 注意外层循环范围为：[n-1,1]，前面元素全部比较完毕，最后一个元素[0]自然是最小的，无须再比较
    for i in range(n-1,0,-1):
        # 定义一个标志变量，如果后面元素是有序的（没有元素交换操作），无须排序，直接终止
        flag = True
        # 内层循环范围：[0,n-1-1]，因为后面比较的方式是nums[j+1]，这样就可以比较到最后一个元素
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=False
        if flag:
            break

if __name__=="__main__":
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 55, 72,
            29, 45]
    bubble_sort(nums)
    print(nums)