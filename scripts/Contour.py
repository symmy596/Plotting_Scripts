import matplotlib.pyplot as plt
import numpy as np

X = np.arange(100)
Y = np.arange(100)
Grid = np.random.rand(100, 100)
    
X, Y = np.meshgrid(X, Y)
plt.contourf(X, Y, Grid, 25, cmap='jet', interpolation='nearest')
plt.xlabel("X label", fontsize=18)
plt.ylabel("Y label", fontsize=18)
plt.tick_params(labelsize=14)
plt.tight_layout()
plt.colorbar()
plt.savefig("Contor.png", dpi=600)
plt.show()
plt.close()
