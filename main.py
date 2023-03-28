from Signal import Signal
if __name__ == '__main__':
    data1 = [1,4,5,6,1,3]
    sr = 44100
    signal1 = Signal(data1, sr)

    data2 = [7,5,3,5,9,2,1,4,5,6,1,3]
    signal2 = Signal(data2,sr)

    data3 = [12, 10, 6, 10, 18, 4, 2, 4, 10, 6, 2, 6]
    signal3 = Signal(data3, sr)

    # signal1.shift_time(10)

    # signal1.flipp_time()

    # signal1.multiply(signal2)

    # signal3.resample(2)

    # signal1.convolve(signal2)

    signal1.compress(0.5)

    # energy = signal1.energy()

    # print(energy)
    signal1.plot()



