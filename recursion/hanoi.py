step = 1


def hanoi(num, src, des, tmp):
    if num <= 1:
        movSingle(src, des)
    else:
        hanoi(num - 1, src, tmp, des)
        movSingle(src, des)
        hanoi(num - 1, tmp, des, src)


def movSingle(src, des):
    global step  # 声明为global，否则cannot access local variable 'step' where it is not associated with a value
    disk = src[0].pop()
    print("第" + str(step) + "步:从" + src[1] + "柱移动" + str(disk) + "盘到" + des[1] + "柱")
    step += 1
    des[0].append(disk)


if __name__ == "__main__":
    a = ([6, 5, 4, 3, 2, 1], "A")
    b = ([], "B")
    c = ([], "C")
    hanoi(len(a[0]), a, b, c)
