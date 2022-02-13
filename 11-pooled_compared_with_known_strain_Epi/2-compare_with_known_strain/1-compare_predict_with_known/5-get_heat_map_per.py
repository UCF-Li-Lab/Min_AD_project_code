import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
def get_map(file1,file2,title_name):

    df1 = pd.read_csv(file1,index_col=0,sep='\t')
    print(df1)
    data = df1.to_numpy()

    fig, ax = plt.subplots(figsize=(10, 9))
    im = ax.imshow(data)

    # We want to show all ticks...
    ax.set_yticks(np.arange(len(df1.index.to_list())))
    ax.set_xticks(np.arange(len(df1.columns.to_list())))
    # ... and label them with the respective list entries
    ax.set_yticklabels(df1.index.to_list())
    ax.set_xticklabels(df1.columns.to_list())

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(df1.index.to_list())):
        for j in range(len(df1.columns.to_list())):
            text = ax.text(j, i, data[i, j],
                           ha="center", va="center", color="w")

        # Create colorbar
    # divider = make_axes_locatable(ax)
    # cax = divider.new_vertical(size='30%', pad=0.1)
    # fig.add_axes(cax)
    # fig.colorbar(im, cax=cax, orientation='horizontal')
    cbar = ax.figure.colorbar(im, ax=ax,orientation = 'horizontal', pad = 0.3)
    # cbarlabel = 'shared SNPs'
    # cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    # cbar.ax.set_ylabel(cbarlabel, rotation=0, va="auto",labelpad=-40, y=0.45)
    # cbar.ax.set_ylabel(cbarlabel, rotation=0, labelpad = 0.45, y=0.45)
    ax.set_title(title_name)

    # Turn spines off and create white grid.


    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=1.5)
    ax.tick_params(which="minor", bottom=False, left=False)

    fig.tight_layout()
    # fig.savefig(file2,bbox_inches='tight')
    fig.savefig(file2)


input_path = '/media/saidi/Elements/Project/Project_for_Min/Min_AD_pooled_analysis/ADMixtureSResults_6Sept2021/Epi_compared_with_known_strain/prediction_compared_with_known_snps'
files = os.listdir(input_path)

for file in files:
    f1 = input_path + '/' + file + '/predicted_strain_per_common_heatmap.bed'
    f2 = input_path + '/' + file + '/predicted_strain_per_common_heatmap.png'

    get_map(f1,f2, file + ' common (%)')