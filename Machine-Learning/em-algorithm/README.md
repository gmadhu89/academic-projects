Code to implement Expectation-Maximization (EM) Algorithm for fitting a Gaussian mixture model for the MNIST hand-written digits dataset. The dataset is reduced to only two cases, of
digits "2" and "6" only. I will fit GMM with C = 2. I have used the data file data.mat. True label of the data are provided in label.mat and label.dat.  

The matrix images is of size 784-by-1990, i.e., there are totally 1990 images, and each column of the matrix corresponds to one image of size 28-by-28 pixels (the image is vector-
ized; the original image can be recovered by map the vector into a matrix).  

I first use PCA to reduce the dimensionality of the data before applying to EM. We will put all "6" and "2" digits together, to project the original data into 4-dimensional vectors.

**Source code will be provided upon request**
