# HSVD Mathematical Core

## Fundamental Dynamics

$$\frac{d\mathbf{x}_i}{dt} = -\gamma_i \nabla_{\mathbf{x}_i} \mathcal{F}_i(\mathbf{x}_i, q_i) + \boldsymbol{\eta}_i(t)$$

### Variational Free Energy
$$\mathcal{F}_i = \mathbb{E}_{q}[E] - T_i H[q] + D_{KL}(q_i \parallel p_i)$$ 

## Scaling Laws

$$\tau_i = \tau_0 \lambda^i \qquad \gamma_i = \gamma_0 \lambda^{-i} \qquad T_i = T_0 e^{\alpha i}$$

## Power & Control

Mean-field order parameter dynamics:

$$\frac{dm}{dt} = \tanh\left( \frac{J m + h}{T} \right) - m$$

where $h$ is control strength (power).