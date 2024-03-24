import matplotlib.pyplot as plt

# from matplotlib.font_manager import FontManager
plt.style.use('seaborn-v0_8-darkgrid')
import numpy as np
import matplotlib

matplotlib.rc("font", family='Microsoft YaHei')


def config():
    # 获取系统字体库
    mpl_fonts = set(f.name for f in FontManager().ttflist)
    print('all font list get from matplotlib.font_manager:')
    for f in sorted(mpl_fonts):
        print('\t' + f)

    # 查看样式
    print(plt.style.available[::-1])


# 折线图基本用法
def plot_view():
    x = np.linspace(0, 2 * np.pi, 1000)
    plt.ylabel('y轴')
    plt.xlabel('x轴')
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    # plt.savefig('1.png')
    plt.show()


def multi_plot_view():
    x = np.linspace(0, 2 * np.pi, 100)
    # linspace包含起始两个点的值，然后均分5个点
    offsets = np.linspace(0, np.pi, 5)
    # print(offsets)
    # 颜色可以简写
    colors = ['blue', 'r', 'green', 'yellow', 'pink']
    linestyles = ['solid', '-', '--', '-.', 'dotted']
    linewidths = np.linspace(1, 3, 5)
    markers=['*','+','o','s','.']
    legs=['sin0','-pi/4','-pi/2','-pi3/4','-pi']

    # 设置线条的样式（颜色、样式、粗细等）
    for offset, color, ls, lw,mkr,leg in zip(offsets, colors, linestyles, linewidths,markers,legs):
        # color可以简写为c
        # linestyle可以简写为ls
        # linewidth可以简写为lw
        # color:线条颜色；linestyle：线条样式；linewidth：线条宽度；marker：标记形状
        # plt.plot(x, np.sin(x - offset), c=color, linestyle=ls, linewidth=lw,marker=mkr)
        plt.plot(x, np.sin(x - offset), c=color, linestyle=ls, linewidth=lw,label=leg)

    # 座标轴的范围
    plt.xlim(0,7)
    plt.ylim(-1.5,1.5)

    # 座标轴刻度
    plt.xticks(np.linspace(0,2*np.pi,9))
    # arange不包含终点，但是linspace包含终点
    plt.yticks(np.arange(-1.6,1.6,step=0.2))

    # 设置标签
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    plt.title('正弦函数')

    # 启用设置图例
    # loc:图例位置；frameon：True开启一个框框；fontsize：字体大小
    plt.legend(loc='upper right',frameon=True,fontsize=10)
    plt.show()

def scatter_view():
    x=np.arange(1,50,1)
    # plt.scatter(x,x**2+2*x+1)
    plt.scatter(x,np.log2(x),color='r',marker=',',label='log2')
    plt.scatter(x,np.log10(x),color='blue',linewidths=0.2,label='log10')
    plt.legend()
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.title('LOG')
    plt.show()


if __name__ == "__main__":
    # plot_view()
    # multi_plot_view()
    scatter_view()
