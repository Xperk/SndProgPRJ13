import numpy as np
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, data, sr):
        self.data = data
        self.sr = sr
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


