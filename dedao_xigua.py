import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 20, 10 # mean and standard deviation
s = np.random.normal(mu, sigma, [1000,100])
print(s.shape)
fig, ax = plt.subplots(1)
for alpha in [0.05,0.1,0.2,0.4,0.6,0.8,1.0]:
    max_select = []
    for step in range(1,100):
        select = []
        for i in range(1000):
            max = np.array(s[i][:step]).max()
            std = np.array(s[i][:step]).std()
            find = 0
            for j in range(step,100):
                if s[i][j]>max-alpha*std:
                    select.append(s[i][j])
                    find = 1
                    break
            if find==0:
                select.append(s[i][99])
        assert len(select)==1000
        #print("取到最大西瓜",np.array(select).mean())
        step_mean = np.array(select).mean()
        max_select.append(step_mean)
    ax.plot(max_select)
ax.legend([0.05,0.1,0.2,0.4,0.6,0.8,1.0])
plt.show()
# max_select = []
# for step in range(1,100):##遍历步数
#     select = []
#     for i in range(1000):
#         max = np.array(s[i][:step]).max() ## 统计最大值
#         std = np.array(s[i][:step]).std()
#         find = 0
#         for j in range(step,100):
#             if s[i][j]>max-0.5*std:## 找到比之前最大值更大的，停止搜索
#                 select.append(s[i][j])
#                 find = 1
#                 break
#         if find==0:## 没有找到最大的，只能选最后一个
#             select.append(s[i][99])
#     assert len(select)==1000
#     #print("取到最大西瓜",np.array(select).mean())
#     step_mean = np.array(select).mean()
#     max_select.append(step_mean)
# ax.plot(max_select)
for alpha in [0.05,0.1,0.2,0.4,0.6,0.8,1.0]:
    max_select = []
    for step in range(1,100):
        select = []
        for i in range(1000):
            max = np.array(s[i][:step]).max()
            std = np.array(s[i][:step]).std()
            find = 0
            for j in range(step,100):
                if s[i][j]>max-alpha*std:
                    select.append(s[i][j])
                    find = 1
                    break
            if find==0:
                select.append(s[i][99])
        assert len(select)==1000
        #print("取到最大西瓜",np.array(select).mean())
        step_mean = np.array(select).mean()
        max_select.append(step_mean)
    ax.plot(max_select)
ax.legend([0.05,0.1,0.2,0.4,0.6,0.8,1.0])
plt.show()