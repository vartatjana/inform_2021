import numpy as np
x = int(input())
a = np.e**(1/(np.sin(x)+1))
b = 5/4 + 1/(x**15)
y = np.log(a/b) / np.log(x*x+1)
print(y)
