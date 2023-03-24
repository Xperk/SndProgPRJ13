from Signal import Signal
import numpy as np
if __name__ == '__main__':
    data1 = [1,4,5,6,1,3]
    sr1 = 44100
    signal1 = Signal(data1, sr1)
    signal1.plot()

    # signal1.shift_time(10)

    signal1.flipp_time()
    signal1.plot()

    # data2 = [7,5,3,5,9,2]
    # src2 = 44100
    # signal2 = Signal(data2,src2)
    # signal2.plot()

