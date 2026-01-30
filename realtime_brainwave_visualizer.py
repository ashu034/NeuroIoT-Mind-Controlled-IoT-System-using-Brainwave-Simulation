import numpy as np
import matplotlib.pyplot as plt
import time
from collections import deque

# --- Simulated Brainwave Data (from Step 3) ---
def simulate_brainwave():
    t = np.linspace(0, 10, 500)
    for i in range(len(t)):
        beta = 0.6 + 0.4 * np.sin(2 * np.pi * 0.25 * t[i])  # focus wave
        gamma = 0.5 + 0.4 * np.cos(2 * np.pi * 0.1 * t[i])  # relax wave
        yield beta, gamma
        time.sleep(0.05)

# --- Classification Logic ---
FOCUS_THRESHOLD = 0.65
RELAX_THRESHOLD = 0.55

def classify_state(beta, gamma):
    if beta > FOCUS_THRESHOLD and beta > gamma:
        return "FOCUS"
    elif gamma > RELAX_THRESHOLD and gamma > beta:
        return "RELAX"
    else:
        return "NEUTRAL"

# --- Live Plot Setup ---
plt.ion()
fig, ax = plt.subplots(figsize=(8, 4))
beta_data, gamma_data = deque(maxlen=100), deque(maxlen=100)
x_data = deque(maxlen=100)

line_beta, = ax.plot([], [], label='Beta (Focus)', color='tab:blue')
line_gamma, = ax.plot([], [], label='Gamma (Relax)', color='tab:orange')
ax.set_ylim(0, 1)
ax.set_xlim(0, 100)
ax.set_xlabel("Time (samples)")
ax.set_ylabel("Intensity")
ax.legend(loc="upper right")
fig.suptitle("🧠 NeuroIoT - Brainwave Monitor", fontsize=14)

# --- Stream and Update ---
state = "NEUTRAL"
counter = 0
for beta, gamma in simulate_brainwave():
    counter += 1
    beta_data.append(beta)
    gamma_data.append(gamma)
    x_data.append(counter)

    line_beta.set_data(x_data, beta_data)
    line_gamma.set_data(x_data, gamma_data)
    ax.set_xlim(max(0, counter - 100), counter)

    # Classify
    new_state = classify_state(beta, gamma)
    if new_state != state:
        state = new_state
        print(f"🧭 State changed → {state}")

    # Change title color based on state
    color = {"FOCUS": "green", "RELAX": "deepskyblue", "NEUTRAL": "gray"}[state]
    fig.suptitle(f"🧠 NeuroIoT - {state} Mode", color=color, fontsize=14)

    plt.pause(0.05)

plt.ioff()
plt.show()
