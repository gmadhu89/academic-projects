This project aims at creating routines that fit an input of random variables to a set of continuous / discrete distributions to determine the best fitting distribution for the sample data. Input sample is tested against discrete distributions like Bernoulli, Poisson, Geometric and continuous distributions like Normal, Gamma and Weibull. We generate maximum likelihood estimates of the distributions that are very close to the actual parameters of the sample data set, and perform Chi-Squared goodness of fit tests on the sample data against every distribution to validate the goodness of fit of the routine. Additionally, we validate negative scenarios, for e.g., an input geometric data should fail the goodness of fit test for a normal distribution.  

Code:  
Input_Distribution_Routines.ipynb  

Results:  
Fitting_Input_Distributions_Report.pdf
