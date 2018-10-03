import matplotlib.pyplot as plt
import numpy as np

# One row and two colums and select first plot
plt.subplot(1, 2, 1)
# Centered around 0
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x)

# One row and two colums and select first plot
plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()