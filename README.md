## 何时停止思考
这个话题很有意思，有时决策参考的角度太多，我们没办法收集全部信息再做决断，那么我们该何时停止思考，以当前信息来做决断呢？  
今天的罗振宇举了一个例子，在瓜田里有100个西瓜，你要选出最大的，条件是只能一个一个挑，没有选择的就不能再选了。科学家给出了一个方法：你先选择37个西瓜，不做选择，只记录这37个西瓜中最大的值，在后面的挑选过程中，如果遇到比这个最大值大的，你就可以做决定，停止思考，选择这个最大的西瓜。

挺有意思，那么来做实验验证一下：设定西瓜的大小是按正态分布的，均值是20斤，方差是10，通过实验模拟。
实验结果：
- 不需要37步，只需要记录17步，选到最大西瓜的期望是最大的，大概是37斤。
![](https://upload-images.jianshu.io/upload_images/6234504-3576dcdfa18c2895.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>这个是一个非常挑剔的人，必须要找到比之前都大的西瓜。实际情况是我们只需要找到比之前可能稍小一点的，也可以做决定。
- 实验结果，我们可接受的范围越大，那么我们应该记录更多步，但是我们随着可接受范围的增大，我们得到西瓜大小的期望也越小。
![](https://upload-images.jianshu.io/upload_images/6234504-1c1a86e7b3ab29de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
代码：
```
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
```
