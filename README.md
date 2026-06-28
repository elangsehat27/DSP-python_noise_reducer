🎧 Python Noise Reducer (Spectral Subtraction)



\[!\[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)



Proyek ini adalah implementasi sistem **Noise Reduction** (Pengurangan Derau) pada file audio menggunakan pendekatan matematis murni: **Spectral Subtraction**. 



Berbeda dengan menggunakan library instan yang bekerja seperti "kotak hitam", proyek ini dibangun dari nol (\*from scratch\*) menggunakan algoritma *Short-Time Fourier Transform* (STFT) untuk memisahkan frekuensi suara vokal manusia dari *background noise* yang konstan (seperti desis mikrofon, suara kipas, atau AC) tanpa merusak kejelasan vokal.



Proyek ini juga didokumentasikan dalam format video di YouTube: https://youtu.be/RNhoOheUtnM?si=LOec7DP-ooBjdz\_0

Proyek ini juga didokumentasikan dalam format Ebook di webiot: https://ebook.webiot.id/ebooks/implementasi-spectral-substraction

\---



**## Fitur Utama**



\- **Zero Black-Box Library:** Menggunakan murni kalkulasi matematika (`numpy` \& `scipy`) tanpa library AI pihak ketiga.

\- **Auto-Normalization:** Otomatis menyeimbangkan volume audio asli agar suara vokal tidak ikut terhapus.

\- **Smart Noise Profiling:** Mencari nilai \*Median\* secara otomatis dari seluruh durasi audio untuk menangkap "sidik jari" \*noise\*.

\- **Interactive UI:** Dilengkapi dengan pop-up jendela \*File Explorer\* (`tkinter`) untuk memilih file `.wav` dengan mudah.

\- **Visual Proof:** Menghasilkan 6 grafik perbandingan visual (Waveform \& FFT Spectrogram) menggunakan `matplotlib` setelah pemrosesan selesai.



\---



**## Prasyarat \& Instalasi**



Pastikan kamu sudah menginstal Python (versi 3.8 atau lebih baru). Lalu, instal semua library pendukung dengan menjalankan perintah berikut di terminal/CMD:



```bash

pip install numpy scipy soundfile matplotlib

