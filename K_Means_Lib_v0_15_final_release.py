"""
Project : Unsupervised Learning (K-means)
Engineer : Nikhil.P.Lokhande
email: nlokhande@asu.edu
"""
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import random


def assign(D, C): # assgin based on objective function
  output=[]
  for i in range(0,len(D)):
    compare_List=[]
    for j in range(0,len(C)):
      compare_List.append( pow(((D[i][0]-C[j][0])**2)+((D[i][1]-C[j][1])**2),0.5)) # objective function
    output.append(compare_List.index(min(compare_List)))

    
  return output

def find_Max(D, centroid_List): # find the maximum average distance of each point to each centroid
  
  flag = False
  output=[]
  output_List=[]
  compare_Lists=[]
  
  for j in range(0,len(D)):
    if(flag):                                 #redundant flag unused
      return D[random.randint(0,len(D)-1)]
    
    compare_List=[]

    for i in range(0,len(centroid_List)):
      if(not hasattr(centroid_List[i], "__len__")):    #check if pythonic None or non iterables are passed 
       
        flag = True
        return D[random.randint(0,len(D)-1)]   #and filter with new data point
      compare_List.append( pow(((D[j][0]-centroid_List[i][0])**2)+((D[j][1]-centroid_List[i][1])**2),0.5))
    compare_Lists.append(compare_List)  
  
    
    
  
  for i in range(len(compare_Lists)):
    output_List.append(np.sum(compare_Lists[i])/float(len(compare_Lists[i]))) #comput the average for each data point to each centroid
  
    


  centroid = D[output_List.index(max(output_List))]

  return (centroid)


def centroid(D, C): # Calculate centorid
  k = max(C)+1
  cluster_List=[]
  centroids=[]
  for i in range(0,k):
    cluster_List.append([])
    centroids.append([0,0])
  k0 = []
  k1 = []
  k2 = []
  k3 = []
  k0mx,k0my,k1mx,k1my,k2mx,k2my,k3mx,k3my =0,0,0,0,0,0,0,0 
  elements_Cluster=[]
  output = []
 

    
      
    
  for i in range(0,len(C)):
    cluster_List[C[i]].append(D[i])

      
 

  for k in range(0,len(cluster_List)): #find mean cluster
    cluster = cluster_List[k] 
    kmx,kmy=0,0
    for i in range(0,len(cluster)):
      kmx += cluster[i][0]
      kmy += cluster[i][1]
    centroids[k] = [kmx/float(len(cluster)),kmy/float(len(cluster))]  
  

    
 
  return centroids
