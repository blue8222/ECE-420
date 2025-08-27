import numpy as np
import matplotlib.pyplot as plt
import os


''' # single peak detector
def peak_detection(t, sig):
    peaks = []
    max_val = -np.inf
    N = len(sig)
    for i in range(0, N):
        if sig[i] > max_val:
            max_val = sig[i]
            position = t[i]
            
    peaks.append((position, max_val))
    return np.array(peaks)
'''


# multi peak detector
def peak_detection(t, sig):
    peaks = []

    threshold = 3
   
    N = len(sig)
    
    B = 10 # size of buffer

    for i in range(B, N - B):
        buffer = sig[i - B//2 : i + B//2 + 1] # slice the window from signal

        if(sig[i] == np.max(buffer) and sig[i] > threshold):
            peaks.append([t[i], sig[i]])

    return np.array(peaks)

os.chdir('H:\ECE 420\lab1')

csv_filename = 'sample_sensor_data.csv'
data = np.genfromtxt(csv_filename, delimiter=',').T
timestamps = (data[0] - data[0,0]) / 1000

accel_data = data[1:4]
gyro_data = data[4:-1]

max_peaks = peak_detection(timestamps, accel_data[0])

plt.plot(timestamps, accel_data[0])
plt.title("First axis of accelerometer data")
plt.xlabel("Time")
plt.ylabel("Meters per second")
plt.scatter(max_peaks[:,0], max_peaks[:,1], color = 'red')
plt.show()

