import matplotlib.pyplot as plt
import numpy as np
n= np.linspace(0,100,100)
y=10000*(1 + 0.05/n)**(n*10)
plt.plot(n,y)
plt.title('Amount vs n')
plt.xlabel('n')
plt.ylabel('Amount')
plt.show()