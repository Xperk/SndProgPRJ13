import soundfile as sf
import numpy as np
from scipy.signal import resample
import librosa as librosa
# Đọc tập tin âm thanh
audio_data1, sample_rate1 = sf.read('1.wav')
audio_data2, sample_rate2 = sf.read('2.wav')


audio1, sr1 = librosa.load('1.wav', sr=None)
audio2, sr2 = librosa.load('2.wav', sr=None)


print(sample_rate1)
print(sample_rate2)

# Chuyển đổi tín hiệu âm thanh thành một vector
audio_vector1 = audio_data1.flatten()
audio_vector2 = audio_data2.flatten()

print("In ra vector âm thanh")
print(audio_vector1)
print(audio_vector2)

audio1 = np.array(audio_vector1)
audio2 = np.array(audio_vector2)
print("audio1\n",audio1)
print("audio2\n",audio2)

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
print("In kết quả thương của vector âm thanh với một số\n",result3)

# Hiệu hai vector âm thanh
result4 = np.subtract(audio1_resized,audio2)
print("In kết quả hiệu hai vector âm thanh\n",result4)

# Nén
resampled_audio1 = resample(audio_data1, len(audio_data1)//100000)
resampled_audio2 = resample(audio_data2, len(audio_data1)//100000)
print("Nén\n",resampled_audio1)
print("Nén\n",resampled_audio2)


# Tăng
y_resampled = resample(resampled_audio1,len(resampled_audio1)*100000);
print("Tăng\n",y_resampled);



# Nhân chập hai vector âm thanh
print("Nhân chập")
resampled_audio11 = resample(audio1, len(audio1)//10000)
resampled_audio21 = resample(audio2, len(audio2)//10000)
# print(resampled_audio11)
# print(resampled_audio21)
audioastype1 = resampled_audio11.astype(np.float32)
audioastype2 = resampled_audio21.astype(np.float32)
# print(audioastype1)
# print(audioastype2)
audio_conv = np.convolve(audioastype1, audioastype2,mode='full')
print(audio_conv);


# Nhân tương quan
result5 = np.correlate(audioastype1,audioastype2,mode='full')
print("Nhân tương quan\n",result5)


# Năng lượng và công suất
energy = np.sum(audio1**2)
power = energy / audio1.size
print("Năng lượng:\n",energy)
print("Công suất:\n",power)