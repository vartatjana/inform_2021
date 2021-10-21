import numpy as np
import matplotlib.pyplot as plt
y = input()
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, eval(y))
plt.grid()
plt.show()

