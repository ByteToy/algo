# 归并排序

# 合并函数，对分解的列表，合并排序存储在tmp列表中，然后将列表中元素复制到nums中
def merge(nums: list[int], left, mid, right):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    # 合并左右子列表，从左端逐个比较左右列表，然后按序存入tmp列表
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    # 对左右子列表仍有元素未插入的（即大的元素，存入tmp列表尾部）
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1

    # 将临时列表数据存入nums列表中，并且保证位置（下标）对应
    for k in range(0, len(tmp)):
        nums[left + k] = tmp[k]


# 归并排序，使用递归方式，先处理左右子列表，当列表元素为1时，向上返回，然后使用合并排序函数merge进行排序
def merge_sort(nums: list[int], left, right):
    # 递归边界条件（终止）：判断列表元素是否为1
    if left >= right:
        return
    mid = (left + right) // 2
    # 分别处理左右子列表
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    # 子列表排序合并
    merge(nums, left, mid, right)


if __name__ == "__main__":
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 72,
            29, 45]
    merge_sort(nums, 0, len(nums) - 1)
    print(nums)
