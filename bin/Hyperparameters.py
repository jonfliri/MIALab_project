import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
import os

# Saving
output_directory = ('C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/09_Hyperparameter')

#Constant depth = 10
x = [0, 1, 2, 5, 10, 20, 50, 100]
D = [0, 0.598684246, 0.605940166, 0.613891804, 0.618256249, 0.618315119, 0.618264554, 0.619078745]
H = [18, 15.01647387, 13.48346507, 11.88461035, 10.70652581, 10.62143896, 10.21081322, 10.17405875]


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
plt.title('Constant tree depth = 10')
plt.grid(color = 'k', linewidth = 0.1, axis='both')

fig.tight_layout()  # otherwise the right y-label is slightly clipped


file_path = os.path.join(output_directory, f'Const_tree_depth_DICE.png')
plt.savefig(file_path)
plt.close()

#Constant Estimator = 20
x = [0, 1, 2, 5, 10, 20, 50, 100]
D = [0, 0.090607292, 0.294794457, 0.366511281, 0.618315119, 0.67789637, 0.682486692, 0.682486692]
H = [25, 25, 25, 22.8762013, 10.62143896, 9.004471228, 8.986045442, 8.986045442]


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Tree depth')
ax1.set_ylabel('Dice', color=color)
plt.ylim(0, 1)
ax1.plot(x,D, marker = 'o', color = 'r')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Hausdorff distance', color=color)  # we already handled the x-label with ax1
ax2.plot(x,H, marker = '^', color = 'b')
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Constant # of estimators = 10')
plt.grid(color = 'k', linewidth = 0.1, axis='both')

fig.tight_layout()  # otherwise the right y-label is slightly clipped


file_path = os.path.join(output_directory, f'Const_num_estimators_DICE.png')
plt.savefig(file_path)
plt.close()