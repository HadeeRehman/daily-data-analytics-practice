# Plot multiple styled lines by unpacking dictionary kwargs in Matplotlib
import matplotlib.pyplot as plt

import numpy as np

x = np.array([2002, 2003, 2004, 2005])
y1 = np.array([22, 55, 33, 40])
y2 = np.array([17, 23, 28, 5])
y3 = np.array([22, 33, 11, 10])

line_style = dict( marker="s", 
                   markersize=8, 
                   markerfacecolor="#0b0c0c",
                   markeredgecolor="#fc5f1c", 
                   linestyle="dashdot", 
                    linewidth=4, 
                    )

plt.plot(x, y1, color="#fc1ca6", **line_style)
plt.plot(x, y2, color="#1cfc50", **line_style)
plt.plot(x, y3, color="#2f1cfc", **line_style)
plt.show()