# Import libraries
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

# Saving Boxplot
output_directory = ('C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/Boxplots')
file_path = os.path.join(output_directory, f'plot_.png')



data_P = pd.read_csv('C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/Boxplots/Data_3.csv', sep = ';')
print(data_P)


#data = [data_1, data_2, data_3, data_4]

titel = ('Comparison')
labels = ('Amygdala', 'Amygdala-PP', 'GreyMatter', 'GreyMatter-PP', 'Thalamus', 'Thalamus-PP', 'WhiteMatter','WhiteMatter-PP')

plt.boxplot(data_P, labels = labels)

plt.show()

#plt.savefig(file_path)
