This folder contains implementation of ISOMAP algorithm from the scratch.  

The file isomap.mat (or isomap.dat) contains 698 images, corresponding to different poses of the same face. Each image is given as a 64 x 64 luminosity map, hence represented as a vector in R4096. This vector
is stored as a row in the file.  

I have constructed an ISOMAP using Euclidean distance and Manhattan distance metrics. Finally, the results of ISOMAP are compared against PCA and evaluated.  

ISOMP.html - Contains results of ISOMAP implementation.  

**Source code will be provided upon request**.

**Snapshot of input images of diffrent poses of the same person**  
![Snapshot of Input](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/isomap/poses.jpg?raw=true "Snapshot of Input")  

**Snapshot of ISOMAP results in 2-Dimensions illustrating similar orientations aligned to one direction**  
![Snapshot of isomap](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/isomap/isomap_results.jpg?raw=true "Snapshot of ISOMAP results")  

**Snapshot of PCA experimented on same dataset. ISOMAP performs better than PCA due to non-linear nature of image data**  
![Snapshot of PCA](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/isomap/pca_results.jpg?raw=true "Snapshot of PCA results")  
