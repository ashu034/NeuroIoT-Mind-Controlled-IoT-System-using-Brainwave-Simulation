import time
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
SAMPLES = 100
t = np.linspace(0, 10, SAMPLES)
beta = 0.6 + 0.4 * np.sin(2 * np.pi * 0.2 * t)   # Focus wave
gamma = 0.5 + 0.4 * np.cos(2 * np.pi * 0.1 * t)  # Relax wave

# Plot EEG wave simulation
plt.figure(figsize=(8, 4))
plt.plot(t, beta, label="Beta (Focus)")
plt.plot(t, gamma, label="Gamma (Relax)")
plt.xlabel("Time (s)")
plt.ylabel("Signal Intensity")
plt.title("Simulated Brainwave Signals")
plt.legend()
plt.grid(True)
plt.show()
