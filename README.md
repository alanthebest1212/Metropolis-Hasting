# Metropolis-Hasting

## Overview


## theory
Metropolis-Hasting algorithm is a Markov Chain Monte Carlo method. 
The algorithm generates an stationary distribution which represents the target posterior in Bayesian statistics
By construction, Metropolis-Hasting creates a reversible chain.
With enough sampling, the related frequency of each value converges to their original density distribution
### detailed balance equation
$\pi(x) P_{x,x'} = \pi(x') P_{x',x}$
for $\pi{(x)}$ , i.e. the related frequency for result all x, satisfies the reversible flow of the Markov Chain,
then $\pi{x}$ is the posterior density function.
