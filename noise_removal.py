import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import stft, istft
from scipy.fft import fft, fftfreq
import os
import tkinter as tk
from tkinter import filedialog

# =========================
# 1. LOAD AUDIO (DINAMIS DENGAN POP-UP)
# =========================
print("Membuka jendela pemilihan file...")

root = tk.Tk()
root.withdraw() 
root.attributes('-topmost', True) 

file_path = filedialog.askopenfilename(
    title="Pilih File Audio Asli",
    filetypes=[("WAV Files", "*.wav")]
)

if not file_path:
    print("Proses dibatalkan: Tidak ada file yang dipilih.")
    exit()

nama_file_asli = os.path.basename(file_path)
nama_file_tanpa_ext = os.path.splitext(nama_file_asli)[0]

print(f"File berhasil dimuat: {nama_file_asli}")

audio, fs = sf.read(file_path)

if len(audio.shape) > 1:
    audio = audio[:, 0]

audio = audio / np.max(np.abs(audio))

# =========================
# 2. TAMBAH NOISE
# =========================
np.random.seed(0)
noise = np.random.normal(0, 0.02, len(audio))
audio_noisy = audio + noise

sf.write(f"{nama_file_tanpa_ext}_noisy.wav", audio_noisy, fs)

# =========================
# 3. SPECTRAL SUBTRACTION (MURNI MATEMATIKA)
# =========================
print("Menjalankan Spectral Subtraction Manual...")

f, t, Zxx = stft(audio_noisy, fs, nperseg=2048)
magnitude = np.abs(Zxx)
phase = np.angle(Zxx)

noise_profile = np.median(magnitude, axis=1, keepdims=True)

alpha = 2.0  
beta = 0.02  

subtracted_magnitude = magnitude - (alpha * noise_profile)
subtracted_magnitude = np.maximum(subtracted_magnitude, beta * noise_profile)

Zxx_denoised = subtracted_magnitude * np.exp(1j * phase)
_, audio_denoised = istft(Zxx_denoised, fs)
audio_denoised = audio_denoised[:len(audio)]

# Menyimpan file denoised dengan nama dinamis
sf.write(f"{nama_file_tanpa_ext}_denoised.wav", audio_denoised, fs)

# =========================
# 4. FFT FUNCTION
# =========================
def plot_fft(signal, fs, title):
    N = len(signal)
    freq = fftfreq(N, 1 / fs)
    magnitude = np.abs(fft(signal))

    plt.figure()
    plt.plot(freq[:N // 2], magnitude[:N // 2])
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()

# =========================
# 5. PLOT WAVEFORM
# =========================
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(audio)
plt.title(f"Original: {nama_file_asli} (Normalized)")

plt.subplot(3, 1, 2)
plt.plot(audio_noisy)
plt.title("Noisy")

plt.subplot(3, 1, 3)
plt.plot(audio_denoised)
plt.title("Denoised (Manual Spectral Subtraction)")

plt.tight_layout()

# =========================
# 6. PLOT FFT
# =========================
plot_fft(audio, fs, "FFT Original")
plot_fft(audio_noisy, fs, "FFT Noisy")
plot_fft(audio_denoised, fs, "FFT Denoised")

plt.show()

print(f"Selesai! Hasil disimpan sebagai:")
print(f"- {nama_file_tanpa_ext}_noisy.wav")
print(f"- {nama_file_tanpa_ext}_denoised.wav")