import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.xlabel('$x$')
plt.ylabel('$sen(x^2)$')