import numpy as np
import matplotlib.pyplot as plt
xticks = np.linspace(-0.3,0.3,num=10000)
xvalues = 1/xticks
yvalues = np.sin(xvalues)
plt.plot(xticks, yvalues)
plt.grid(True)
plt.xlabel("pi*n", fontsize=24)
plt.ylabel("sin x", fontsize = 24)