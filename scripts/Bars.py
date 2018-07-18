import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from pylab import *

fig, ax = plt.subplots()
fontsize = 10
rc('axes', linewidth=2)

y = np.array([2.613240418, 2.116402116, 2.402957486, 1.849217639, 2.444987775, 1.866251944]) 
x = np.array([1, 2, 3, 4, 5, 6])
index = np.array(['darkblue', 'darkblue', 'red', 'red', 'darkgreen', 'darkgreen​'])
ax.set_xticks(x)
ax.set_xticklabels(index)

ax.axvspan(0.6, 2.4, alpha=0.4, color='blue')
ax.axvspan(2.6, 4.4, alpha=0.4, color='red')
ax.axvspan(4.6, 6.4, alpha=0.4, color='green')

ax.text(0.73, 2.8, "n11 Series", color="black", fontsize=15)
ax.text(2.72, 2.8, "n10 Series", color="black", fontsize=15)
ax.text(4.72, 2.8, "nn1 Series", color="black", fontsize=15)

ax.set_ylim(0.0 ,3.2)
ax.set_ylabel('Y Label', fontsize=12, fontweight='bold')
ax.set_xlabel('X Label', fontsize=12, fontweight='bold')

ax.bar(x, y, color=('darkblue', 'darkblue', 'red', 'red', 'darkgreen', 'darkgreen'))
ax.tick_params(labelsize=11)

plt.savefig("pseudo.png", dpi=600)
plt.show()
