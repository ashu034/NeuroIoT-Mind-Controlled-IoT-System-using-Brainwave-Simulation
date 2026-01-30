import time
import numpy as np

# Simulated Brainwave Stream (for testing)
def simulate_brainwave():
    """
    Returns simulated brainwave readings over time.
    Beta = Focus, Gamma = Relax.
    """
    t = np.linspace(0, 10, 100)
    for i in range(len(t)):
        beta = 0.6 + 0.4 * np.sin(2 * np.pi * 0.2 * t[i])     # focus wave
        gamma = 0.5 + 0.4 * np.cos(2 * np.pi * 0.1 * t[i])    # relax wave
        yield beta, gamma
        time.sleep(0.1)

# Thresholds
FOCUS_THRESHOLD = 0.65
RELAX_THRESHOLD = 0.55

def classify_state(beta, gamma):
    """
    Classify state based on signal strengths.
    """
    if beta > FOCUS_THRESHOLD and beta > gamma:
        return "FOCUS"
    elif gamma > RELAX_THRESHOLD and gamma > beta:
        return "RELAX"
    else:
        return "NEUTRAL"

# Main Loop
if __name__ == "__main__":
    print("🧠 NeuroIoT Brainwave Classification Started...\n")
    prev_state = None

    for beta, gamma in simulate_brainwave():
        state = classify_state(beta, gamma)
        print(f"Beta: {beta:.2f} | Gamma: {gamma:.2f} | → State: {state}")

        # Detect change of state
        if state != prev_state:
            print(f"👉 Transition Detected → {state} Mode Activated!\n")
            prev_state = state
