# Import libraries
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

# Saving Boxplot
output_directory = ('C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/07_Boxplots')



#load data
data = pd.read_csv('C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/07_Boxplots/Overall_Dataset_DICE.csv', sep = ';')
print(data)



labels = ('A', 'A-PP', 'GM', 'GM-PP', 'H', 'H-PP', 'T', 'T-PP', 'WM','WM-PP')
#labels = ('1', '1-PP', '2', '2-PP', '3', '3-PP', '4', '4-PP', '5', '5-PP')
labels = ('Overall', 'Overall-PP')

Boxplot = plt.boxplot(data, labels = labels)


plt.setp(Boxplot['boxes'], color= 'black')
plt.setp(Boxplot['whiskers'], color= 'black')
plt.setp(Boxplot['caps'], color= 'black')
plt.setp(Boxplot['caps'], linewidth=1)
plt.setp(Boxplot['medians'], color= 'red')
plt.setp(Boxplot['medians'], linewidth=1)
plt.setp(Boxplot['fliers'], marker='.')
plt.setp(Boxplot['fliers'], markerfacecolor='black')
plt.setp(Boxplot['fliers'], alpha=1)
plt.grid(color = 'k', linewidth = 0.1, axis = 'y')
plt.ylabel('STD')
plt.ylim(0, .1)
plt.ylabel('Dice')
plt.ylim(0, 1)
plt.xlabel('Structure')

plt.title("Standart deviation of the different Brain structures before and after \n post-processing over all Datasets")
#plt.title("Dice of the different Datasets before and after \n Post-Processing")
plt.title("\nOverall Dice before and after post-prossesing")


#plt.show()
file_path = os.path.join(output_directory, f'Overall_Datasets_DICE.png')
plt.savefig(file_path)
plt.close()
