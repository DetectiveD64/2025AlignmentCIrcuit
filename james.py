import time
import piplates.DAQC2plate as DAQC2
import statistics

ADDR = 0      # DAQC2 board address
CHANNEL = 0   # ADC input channel (0–7)
SAMPLES = 200 # Number of measurements
DELAY = 0.1   # Delay between samples in seconds (10 Hz)

def main():
    print(f"Collecting {SAMPLES} voltage readings from channel {CHANNEL} at 10 Hz...")

    voltages = []

    for i in range(SAMPLES):
        volts = DAQC2.getADC(ADDR, CHANNEL)
        voltages.append(volts)
        print(f"Reading {i+1}/{SAMPLES}: {volts:.4f} V")
        time.sleep(DELAY)

    avg_voltage = statistics.mean(voltages)
    median_voltage = statistics.median(voltages)
    std_dev = statistics.stdev(voltages)
    min_voltage = min(voltages)
    max_voltage = max(voltages)

    print("\n=== Measurement Summary ===")
    print(f"Average Voltage     : {avg_voltage:.4f} V")
    print(f"Median Voltage      : {median_voltage:.4f} V")
    print(f"Standard Deviation  : {std_dev:.4f} V")
    print(f"Lowest Voltage      : {min_voltage:.4f} V")
    print(f"Highest Voltage     : {max_voltage:.4f} V")

if __name__ == "__main__":
    main()


