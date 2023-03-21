'''
Created on Nov 5, 2020

@author: Sam Vatany
@author: Davis Edwards
@author: Josh Edmonson
'''

import numpy as np
from sklearn.cluster import DBSCAN 
from sklearn import metrics
import pylab
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt
import time
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

def _DBSCAN():
    # store all pairs of values in 2D array
    dataSet = []
    filename = input("Enter File Name: ")
    with open(filename, "rb") as file1:
        for i in range(0, 4, 1):
            file1.readline()
        values = file1.read().split()
        for i in range(0, len(values), 2):
            dataSet.append([int(values[i]), int(values[i+1])])
    
    # plot distances to find best epsilon value (sharpest part of the curve)
    neighbor = NearestNeighbors(n_neighbors=2)
    neightborFit = neighbor.fit(dataSet)
    distances, indices = neightborFit.kneighbors(dataSet)
    distances = np.sort(distances, axis=0)
    distances = distances[:,1]
    plt.title('Data Points vs Distance From Neighbor')
    plt.plot(distances)
    pylab.show() 

    # apply DBSCAN algorithm
    val = float(input("Enter Epsilon Value: "))
    starttime = time.perf_counter()
    dbscan = DBSCAN(eps=val, min_samples=4)
    
    #fit the model
    model = dbscan.fit(dataSet)
    labels = model.labels_   
    
    # identify points which make up core points
    sampleCores = np.zeros_like(labels, dtype=bool)
    sampleCores[dbscan.core_sample_indices_] = True
    
    # create cluster
    X, labels_true = make_blobs(n_samples=len(dataSet), centers=dataSet, cluster_std=0.4,
                            random_state=0)
    X = StandardScaler().fit_transform(X)  
    unique_labels = set(labels)
    colors = [plt.get_cmap('Spectral')
          for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]

    class_member_mask = (labels == k)
    xy = X[class_member_mask & sampleCores]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)
    xy = X[class_member_mask & ~sampleCores]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)
    plt.title('Data Set Cluster')
    plt.show()
    
    numClusters = len(set(labels)) - (1 if -1 in labels else 0)
    endtime = time.perf_counter()
    
    #Display results
    print("Number of Clusters: " + str(numClusters))
    print("Algorithm Running Time: " + str(endtime - starttime))
    print("Silhouette Score: " + str(metrics.silhouette_score(dataSet, labels)))
    print("Davies Bouldin Score: " + str(metrics.davies_bouldin_score(dataSet, labels)))
    return 
        
_DBSCAN()