import numpy as np
import matplotlib.pyplot as plt
xticks = np.linspace(-10,10,num=1000)
xvalues = xticks
yvalues = np.sin(xticks)
plt.plot(xvalues, yvalues)
plt.grid(True)
plt.xlabel("pi*n", fontsize=24)
plt.ylabel("sin x", fontsize = 24)
