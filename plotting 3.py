
import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    if n==0:
        return 1
    elif n<0:
        return 1
    else:
        return n*fact(n-1)
    
xticks = np.linspace(1,365,num=365)
xvalues = xticks
yvalues = 1-((fact(365)/(fact(365-xvalues)))/365**xvalues)
plt.plot(xticks, yvalues)
plt.grid(True)
plt.xlabel("days", fontsize=24)
plt.ylabel("ppl", fontsize = 24)