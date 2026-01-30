🧠 NeuroIoT: Mind-Controlled IoT System using Brainwave Simulation

NeuroIoT is an innovative IoT-based project that demonstrates mind-controlled device automation using simulated brain focus and relaxation states.
Instead of using an expensive EEG headset, this system uses AI-based webcam eye-tracking to mimic human focus and relaxation, and controls real-world electrical devices using an ESP32 and relay module.

🚀 Project Overview

The human brain generates different mental states such as focus and relaxation.
In this project, we simulate these mental states using computer vision (eye tracking) and convert them into control signals for IoT devices.

Eyes open / focused → Device turns ON

Eyes closed / relaxed → Device turns OFF

The system bridges AI + IoT + Embedded Systems into a single real-time working prototype.

🧠 How It Works

A webcam captures real-time video of the user.

Mediapipe Face Mesh detects eye landmarks.

Eye Aspect Ratio (EAR) is calculated:

High EAR → Focus

Low EAR → Relax

Python sends FOCUS or RELAX commands to ESP32 via serial communication.

ESP32 controls a relay module.

Relay switches an electrical bulb ON or OFF.
