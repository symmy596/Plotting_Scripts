import matplotlib.pyplot as lt
import numpy as np


width = 0.2
Ce = np.array([-217.64, -83.94, -138.93, -258.911])
Sm = np.array([-201.58, -79.64, -122.77,  -278.01])
Gd = np.array([-189.77, -78.59, -118.38,  -274.04,])
Y = np.array([-181.33,  -78.34, -114.30,  -270.75])
x = np.array([1, 2, 3, 4])

fig, ax = plt.subplots()

ax.set_ylabel("Y label", fontsize=13,fontweight="bold")
ax.set_xticks(x + 0.1)

ax.set_xticklabels(("A", "B", "C", "D"), fontsize=13, fontweight="bold")
ax.tick_params(axis="x", labeltop=True, labelbottom=False, top=True, bottom=False)
ax.tick_params(axis="y", labelsize=12)

First = ax.bar(x - width, Ce, width, color="black", label="W")
Second = ax.bar(x, Sm, width, color="red", label="X")
Third = ax.bar(x + width, Gd, width, color="darkblue", label="Y")
Third = ax.bar(x + (width * 2), Y, width, color="darkgreen", label="Z")

ax.legend(frameon=False, loc=3, ncol=2)
plt.tight_layout()
plt.show()
