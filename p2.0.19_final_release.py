"""
Project : Unsupervised Learning (K-means)
Engineer : Nikhil.P.Lokhande
email: nlokhande@asu.edu
"""
import K_Means_Lib_v0_15_final_release  as K_Means
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import random

  
input_File = loadmat("dcG9m8gvEemRPArJHNevzg_b3ba7dd655bd4dafb06a913ff8515732_AllSamples.mat") #input 
select_Strategy = input("Enter 1 for Strategy 1 and 2 for Strategy 2. Default 1:")
k=int(input("Enter k value:")) #k value

data_Set=input_File['AllSamples']
   
centroids=[]
centroid_Count=1 #counter for max distance based on previous data point
while(len(centroids)<k):                 #Strategy 1 
    centroid = data_Set[random.randint(0,len(data_Set)-1)]
    centroids.append(centroid)
   
if(int(select_Strategy) == 2):  #Strategy 2
    print("Using Strategy 2")
    centroids.clear()       #clear previous data
    centroids.append(data_Set[random.randint(0,len(data_Set)-1)]) #start with a random
    while(centroid_Count<k): # While centroids are not equal to k , add the  centroid of max distance from the i-1 centroid 
        centroids.append(K_Means.find_Max(data_Set,centroids))
        centroid_Count+=1 # update counter 
        
dup=True      # For Strategy 2 may be duplicates due to outliers and max distance repeating

  # Find duplicates if any till no duplicates , then get a random dp to replace the duplicate only, to meet number of k requirement
for i in range(0,len(centroids)):
    for j in range(1,len(centroids)):
        if(centroids[i][0] == centroids[j][0] and centroids[i][1] == centroids[j][1] and j!=i): # way to check duplicates by asserting the values at both dimensionss
            centroids[i]=K_Means.find_Max(data_Set,data_Set[random.randint(0,len(data_Set)-1)])
           
        
    

        
found = False # find the centroids flag
iteration= 0
while(found!= True ):
      K_assignment_List=K_Means.assign(data_Set,centroids) #assing and find centorid mean , repeat until convergence
      c=0
      for i in range(len(centroids)):

        if((len(K_Means.centroid(data_Set,K_assignment_List))!= k)): #if a cluster k is unassigned any value stop , < k(desired input)
            found=True
            break
            
        if( (centroids[i][0]) == (K_Means.centroid(data_Set,K_assignment_List)[i][0]) and (centroids[i][1]) == (K_Means.centroid(data_Set,K_assignment_List)[i][1])):
          c+=1
        if(c==len(centroids)):
          found=True
          #break
        
      iteration+=1
     
      centroids = K_Means.centroid(data_Set,K_assignment_List)

if( iteration <2 and select_Strategy): #max point repeat  message explained
    print("Stopping early as one max distance centroid was unassigned any data points due to outlier, please restart as function currently will return number of centorids < k(desired input)")
print("Centroids:")
    
print(centroids)
#print(K_Means.centroid(data_Set,K_assignment_List))
print("K_assignment_List:")

print(K_assignment_List)
#print(c)
print("Iteration:")

print(iteration)
x_List=[]
y_List=[]
for i in range(len(centroids)):
    x_List.append(centroids[i][0])
    y_List.append(centroids[i][1])
print(centroids[0])    
imgplot = plt.scatter(x_List,y_List,color = 'k')
plt.show()






