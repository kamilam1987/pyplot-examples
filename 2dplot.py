import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label = "Actual")
# b stands for blue dots instead of line
plt.plot(x, y, 'b-', label = "Model")

# Adds title
plt.title("Simple plot")
# Adds label
plt.xlabel("Weight")
plt.ylabel("Mass")
# Adds legend
plt.legend()
# shows figures
plt.show()

plt.plot(x, y + noise, 'c.')
plt.plot(x, y, 'g-')

plt.show()