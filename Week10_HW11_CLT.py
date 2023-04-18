"""
Computational Physics PHSX 815 | Homework #11

- Write a program that illustrates, in some way, the Central Limit Theorem (preferably with one or more figures)
- For example, the Central Limit Theorem indicates that the normalized sum (i.e. the arithmetic mean) of random variables, each independently sampled from the same distribution, will asymptotically follow a Gaussian distribution. Try sampling a continuous variable from a probability distribution that is *not* a Gaussian - repeat this N times and take the average. Then repeat *that* again many times (so M "experiments" each with N samples) - what does this distribution of averages look like? As you increase N?

        - As you increase N the distribution of averages becomes closer and closer to a
          Gaussian distribution.
   
   
Sources Consulted:
- https://towardsdatascience.com/central-limit-theorem-explained-with-python-code-230884d40ce0
- https://www.geeksforgeeks.org/python-central-limit-theorem/
- https://medium.com/analytics-vidhya/illustration-with-python-central-limit-theorem-aa4d81f7b570
"""

# Import necessary packages
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

""" Per the Central Limit Theorem, even with a data sample that is not already normally distributed, the sample mean will be approximately normally distributed for large sample sizes regardless of the distribution from which we sample. For this homework I will show what happens when we start from a gamma distribution as well as a dataset of randomly generated numbers """

""" Gamma Distribution """
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

# build gamma distribution of data
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.gamma(shape, scale, 1000000)

## sample from population with different number of sampling
# a list of sample means -- which will be plotted later on
meansample = []

# number of samples -- this is what we are testing 
# according to the CLT, as this increases, the distribution should appear more and more like a normal distribution
numofsample = [1000,2500,5000,10000,25000,100000]

# sample size
samplesize = 500

# for each number of sampling (1000 to 50000)
for i in numofsample:
    # collect mean of each sample
    eachmeansample = []
    # for each sampling
    for j in range(0,i):
        # sampling 500 sample from population
        rc = random.choices(s, k=samplesize)
        # collect mean of each sample
        eachmeansample.append(sum(rc)/len(rc))
    # add mean of each sampling to the list
    meansample.append(eachmeansample)
   
# I will import the list above, so I make the code after this line run only when I call this file directly
 
# plot
cols = 3
rows = 2
fig, ax = plt.subplots(rows, cols, figsize=(20,15))
n = 0
for i in range(0, rows):
    for j in range(0, cols):
        ax[i, j].hist(meansample[n], 200, density=True, color='goldenrod')
        ax[i, j].set_title(label="Number of Sampling : " + str(numofsample[n]))
        n += 1
        ax[i, j].set_xlabel(xlabel="Sample Means")
plt.show()


""" Randomly Generated Numbers """

import numpy
import matplotlib.pyplot as plt
 
# number of sample
#num = [1, 5, 50, 100] 
num = [10, 2500, 10000, 100000] 

# list of sample means
means = [] 
 
# Generating 1, 10, 30, 100 random numbers from -40 to 40
# taking their mean and appending it to list means.
for j in num:
    # Generating seed so that we can get same result
    numpy.random.seed(1)
    x = [numpy.mean(
        numpy.random.randint(
            -50, 50, j)) for _i in range(2000)]
    means.append(x)
k = 0
 
# plotting all the means in one figure
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        # Histogram for each x stored in means
        ax[i, j].hist(means[k], bins=200, density = True, color='indianred')
        ax[i, j].set_title(label ="Number of Sampling : " + str(num[k]))
        k = k + 1
        ax[i, j].set_xlabel(xlabel="Sample Means")
plt.show()





