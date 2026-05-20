import numpy as np

class MetropolisHasting:

    def __init__(self, target_pdf, distribution_range=[], proposal_std=1.0):
        self.target_pdf = target_pdf
        self.d_range = distribution_range
        self.proposal_std = proposal_std
        self
    
    def generate_candidate(self, current_state, coordinate):
        updated_state = current_state.copy()
        if (len(self.d_range) == 0):
            # gaussian proposal if it's unbounded
            updated_state[coordinate] += np.random.normal(0,self.proposal_std)
            return updated_state
        updated_state[coordinate] = np.random.uniform(self.d_range[0], self.d_range[1])
        return updated_state

    def sampler(self, initial_state, n, burn_in=0):
        dimension = len(initial_state)
        current_state = initial_state
        samples = []
        for step in range(burn_in + n):
            for coordinate in range(dimension):
                candidate = self.generate_candidate(current_state, coordinate)
                # acceptance step 
                try:
                    alpha = min(1, self.target_pdf(candidate)/self.target_pdf(current_state))
                except ZeroDivisionError:
                    alpha = 1 # zero divisor, i.e current state is outside of the range
                # randomly generate a uniformly distributed number in range [0,1]
                u = np.random.rand()
                if alpha > u:
                    current_state = candidate # accept move
            if step >= burn_in:
                samples.append(current_state.copy())
        return np.array(samples)



