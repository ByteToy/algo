# numpy学习
import numpy as np
import os

if __name__ == "__main__":
    # 1. 由列表创建数组
    arr_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr_list2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    print(arr_list1)
    x1 = np.array(arr_list1)
    print(x1)
    x1 = np.array(arr_list2, dtype=int)
    print(x1)
    # 需要用[]，表明是一个参数
    x1 = np.array([arr_list1, arr_list2], dtype=int)
    print(x1)

    # 2. 从头创建数组
    x2 = np.zeros((3, 4), dtype=float)
    print(x2)
    x2 = np.ones((2, 4), dtype=int)
    print(x2)
    x2 = np.full((3, 5), 9.9, dtype=float)
    print(x2)

    # 3. 创建序列数组
    # 从start到end创建序列，注意不包含end点
    x3 = np.arange(1, 10, 2, dtype=int)
    print(x3)
    # 等差数列
    x3 = np.linspace(1, 100, 100, dtype=int)
    print(x3)
    # 等比数列
    x3 = np.logspace(1, 100, 50)
    print(x3)
    # 随机
    x3 = np.random.random((3, 3))
    print(x3)
    x3 = np.random.randint(1, 10, (3, 4))
    print(x3)

    # 4. 数组的性质
    x4 = np.random.randint(1, 50, (5, 8))
    print(x4)
    print('x4数组的形状', x4.shape)
    print('x4数组的维度', x4.ndim)
    print('x4数组的类型', x4.dtype)

    # 5. 数组的索引
    x5 = np.random.randint(1, 40, (6, 7))
    print(x5)
    print('x5二维数组获取一行', x5[1])
    print('x5二维数组获取一列', x5[:, 1])
    print('x5指定位置：', x5[1][2])
    print('x5指定位置：', x5[1, 2])

    # 6.数组切片
    # 一维数组切片
    x6 = np.random.randint(1, 30, 15)
    print(x6)
    # 包含起点，不包含终点
    print('截取一段', x6[5:12])
    print('截取至倒数第三个元素', x6[:-2])
    # 注意是2个:
    print('反向输出', x6[::-1])

    # 二维数组切片
    os.system('cls')
    x6 = np.random.randint(1, 30, (4, 5))
    print(x6)
    # 不包含终点（第二行，第三列）
    print('截取一段', x6[:2, :3])
    # 可以理解为先按行反向，然后再按列反向（与转置是不同的)
    print('反向输出',x6[::-1,::-1])
    # 3为步长
    print(x6[:1,0:5:3])
    # 也可以写为：x6[1]
    print("获取一行：",x6[1,:])
    print('获取一列：',x6[:,2])

    # 视图与copy的区别
    # 视图修改，原数组也修改
    x7=x6[:2,:2]
    x7[0,0]=35
    print(x6)
    print(x7)

    # 使用copy方法，返回副本，不影响原数组
    x7=x6[:2,:3].copy()
    x7[0,0]=38
    print(x6)
    print(x7)

    # 7. 数组变形
    os.system('cls')
    # 注意写法：(12,)表明是一个一维数组；(12,1)是一个2维数组，12×1
    x7=np.random.randint(1,20,(12,))
    print(x7)
    print(x7.shape)
    # 维度转换，必须元素的长度是一致的。1×23=3×4
    x8=x7.reshape(3,4)
    print(x8)
    # reshap生成的是视图，修改数组内容，影响原数组
    x8[1,1]=100
    print(x7)
    print(x8)

    # 多维数组转为一维数组
    os.system('cls')
    x7=np.random.randint(1,30,(3,4))
    print(x7)
    # flatten：返回副本
    x8=x7.flatten()
    print(x8)
    # ravel：返回视图
    x9=x7.ravel()
    print(x9)
    # reshape：返回视图
    x10=x7.reshape(-1)
    print(x10)

    # 8. 数组拼接
    os.system('cls')
    x8=np.random.randint(1,20,(2,3))
    print(x8)
    x9=np.random.randint(30,50,(2,3))
    print(x9)
    # 水平拼接，np.hstack
    # 注意参数写法[arr1,arr2]
    x10=np.hstack([x8,x9])
    print(x10)
    # 水平拼接,np.c_
    # 注意参数写法
    x11=np.c_[x8,x9]
    print(x11)

    # 垂直拼接
    x12=np.vstack([x8,x9])
    print(x12)
    x13=np.r_[x8,x9]
    print(x13)

    # 9. 数组分裂
    os.system('cls')
    x9=np.random.randint(1,30,20)
    print(x9)
    # 不包含终点，即可以理解为下一个的起点
    # 注意索引参数的用法[]
    x10,x11,x12=np.split(x9,[5,12])
    print(x10,x11,x12)

    # 二维数组分裂
    os.system('cls')
    x10=x9.reshape(4,5)
    print(x10)

    # 按行分裂
    # 注split和vsplit相同
    x11,x12,x13=np.vsplit(x10,[2,3])
    print(x11,'\n',x12,'\n',x13)

    # 按列分裂
    x11,x12,x13=np.hsplit(x10,[2,3])
    print(x11, '\n', x12, '\n', x13)

    # 10. 运算
    # 向量化运算
    os.system('cls')
    x10=np.arange(1,10)
    print(x10)
    x11=np.arange(11,20)
    print(x11)
    # 内部元素对应位置的+，-，×，/
    print(x10+5)
    print(x10+x11)
    print(x10*x11)
    # numpy内部函数：sin,cos,tan,log,log2,log10等，返回一个数组。
    print(np.sin(x10))
    print(np.log(x11))

    # 矩阵运算
    os.system('cls')
    x10=np.arange(1,10).reshape(3,3)
    x11=np.arange(11,20).reshape(3,3)
    print(x10)
    # 矩阵转置
    print(x10.T)
    # 矩阵乘法
    print(x10.dot(x11))
    print(np.dot(x10,x11))

    #比较运算
    os.system('cls')
    x10=np.random.randint(1,100,(10,10))
    print(x10)
    # 返回一个10×10数组，填充false、ture，大于50为true，其他填充为false
    print(x10>50)
    # 统计大于50的个数
    print(np.sum(x10>50))
    # 多条件判断50< <80
    print(np.sum((x10 > 50) & (x10 < 80)))
    # 判断元素是否全部大于0
    print(np.all(x10>0))
    # 判断按行是否全部大于50；axis为轴，1行，0列
    print(np.all(x10>50,axis=1))
    # 掩码运算：获取大于50的元素
    # x10>50返回false，true数组
    # x10[]从数组中获取为True的元素
    print(x10[x10>50])

    # 花哨的索引
    # 一维数组
    os.system('cls')
    x11=np.random.randint(1,100,10)
    print(x11)
    # 定义一个索引数组
    ind=[1,5,9]
    # 根据索引数组，返回数组内容
    print(x11[ind])
    # 根据索引，生成二维数组
    ind=[[2,4],[3,1]]
    print(x11[ind])

    # 二维数组
    os.system('cls')
    x11 = np.random.randint(1, 100, (5, 5))
    print(x11)
    # 定义行、列索引
    row=np.array([0,2,4])
    col=np.array([1,3,0])
    x12=x11[row,col]
    print(x12)

    # 12. 其他函数
    os.system('cls')
    x12=np.random.randint(1,100,15)
    print(x12)
    # np.sort排序，原数组不变，生成一个新数组
    print(np.sort(x12))
    print(x12)
    # 替换原数组，为生成排序变化后的数组
    x12.sort()
    print(x12)
    # 最大、小值元素
    print(np.max(x12),np.min(x12))
    # 最大、小值元素的索引
    print(np.argmax(x12),np.argmin(x12))
    print(np.sum(x12))

    # 多维数组
    os.system('cls')
    x12=np.random.randint(1,100,(4,4))
    print(x12)
    print(np.sum(x12))
    # 按行求和，轴=1
    print(np.sum(x12,axis=1))