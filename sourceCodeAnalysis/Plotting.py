from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plotSimilarityMatrix(inputMatrix):
    sns.set(style="white")
    # Generate a large random dataset
    result = np.matrix(inputMatrix)
    d = pd.DataFrame(data=result)
    print(d)
    # Compute the correlation matrix
    corr = d
    # Generate a mask for the upper triangle
    #mask = np.zeros_like(corr, dtype=np.bool)
    #mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(25, 25))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    #heatmap = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=0, square=True)
    heatmap = sns.heatmap(corr, cmap=cmap, vmax=1, vmin=0, square=True)
    loc, labelsx = plt.xticks()
    loc, labelsy = plt.yticks()
    heatmap.set_xticklabels(labelsx, rotation=90)
    heatmap.set_yticklabels(labelsy, rotation=90)

    plt.show()
    plt.savefig('similarity.png')
    plotSimilarityMatrixTop50(inputMatrix)


def plotSimilarityMatrixTop50(inputMatrix):
 sns.set(style="white")
 # Generate a large random dataset
 result=np.matrix(inputMatrix[0:50,0:50])
 d = pd.DataFrame(data=result)
 print(d)
 #Compute the correlation matrix
 corr = d
 #print("matrix corr:",corr)
 # Generate a mask for the upper triangle
 mask = np.zeros_like(corr, dtype=np.bool)
 mask[np.triu_indices_from(mask)] = True

 # Set up the matplotlib figure
 # get the tick label font size
 #fontsize_pt = plt.rcParams['ytick.labelsize']
 #dpi = 72.27

 # comput the matrix height in points and inches
 #matrix_height_pt = fontsize_pt * result.shape[1]
 #matrix_height_in = matrix_height_pt / dpi

 # compute the required figure height
 #top_margin = 0.04  # in percentage of the figure height
 #bottom_margin = 0.04  # in percentage of the figure height
 #figure_height = matrix_height_in / (1 - top_margin - bottom_margin)

 # build the figure instance with the desired height
 #fig, ax = plt.subplots(figsize=(40, figure_height),gridspec_kw=dict(top=1 - top_margin, bottom=bottom_margin))
 f, ax = plt.subplots(figsize=(25, 25))
# Generate a custom diverging colormap
 cmap = sns.diverging_palette(220, 10, as_cmap=True)
 #cmap = sns.diverging_palette(250, 15, s=75, l=40,n=9, center="dark" as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
 #sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1,vmin=0, center=.5,square=True, linewidths=.1, cbar_kws={"shrink": .5})
 heatmap=sns.heatmap(corr,cmap=cmap,vmax=1,vmin=0,square=True)
 loc, labelsx = plt.xticks()
 loc, labelsy = plt.yticks()
 heatmap.set_xticklabels(labelsx, rotation=90)
 heatmap.set_yticklabels(labelsy, rotation=90)

 plt.show()
 plt.savefig('similarity.png')
 plotClustering(inputMatrix,None)

def plotClustering(inputMatrix,cluster):
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    g = sns.clustermap(inputMatrix, method="single",cmap=cmap)
    rotation = 90
    for i, ax in enumerate(g.fig.axes):  ## getting all axes of the fig object
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=rotation)

    #sns.set(style="white")
    plt.show()
    plt.savefig('clusterusingdendogram.png')
    plotClusteringTop40(inputMatrix,None)

def plotClusteringTop40(inputMatrix,cluster):
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    g = sns.clustermap(inputMatrix[0:40,0:40], method="single",cmap=cmap)
    rotation = 90
    for i, ax in enumerate(g.fig.axes):  ## getting all axes of the fig object
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=rotation)

    #sns.set(style="white")
    plt.show()
    plt.savefig('clusterusingdendogram.png')

mat = np.matrix([[1., .1, .6, .4], [.1, 1., .1, .2], [.6, .1, 1., .7], [.4, .2, .7, 1.]])
#plotSimilarityMatrix(mat)
#plotClustering(mat,[0,1,2,2])