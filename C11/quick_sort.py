# 快速排序算法
# partition将列表划分为两个部分：左子列表<基数<右子列表
def partition(nums: list[int], left: int, right: int) -> int:
    i, j = left, right
    # 选定最列表最左侧元素为基数
    base = nums[left]
    while i < j:
        # 这里先从右至左寻找小于base的值，再从左至右查找大于base的值，顺序有先后
        while i < j and nums[j] >= base:
            j -= 1
        while i < j and nums[i] <= base:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    # 将基数与i互换，使得左列表<基数<右列表
    nums[left], nums[i] = nums[i], nums[left]
    return i

# 使用递归方式，不断将列表划分为更小更小的列表，直到列表只有一个元素，达到边界（终止）条件
def quick_sort(nums: list[int], left: int, right: int):
    if left >= right:
        return
    base_index = partition(nums, left, right)
    quick_sort(nums, left, base_index - 1)
    quick_sort(nums, base_index + 1, right)


if __name__ == "__main__":
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 55, 72,
            29, 45]
    # nums=[2, 4, 1, 0, 3, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
