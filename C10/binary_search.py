# 二分查找，左右双闭方式
def binary_search(nums: list[int], num: int):
    left_index, right_index = 0, len(nums) - 1
    # 必须是<=，否则无法查找到最左、右侧的元素
    while left_index <= right_index:
        # 每次循环，均先调整左右边界的列表下标，然后计算中间值下标
        print('在[{}]至[{}]中查找'.format(left_index,right_index))
        m = (left_index + right_index) // 2
        # 每次必须调整左、右侧下标，且不能包含原中间元素
        if nums[m] < num:
            left_index = m + 1
        elif nums[m] > num:
            right_index = m - 1
        else:
            return m
    return -1


if __name__ == "__main__":
    nums = [0] * 100
    # 创建一个列表，包含100个奇数
    for i in range(len(nums)):
        nums[i] = i * 2 + 1
    print(nums)

    num = 555
    index = binary_search(nums, num)
    print("{}的下标为{}".format(num, index))
