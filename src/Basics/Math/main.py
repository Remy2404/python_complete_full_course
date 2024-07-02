import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def linear(x):
    return 2*x + 3

def quadratic(x):
    return x**2

def exponential(x):
    return np.exp(x)

def sine(x):
    return np.sin(x)

# Create a range of values for x
x = np.linspace(-2, 2, 400)
x_sine = np.linspace(-np.pi/2, np.pi/2, 400)

# Plot the functions
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, linear(x), label='$f(x) = 2x + 3$')
plt.title('Linear Function')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, quadratic(x), label='$g(x) = x^2$')
plt.title('Quadratic Function')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, exponential(x), label='$h(x) = e^x$')
plt.title('Exponential Function')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_sine, sine(x_sine), label='$k(x) = \sin(x)$')
plt.title('Sine Function')
plt.legend()

plt.tight_layout()
plt.show()
