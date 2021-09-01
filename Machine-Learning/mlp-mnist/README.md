This folder contains a Visualization of MLP weights on MNIST.  

Sometimes looking at the learned coefficients of a neural network can provide insight into the learning behavior. For example if weights look unstructured, maybe some were not used at all, or if very large coefficients exist, maybe regularization was too low or the learning rate too high.  

This example shows how to plot some of the first layer weights in a MLPClassifier trained on the MNIST dataset.  

The input data consists of 28x28 pixel handwritten digits, leading to 784 features in the dataset. Therefore the first layer weight matrix have the shape (784, hidden_layer_sizes[0]).  We can therefore visualize a single column of the weight matrix as a 28x28 pixel image.   

To make the example run faster, we use very few hidden units, and train only for a very short time. Training longer would result in weights with a much moother spatial appearance. The example will throw a warning because it doesn't converge, in this case this is what we want because of CI's time constraints.  
