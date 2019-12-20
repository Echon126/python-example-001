import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# 使用numpy产生数据
x = np.arange(-5, 5, 0.1)
y = x * 3

# 创建窗口、子图
# 方法1：先创建窗口，再创建子图。（一定绘制）
fig = plt.figure(num=1, figsize=(15, 8), dpi=80)  # 开启一个窗口，同时设置大小，分辨率
ax1 = fig.add_subplot(2, 1, 1)  # 通过fig添加子图，参数：行数，列数，第几个。
ax2 = fig.add_subplot(2, 1, 2)  # 通过fig添加子图，参数：行数，列数，第几个。
print(fig, ax1, ax2)
# 方法2：一次性创建窗口和多个子图。（空白不绘制）
fig, axarr = plt.subplots(4, 1)  # 开一个新窗口，并添加4个子图，返回子图数组
ax1 = axarr[0]  # 通过子图数组获取一个子图
print(fig, ax1)
# 方法3：一次性创建窗口和一个子图。（空白不绘制）
ax1 = plt.subplot(1, 1, 1, facecolor='white')  # 开一个新窗口，创建1个子图。facecolor设置背景颜色
print(ax1)
# 获取对窗口的引用，适用于上面三种方法
# fig = plt.gcf()   #获得当前figure
# fig=ax1.figure   #获得指定子图所属窗口

# fig.subplots_adjust(left=0)                         #设置窗口左内边距为0，即左边留白为0。

# 设置子图的基本元素
ax1.set_title('python-drawing')  # 设置图体，plt.title
ax1.set_xlabel('x-name')  # 设置x轴名称,plt.xlabel
ax1.set_ylabel('y-name')  # 设置y轴名称,plt.ylabel
plt.axis([-6, 6, -10, 10])  # 设置横纵坐标轴范围，这个在子图中被分解为下面两个函数
ax1.set_xlim(-5, 5)  # 设置横轴范围，会覆盖上面的横坐标,plt.xlim
ax1.set_ylim(-10, 10)  # 设置纵轴范围，会覆盖上面的纵坐标,plt.ylim

xmajorLocator = MultipleLocator(2)  # 定义横向主刻度标签的刻度差为2的倍数。就是隔几个刻度才显示一个标签文本
ymajorLocator = MultipleLocator(3)  # 定义纵向主刻度标签的刻度差为3的倍数。就是隔几个刻度才显示一个标签文本

ax1.xaxis.set_major_locator(xmajorLocator)  # x轴 应用定义的横向主刻度格式。如果不应用将采用默认刻度格式
ax1.yaxis.set_major_locator(ymajorLocator)  # y轴 应用定义的纵向主刻度格式。如果不应用将采用默认刻度格式

ax1.xaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
ax1.yaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式

ax1.set_xticks([])  # 去除坐标轴刻度
ax1.set_xticks((-5, -3, -1, 1, 3, 5))  # 设置坐标轴刻度
ax1.set_xticklabels(labels=['x1', 'x2', 'x3', 'x4', 'x5'], rotation=-30,
                    fontsize='small')  # 设置刻度的显示文本，rotation旋转角度，fontsize字体大小

plot1 = ax1.plot(x, y, marker='o', color='g', label='legend1')  # 点图：marker图标
plot2 = ax1.plot(x, y, linestyle='--', alpha=0.5, color='r',
                 label='legend2')  # 线图：linestyle线性，alpha透明度，color颜色，label图例文本

ax1.legend(loc='upper left')  # 显示图例,plt.legend()
ax1.text(2.8, 7, r'y=3*x')  # 指定位置显示文字,plt.text()
ax1.annotate('important point', xy=(2, 6), xytext=(3, 1.5),  # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
# 显示网格。which参数的值为major(只绘制大刻度)、minor(只绘制小刻度)、both，默认值为major。axis为'x','y','both'
ax1.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)

axes1 = plt.axes([.2, .3, .1, .1], facecolor='y')  # 在当前窗口添加一个子图，rect=[左, 下, 宽, 高]，是使用的绝对布局，不和以存在窗口挤占空间
axes1.plot(x, y)  # 在子图上画图
plt.savefig('aa.jpg', dpi=400, bbox_inches='tight')  # savefig保存图片，dpi分辨率，bbox_inches子图周边白色空间的大小
plt.show()  # 打开窗口，对于方法1创建在窗口一定绘制，对于方法2方法3创建的窗口，若坐标系全部空白，则不绘制

fig = plt.figure(2)  # 新开一个窗口
ax1 = fig.add_subplot(1, 2, 1, polar=True)  # 启动一个极坐标子图
theta = np.arange(0, 2 * np.pi, 0.02)  # 角度数列值
ax1.plot(theta, 2 * np.ones_like(theta), lw=2)  # 画图，参数：角度，半径，lw线宽
ax1.plot(theta, theta / 6, linestyle='--', lw=2)  # 画图，参数：角度，半径，linestyle样式，lw线宽

ax2 = fig.add_subplot(1, 2, 2, polar=True)  # 启动一个极坐标子图
ax2.plot(theta, np.cos(5 * theta), linestyle='--', lw=2)
ax2.plot(theta, 2 * np.cos(4 * theta), lw=2)

ax2.set_rgrids(np.arange(0.2, 2, 0.2), angle=45)  # 距离网格轴，轴线刻度和显示位置
ax2.set_thetagrids([0, 45, 90])  # 角度网格轴，范围0-360度

plt.show()

plt.figure(3)
x_index = np.arange(5)  # 柱的索引
x_data = ('A', 'B', 'C', 'D', 'E')
y1_data = (20, 35, 30, 35, 27)
y2_data = (25, 32, 34, 20, 25)
bar_width = 0.35  # 定义一个数字代表每个独立柱的宽度

rects1 = plt.bar(x_index, y1_data, width=bar_width, alpha=0.4, color='b', label='legend1')  # 参数：左偏移、高度、柱宽、透明度、颜色、图例
rects2 = plt.bar(x_index + bar_width, y2_data, width=bar_width, alpha=0.5, color='r',
                 label='legend2')  # 参数：左偏移、高度、柱宽、透明度、颜色、图例
# 关于左偏移，不用关心每根柱的中心不中心，因为只要把刻度线设置在柱的中间就可以了
plt.xticks(x_index + bar_width / 2, x_data)  # x轴刻度线
plt.legend()  # 显示图例
plt.tight_layout()  # 自动控制图像外部边缘，此方法不能够很好的控制图像间的间隔
plt.show()

fig = plt.figure(4)  # 添加一个窗口
ax = fig.add_subplot(1, 1, 1)  # 在窗口上添加一个子图
x = np.random.random(100)  # 产生随机数组
y = np.random.random(100)  # 产生随机数组
ax.scatter(x, y, s=x * 1000, c='y', marker=(5, 1), alpha=0.5, lw=2,
           facecolors='none')  # x横坐标，y纵坐标，s图像大小，c颜色，marker图片，lw图像边框宽度
plt.show()  # 所有窗口运行
