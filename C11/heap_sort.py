# 堆排序
# l:堆的长度（列表长度）
# i：堆的顶点（也可以是左右子堆的顶点，随着向下移动，顶点在向下移动）
def shift_down(nums: list[int], l: int, i: int):
    while True:
        left = i * 2 + 1
        right = i * 2 + 2
        # 最大值先指向堆顶，然后与左右子堆比较，进行堆化
        mx = i
        if left < l and nums[mx] < nums[left]:
            mx = left
        if right < l and nums[mx] < nums[right]:
            mx = right
        # 当顶点指针移动到下边叶子节点时，无左右子顶点，表示遍历完毕，跳出循环，说明向下移动全部完成，或者i顶点本身就比左右子堆节点大
        if mx == i:
            break
        nums[i], nums[mx] = nums[mx], nums[i]
        # 堆顶顶点与左右子顶点互换后，堆顶向下移动（移向左右子顶点最大的顶点）
        i = mx


def heap_sort(nums: list[int]):
    # 建堆操作
    for i in range(len(nums) // 2 - 1, -1, -1):
        shift_down(nums, len(nums), i)

    # 堆排序操作，先将列表堆顶与列表最后一个元素互换，然后对堆顶元素向下移动进行堆化
    # 注意i变量，0和i元素互换取得最大元素后，i相当于后面堆的长度
    for i in range(len(nums) - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        shift_down(nums, i, 0)


if __name__ == '__main__':
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 72,
            29, 45]
    heap_sort(nums)
    print(nums)
