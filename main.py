import numpy as np

from math import exp, log, sqrt, pi


def heston_characteristic_function(u, S0, K, T, r, v0, kappa, theta, sigma, rho):

    """

    Computes the characteristic function of the Heston model.

    """

    i = 1j  # Complex unit

    d = np.sqrt((rho * sigma * u * i - kappa)**2 + (sigma**2) * (u * i + u**2))

    g = (kappa - rho * sigma * u * i - d) / (kappa - rho * sigma * u * i + d)

    C = r * u * i * T + (kappa * theta / (sigma**2)) * ((kappa - rho * sigma * u * i - d) * T - 2 * np.log((1 - g * np.exp(-d * T)) / (1 - g)))

    D = ((kappa - rho * sigma * u * i - d) / (sigma**2)) * ((1 - np.exp(-d * T)) / (1 - g * np.exp(-d * T)))

    return np.exp(C + D * v0 + i * u * np.log(S0))

def integrate(func, a, b, n=1000): 
    """ Simple numerical integration using the trapezoidal rule. """
    x = np.linspace(a, b, n)
    y = func(x)
    return np.trapz(y, x)
def P(S0, K, T, r, v0, kappa, theta, sigma, rho, P_num):

    """

    Computes the risk-neutral probabilities P1 or P2.

    """

    integral, _ = quad(lambda u: integrand(u, S0, K, T, r, v0, kappa, theta, sigma, rho, P_num), 0, 100)

    return 0.5 + (1 / pi) * integral

def heston_price(S0, K, T, r, v0, kappa, theta, sigma, rho):

    """

    Computes the price of a European call option under the Heston model.

    """

    P1 = P(S0, K, T, r, v0, kappa, theta, sigma, rho, 1)

    P2 = P(S0, K, T, r, v0, kappa, theta, sigma, rho, 2)

    return exp(-r * T) * (S0 * P1 - K * P2)



# Parameters
S0 = 100      # Initial asset price

K = 100       # Strike price

T = 1         # Time to maturity (in years)

r = 0.05      # Risk-free rate

v0 = 0.04     # Initial variance

kappa = 2     # Mean reversion speed

theta = 0.04  # Long-term variance

sigma = 0.5   # Volatility of variance

rho = -0.7    # Correlation between price and variance



# Calculate the option price

price = heston_price(S0, K, T, r, v0, kappa, theta, sigma, rho) 

print(f"The Heston model price of the European call option is: {price:.2f}")
