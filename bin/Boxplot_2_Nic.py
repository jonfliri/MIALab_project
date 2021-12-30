import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Local variables for plotting









def set_boxplot_format(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['caps'], linewidth=0)
    plt.setp(bp['medians'], color= 'red')
    plt.setp(bp['medians'], linewidth=1.5)
    plt.setp(bp['fliers'], marker='.')
    plt.setp(bp['fliers'], markerfacecolor='black')
    plt.setp(bp['fliers'], alpha=1)


def generate_boxplot(data: list, label: str, output_directory: str,
                      min_: float = None, max_: float = None):

    # Prepare the data for plotting again
    if not all([True if label in entry['data'].keys() else False for entry in data]):
        raise ValueError(f'The selected label ({label}) is not found for all experiments!')
    plot_data = [entry['data'][label] for entry in data]
    x_ticks = [entry['experiment'] for entry in data]

    # Generate the plot structure
    fig = plt.figure(figsize=(7.2, 9.6))  # figsize defaults to (width, height) = (6.4, 4.8)
    ax = fig.add_subplot(111)  # create an axes instance (nrows = ncols = index)
    bp = ax.boxplot(plot_data, widths=0.6)
    set_boxplot_format(bp, '000')

    # Set and format title, labels, and ticks
    font_dict = {'fontsize': 12, 'fontweight': 'bold'}
    ax.set_title(title, fontdict=font_dict)
    ax.set_ylabel(y_label, fontdict=font_dict)
    ax.yaxis.set_tick_params(labelsize=12)
    ax.set_xticklabels(x_ticks, fontdict=font_dict)
    # Remove frame
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Thicken frame
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)

    # Adjust min and max if provided
    if min_ is not None or max_ is not None:
        min_original, max_original = ax.get_ylim()
        min_ = min_ if min_ is not None and min_ < min_original else min_original
        max_ = max_ if max_ is not None and max_ > max_original else max_original
        ax.set_ylim(min_, max_)

    file_path = os.path.join(output_directory, f'plot_.png')
    plt.savefig(file_path)
    plt.close()


def main():





    # Read the data and prepare it for plotting


    data = pd.read_csv(
        'C:/Users/nickr/OneDrive/Dokumente/GitHub/MIALab_project/bin/mia-result/07_Boxplots/Boxplot_Data_1.csv',
        sep=';')
    print(data)
    plot_title = ('Comparison of Experiments',)
    plot_ylabels = ('Dice',)

    generate_boxplot(data, plot_title, plot_ylabels)
    plt.show()


if __name__ == '__main__':
    main()
