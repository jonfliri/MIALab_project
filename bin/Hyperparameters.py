import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator

x = [0 ,1, 2, 5, 10, 20, 50, 100, 200]
D = [0, 0.45, 0.55, 0.625, 0.675, 0.7, 0.71, 0.715, 0.716]
H = [20 ,17, 13, 10, 8, 7, 6.8, 6.78, 6.77]


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('# Estimators')
ax1.set_ylabel('Dice', color=color)
plt.ylim(0, 1)
ax1.plot(x,D, marker = 'o', color = 'r')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Hausdorff distance', color=color)  # we already handled the x-label with ax1
ax2.plot(x,H, marker = '^', color = 'b')
ax2.tick_params(axis='y', labelcolor=color)

plt.grid(color = 'k', linewidth = 0.1, axis='both')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()