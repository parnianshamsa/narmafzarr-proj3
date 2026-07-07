import numpy as np
from scipy.integrate import quad, fixed_quad

# f(x) = e^(x^2) using numpy to support vector operations
def f(x):
    return np.exp(x**2)

a, b = 0, 1
n = 100
h = (b - a) / n

# 1. Simpson's Rule
sum_simpson = f(a) + f(b)
for i in range(1, n):
    x = a + i * h
    if i % 2 == 0:
        sum_simpson += 2 * f(x)
    else:
        sum_simpson += 4 * f(x)
simpson_val = (h / 3) * sum_simpson

# 2. Trapezoidal Rule
sum_trap = f(a) + f(b)
for i in range(1, n):
    x = a + i * h
    sum_trap += 2 * f(x)
trapezoid_val = (h / 2) * sum_trap

# 3. Gaussian Quadrature (N=5)
gauss_val, _ = fixed_quad(f, a, b, n=5)

# High precision baseline value
exact_val, _ = quad(f, a, b)

# Results Comparison
print(f"Exact Analytical Reference Value: {exact_val:.15f}\n")
print(f"Simpson's Rule Result:            {simpson_val:.15f}")
print(f"Trapezoidal Rule Result:          {trapezoid_val:.15f}")
print(f"Gaussian Quadrature (5-Point):    {gauss_val:.15f}\n")
print(f"Simpson Absolute Error:           {abs(simpson_val - exact_val):.2e}")
print(f"Trapezoid Absolute Error:         {abs(trapezoid_val - exact_val):.2e}")
print(f"Gaussian Quadrature Error:        {abs(gauss_val - exact_val):.2e}")