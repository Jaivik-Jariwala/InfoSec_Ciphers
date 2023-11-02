import numpy as np
import matplotlib.pyplot as plt

# Sample data (x and y values)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Fit a polynomial equation (e.g., quadratic) to the data
coefficients = np.polyfit(x, y, 2)  # Fit a quadratic equation (2nd-degree polynomial)

# Create a polynomial function based on the coefficients
poly_function = np.poly1d(coefficients)

# Generate x values for the equation
x_fit = np.linspace(min(x), max(x), 100)

# Calculate y values using the polynomial function
y_fit = poly_function(x_fit)

# Plot the data points and the fitted equation
plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, label=f'Fitted Equation: {coefficients[0]:.2f}x^2 + {coefficients[1]:.2f}x + {coefficients[2]:.2f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Fitting a Polynomial Equation to Data')
plt.grid()

# Show the plot
plt.show()
