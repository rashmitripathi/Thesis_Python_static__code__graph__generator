from pylab import *
from scipy.ndimage import measurements

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import MiniBatchKMeans, KMeans , AffinityPropagation
from collections import defaultdict
import Plotting as plot
import JSONWriter as jsonWriter
from sklearn import metrics

import validate as validate

#https://github.com/frnsys/imclus/blob/08e759137019d012245e116144b71750b7561420/cluster.py

def doCluster(r):
  #SpectralClustering(2).fit_predict(mat)
  #DBSCAN(min_samples=1).fit_predict(mat)
  pass


def doCluster1(r):
  L = 100
  #r = rand(L,L)
  p = 0.4
  z = r<p

  #print(r)

  figure(figsize=(16, 5))
  subplot(1, 3, 1)
  a=imshow(z, origin='lower', interpolation='nearest')
  colorbar()
  title("Matrix")

  # Show image of labeled clusters (shuffled)
  lw, num = measurements.label(z)
  subplot(1, 3, 2)
  b = arange(lw.max() + 1)  # create an array of values from 0 to lw.max() + 1
  shuffle(b)  # shuffle this array
  shuffledLw = b[lw]  # replace all values with values from b
  b=imshow(shuffledLw, origin='lower', interpolation='nearest')  # show image clusters as labeled by a shuffled lw
  colorbar()
  title("Labeled clusters")

  # Calculate areas
  subplot(1, 3, 3)
  area = measurements.sum(z, lw, index=arange(lw.max() + 1))
  areaImg = area[lw]
  im3 = imshow(areaImg, origin='lower', interpolation='nearest')
  colorbar()
  title("Clusters by area")

  # Bounding box
  sliced = measurements.find_objects(areaImg == areaImg.max())
  if (len(sliced) > 0):
      sliceX = sliced[0][1]
      sliceY = sliced[0][0]
      plotxlim = im3.axes.get_xlim()
      plotylim = im3.axes.get_ylim()
      plot([sliceX.start, sliceX.start, sliceX.stop, sliceX.stop, sliceX.start],
           [sliceY.start, sliceY.stop, sliceY.stop, sliceY.start, sliceY.start],
           color="red")
      xlim(plotxlim)
      ylim(plotylim)

  show()
  plt.savefig(a)
  plt.savefig(b)
  plt.savefig(im3)

def test(dirname,input):

    if(len(input) == 0):
        return
    #mat=np.matrix(input)

    #mat = np.matrix([[1., .1, .6, .4], [.1, 1., .1, .2], [.6, .1, 1., .7], [.4, .2, .7, 1.]])

    db=DBSCAN( eps=2,min_samples=10).fit_predict(input) #  with eps as 2 and min samples as 10 we are getting 15 clusters oherwise not good enough
    core_samples_mask = np.zeros_like(db, dtype=int)
    core_samples_mask[db] = True
    dbLength=len(db)
    k_means = KMeans(init='k-means++', n_clusters=10, n_init=10).fit_predict(input)
    mbk = MiniBatchKMeans(init='k-means++', n_clusters=15, batch_size=45,n_init=10, max_no_improvement=10, verbose=0).fit_predict(input)
    af = AffinityPropagation(preference=-50).fit_predict(input)

    print("K_means clustering result:",k_means)
    print("min batch:",mbk)
    print("Affinity Propagation:", af)

    jsonWriter.dumpDataFromList(input,db,"p",dirname+"dbscan")
    jsonWriter.dumpDataFromList(input, k_means, "p", dirname + "k_means")
    jsonWriter.dumpDataFromList(input, mbk, "p", dirname + "mbk")
    jsonWriter.dumpDataFromList(input, af, "p", dirname + "af")

    #1.MinBatchKMeans(Popular)
    #2.AffinityPropagation
    #3.SpectralClustering(Very Good One)
    #4.DBScan
    #5.Birch
    #6.GausianMixture(Very GoodOne)


    #### validation
    print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(input, db))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(input, k_means))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(input, mbk))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(input, af))

    validate.checkCoeffcient(input)
    labels=db

    # for i in range(0,dbLength):
    #labels.append("path"+str(i))

    clusters = defaultdict(list)
    for i, lbl in enumerate(labels):
        #clusters[lbl].append(fnames[i])
        pass


    print("clustering result using DBScan:",labels)
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)


    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

    showPlot(input)

#test()

def showPlot(input):
    plot.plotSimilarityMatrix(input)
