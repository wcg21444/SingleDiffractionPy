import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as inte

L = 10
lbd = 0.01
a = 0.1

def l(x,t):
    return 10*(lbd/x*(np.cos(t)-np.cos(t+a*(x)/(lbd*np.sqrt(x**2+L**2)))))

def integrate_x_l(x):
    def func(t):
        return l(x,t)**2
    return inte.quad(func,1,4)[0]
 
x = np.linspace(-100,100,2500)
# 计算每个x对应的y值的数量
density = np.array([integrate_x_l(val) for val in x])

# 根据密度生成x和y的点
x_samples = []
y_samples = []

# y值均匀分布
y_min, y_max = -2, 2  # y的范围

for x, count in zip(x, density):
    y_positions = np.linspace(y_min, y_max, int(count*1550000))  # 在y方向上均匀分布
    x_samples.extend([x] * len(y_positions))  # 对应的x值
    y_samples.extend(y_positions)  # y值

# 转换为numpy数组
x_samples = np.array(x_samples)
y_samples = np.array(y_samples)

bgcolor = (0.2,0.2,0.2)
# 绘制散点图
plt.figure(figsize=(10, 6),facecolor=bgcolor)
plt.scatter(x_samples, y_samples, alpha=0.02,c= (1,0.0,0.0),edgecolors=(1,0.4,0.4),s=1)

plt.gca().set_facecolor(bgcolor)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False  # 处理负号

plt.title(u'单缝衍射光子散点图',c = 'grey')
plt.xlim(-40, 40)
plt.ylim(0, 1)
plt.grid(False)
plt.show()