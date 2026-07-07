import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy as sp

# Data points
x_vals = np.array([1, 2, 3, 4, 5, 6])
y_vals = np.array([1, 3, 5, 8, 5, 2])

# ---- Lagrange ----
def lagrange_interpolation(x_data, y_data):
    x = sp.Symbol('x')
    n = len(x_data)
    poly = 0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        poly += term
    return sp.expand(poly), x

lagrange_poly, x_sym = lagrange_interpolation(x_vals, y_vals)
print("Lagrange Polynomial:")
print(lagrange_poly)

# ---- Cubic Spline ----
cs = CubicSpline(x_vals, y_vals, bc_type='not-a-knot')

print("\nCubic Spline piecewise polynomials:")
for i in range(len(x_vals) - 1):
    # Correct order in scipy.interpolate.CubicSpline:
    # cs.c[0] -> (x - xi)^3
    # cs.c[1] -> (x - xi)^2
    # cs.c[2] -> (x - xi)^1
    # cs.c[3] -> constant term
    a3 = cs.c[0, i]
    a2 = cs.c[1, i]
    a1 = cs.c[2, i]
    a0 = cs.c[3, i]
    xi = x_vals[i]
    print(f"\nInterval [{x_vals[i]}, {x_vals[i+1]}]:")
    print(f"  S_{i}(x) = {a3:.6f}(x - {xi})³ + {a2:.6f}(x - {xi})² + {a1:.6f}(x - {xi}) + {a0:.6f}")

# ---- Plot ----
x_plot = np.linspace(1, 6, 500)
y_lagrange = [float(lagrange_poly.subs(x_sym, val)) for val in x_plot]
y_spline = cs(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'ko', label='Data Points', markersize=8)
plt.plot(x_plot, y_lagrange, 'r-', label='Lagrange')
plt.plot(x_plot, y_spline, 'b--', label='Cubic Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()