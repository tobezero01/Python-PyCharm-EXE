import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Đọc file âm thanh
audio_path = ''
y, sr = librosa.load(audio_path)

# Tính toán biểu đồ tần số theo thời gian
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Hiển thị biểu đồ
plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()
