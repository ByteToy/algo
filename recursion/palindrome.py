def is_pal_all(input_str):
    for i in range(len(input_str)):
        if input_str[i] != input_str[len(input_str) - 1 - i] and i <= len(input_str) - 1 - i:
            return False
        else:
            print("head[{}]={},tail[{}]={}".format(i, input_str[i], len(input_str) - 1 - i,
                                                   input_str[len(input_str) - 1 - i]))
    return True


def is_pal_half(input_str):
    for i in range(len(input_str) // 2):
        if input_str[i] == input_str[len(input_str) - 1 - i]:
            print("head[{}]={},tail[{}]={}".format(i, input_str[i], len(input_str) - 1 - i,
                                                   input_str[len(input_str) - 1 - i]))
        else:
            return False
    return True


def is_pal_recursion(input_str):
    print(input_str)
    if len(input_str) <= 1:
        return True
    else:
        return input_str[0] == input_str[-1] and is_pal_recursion(input_str[1:-1])


if __name__ == "__main__":
    # flag = is_pal_all("上海自来水来自海上")
    # flag=is_pal_half("山东落花生花落东山")

    flag = is_pal_recursion("黄山落叶松叶落山黄")
    print(flag)
