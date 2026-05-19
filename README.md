# Metropolis-Hasting

## How to use
example for normally distributed random variable ~ N(0,1)
define function without needing to normalize 

def NormalD(x):
    return np.exp(-0.5*((x**2) / (1.0**2)))

then make such object

N_rv = MetropolisHasting(NormalD) // since no range constrant or any other constrant

then make the sample

initial_state = [0] // all in arrays, with multiple coordinate for multi-dimensions


samples = N_rv.sampler([0], 3000) // will give an array of 3000 points
                                  // following the given distribution

## Overview
Direct sampling fails for complicated distribution functions like multi-modal, high-dimensional, no close form distributions
Metropolis-Hasting MC methods is used for finding samplings when Direct sampling fails. 
Also called Gibbs method for multi-dimensional distributions
### special properties
generate samples without needing the normalization of distributions.


## theory
Metropolis-Hasting algorithm is a Markov Chain Monte Carlo method. 
The algorithm generates an stationary distribution which represents the target posterior in Bayesian statistics
By construction, Metropolis-Hasting creates a reversible chain.
With enough sampling, the related frequency of each value converges to their original density distribution
### detailed balance equation
$\pi(x) P_{x,x'} = \pi(x') P_{x',x}$
for $\pi$(x) , i.e. the related frequency for result all x, satisfies the reversible flow of the Markov Chain,
then $\pi{x}$ is the posterior density function.


## simple example with bayesian model
### scenario: coin flip, we want chance of getting heads. And in 10 flips we got 6 heads
Prior: with no information, let the chance of head be uniformely distributed in [0,1]
likelihood: flipping the coin 10 times: 6 heads, 4 tails.
we want chance of head
So posterior will follow ~ Beta(7,5)
using a random trial of 30000 sample size, we have

mean = 0.5838238859633782

variance = 0.01843491328875613

compare to its true value

true mean = 7/12, about 0.583

true variance = 35/1872 about 0.0187


