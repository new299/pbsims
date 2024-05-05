import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('simheat')

# Create heatmap
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()

# Save the plot as a PNG file
plt.savefig('simheat.png')

# Optionally, you can close the plot to free up resources
plt.close()

