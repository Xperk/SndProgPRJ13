import soundfile as sf
import numpy as np
from scipy.signal import resample
# Đọc tập tin âm thanh
audio_data1, sample_rate1 = sf.read('1.wav')
audio_data2, sample_rate2 = sf.read('2.wav')

# Chuyển đổi tín hiệu âm thanh thành một vector
audio_vector1 = audio_data1.flatten()
audio_vector2 = audio_data2.flatten()

print("In ra vector âm thanh")
print(audio_vector1)
print(audio_vector2)

audio1 = np.array(audio_vector1)
audio2 = np.array(audio_vector2)


# Dịch chuyển audio sang trái 100 mẫu
shifted_audio = np.roll(audio1, -100)
print("Dịch thời gian sang trái 100 mẫu của vector 1\n",shifted_audio)

# Đảo thời gian
flipped_audio = np.flip(audio1)
print("Đảo thời gian\n",flipped_audio)


audio1_resized = np.resize(audio1, audio2.shape)
# Tích hai vector âm thanh
result1 = np.multiply(audio1_resized,audio2)
print("In kết quả tích hai vector âm thanh\n",result1)

# Tổng hai vector âm thanh
result2 = np.add(audio1_resized,audio2);
print("In kết quả tổng hai vector âm thanh\n",result2)

# Thương hai vector âm thanh
result3 = np.divide(audio2,3)
print("In kết quả thương hai vector âm thanh\n",result3)

# Hiệu hai vector âm thanh
result4 = np.subtract(audio1_resized,audio2)
print("In kết quả hiệu hai vector âm thanh\n",result4)

# Nhân chập hai vector âm thanh
# audio_conv = np.convolve(audio1, audio2)
# print("In kết quả nhân chập\n",audio_conv)


# Nhân tương quan
# result5 = np.correlate(audio1_resized,audio2,mode='full')
# print("Nhân tương quan\n",result5)


# Nén
resampled_audio = resample(audio1, len(audio1)//100000)
print("Nén\n",resampled_audio)
print(resampled_audio.__len__())