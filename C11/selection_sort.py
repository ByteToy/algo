# 选择排序算法
# 重点是注意列表下标的取值范围，两轮循环的取值最末端是不同的。
def selection_sort(nums: list[int]):
    n = len(nums)
    # n-1实际取值是n-2位置
    for i in range(n - 1):
        # k记录列表i+1至n-1之间最小数的效标
        k = i
        for j in range(i + 1, n):
            # 在i+1至n-1中发现比num[i]小的数，k记录此下标
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == "__main__":
    nums = [62, 65, 51, 15, 30, 63, 37, 8, 55, 70, 13, 84, 46, 44, 86, 11, 91, 10, 47, 3, 96, 9, 36, 54, 24, 55, 72,
            29, 45]
    selection_sort(nums)
    print(nums)
