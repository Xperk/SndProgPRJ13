import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample
import librosa as librosa

class Signal:
    def __init__(self, data, sr):
        self.data = data
        self.sr = sr
        self.root = self.data[0];
        self.length = len(self.data)

    def plot(self, start_sec=None, end_sec=None):
        if start_sec is None:
            start_sample = 0
        else:
            start_sample = int(start_sec * self.sr)
        if end_sec is None:
            end_sample = self.length - 1
        else:
            end_sample = int(end_sec * self.sr)
        time = np.linspace(start_sample / self.sr, end_sample / self.sr, end_sample - start_sample + 1)
        plt.plot(time, self.data[start_sample:end_sample + 1])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()

    def shift_time(self,time):
        self.data = np.roll(self.data,time)

    def flipp_time(self):
        self.data = np.flip(self.data)

    def multiply(self,other):
        self.data = np.multiply(self.data,other.data)

    def add(self,other):
        self.data = np.add(self.data,other.data)

    def divide(self,other):
        self.data = np.divide(self.data,other.data)

    def subtract(self,other):
        self.data = np.divide(self.data,other.data)

    def compress(self, threshold):
        compressed_data = np.sign(self.data) * np.maximum(0, np.abs(self.data) - threshold)
        return Signal(compressed_data, self.sr)


    def resample(self,n):
        self.data = resample(self.data, len(self.data)*n)

    def convolve(self,other):
        self.data = np.convolve(self.data, other.data,mode='full')

    def correlate(self,other):
        self.data = np.correlate(self.data,other.data,mode='full')

    def energy(self):
        return np.sum(np.square(np.abs(self.data)))

    def power(self):
        return np.mean(np.square(np.abs(self.data)))