import serial
import time
import random

# === Configuration ===
PORT = "/dev/tty.usbserial-0001"   # Your ESP32 serial port
BAUD = 115200

# === Simulated Brainwave States ===
states = ["FOCUS", "RELAX", "NEUTRAL"]

def connect_esp32():
    try:
        esp = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)
        print(f"✅ Connected to ESP32 on {PORT}")
        return esp
    except Exception as e:
        print("❌ Connection error:", e)
        return None

def main():
    esp = connect_esp32()
    if not esp:
        return

    try:
        while True:
            state = random.choice(states)  # Simulate brainwave state
            print(f"🧠 Sending state → {state}")
            esp.write((state + "\n").encode())
            time.sleep(3)  # Delay between signals
    except KeyboardInterrupt:
        print("\n🛑 Stopped.")
    finally:
        esp.close()

if __name__ == "__main__":
    main()
