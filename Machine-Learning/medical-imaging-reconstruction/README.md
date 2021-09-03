This folder contains implementation of a medical image reconstruction using regulation techniques (Lasso and Ridge).  

For this, I have considered an example resembles medical imaging reconstruction in MRI. We begin with a true image image of dimension 50 x 50 (i.e., there are 2500 pixels in total). Data is in folder /data/cs.mat;  This image is truly sparse, in the sense that 2084 of its pixels have a value of 0, while 416 pixels have a value of 1. You can think of this image as a toy version of an MRI image that we are interested in collecting.  

Because of the nature of the machine that collects the MRI image, it takes a long time to measure each pixel value individually, but it's faster to measure a linear combination of pixel values. We measure n = 1300 linear combinations, with the weights in the linear combination being random, in fact, independently distributed as N(0; 1) (Multivariate-Gaussian). Because the machine is not perfect, we don't get to observe this directly, but we observe a noisy version. These measurements are given by the entries of the vector
y = Ax + n;  

Now the question is: can we model y as a linear combination of the columns of x to recover some coefficient vector that is close to the image? Although the number of measurements n = 1300 is smaller than the dimension p = 2500, the true image is sparse. Thus we can recover the sparse image using few measurements exploiting its structure. This is the idea behind the field of compressed sensing.  

We use LASSO/ Ridge to perform this compression and reconstruct the image and observe their error rates.  

medical_imaging_reconstruction.pdf - Contains results of the reconstruction.  

**Source code will be provided upon request.**
