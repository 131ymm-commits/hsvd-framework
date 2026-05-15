import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def power_dynamics(t, m, J=1.0, h=0.5, T=1.0):
    return np.tanh((J * m + h) / T) - m

def simulate_power_transition():
    h_values = np.linspace(0, 2.0, 50)
    final_m = []
    for h in h_values:
        sol = solve_ivp(power_dynamics, [0, 50], [0.01], args=(1.0, h, 1.0))
        final_m.append(sol.y[0][-1])
    
    plt.plot(h_values, final_m, 'b-o')
    plt.xlabel('Control strength h (Power)')
    plt.ylabel('Order parameter m')
    plt.title('Phase Transition in Power/Control')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    simulate_power_transition()