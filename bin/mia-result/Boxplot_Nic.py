import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from datetime import datetime


import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

path =
data = data = pd.read_csv(csv_file, delimiter=';')

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data)


plt.show()