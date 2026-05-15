import numpy as np

class HSVDDynamics:
    def __init__(self, n_levels=5, lambda_scale=2.0):
        self.n_levels = n_levels
        self.lambda_scale = lambda_scale
        self.tau = [lambda_scale ** i for i in range(n_levels)]
        self.gamma = [1.0 / (lambda_scale ** i) for i in range(n_levels)]
        self.T = [0.5 * np.exp(0.4 * i) for i in range(n_levels)]
        self.x = [np.random.normal(0, 0.5) for _ in range(n_levels)]
    
    def step(self, dt=0.05):
        for i in range(self.n_levels):
            grad_F = self.x[i]  # simple harmonic approximation
            drift = -self.gamma[i] * grad_F
            noise = np.sqrt(2 * self.T[i] * self.gamma[i]) * np.random.randn()
            # Control from upper level
            if i > 0:
                control = 0.2 * self.x[i-1]
                drift += control
            self.x[i] += (drift + noise) * dt
    
    def simulate(self, steps=1000):
        history = [[] for _ in range(self.n_levels)]
        for _ in range(steps):
            self.step()
            for i in range(self.n_levels):
                history[i].append(self.x[i])
        return history