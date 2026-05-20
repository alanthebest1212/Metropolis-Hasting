import numpy as np
import matplotlib.pyplot as plt

from metropolis_hastings import MetropolisHasting

def target_pdf(x):
    # If x is an array, return a scalar PDF for multidimensional input
    # Here assume 1D
    return np.exp(-0.5 * x[0]**2) / np.sqrt(2 * np.pi)

sampler = MetropolisHasting(target_pdf=target_pdf, distribution_range=[-5, 5], proposal_std=1.0)


initial_state = [0]  # start at 0 for 1D
n_samples = 1000
samples = sampler.sampler(initial_state=initial_state, n=n_samples, burn_in=100)

samples = np.array(samples).flatten()

# Plot density using Seaborn
import seaborn as sns
sns.kdeplot(samples, fill=True)
plt.title("Density plot of Metropolis-Hastings samples")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
