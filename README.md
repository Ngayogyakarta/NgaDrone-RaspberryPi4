# NgaDrone - Protect Your Privacy from Unwanted Drones and Cameras
NgaDrone is an anti-drone protection system designed to safeguard your privacy from unwanted drones and cameras. This system combines radio frequency (RF) detection technology, computer vision, and signal jamming to detect and neutralize drones approaching protected areas. 


## Project Description
NgaDrone adalah sistem proteksi anti-drone yang dirancang untuk melindungi privasi Anda dari drone dan kamera yang tidak diinginkan. Sistem ini menggunakan kombinasi teknologi deteksi frekuensi radio (RF), computer vision, dan gangguan sinyal (jamming) untuk mendeteksi dan menetralisir drone yang mendekati area yang dilindungi. Sistem ini dapat digunakan di rumah maupun saat Anda sedang berlibur atau dalam perjalanan.

## Fitur Utama:
- Deteksi Drone Otomatis: Menggunakan sensor RF dan kamera untuk mendeteksi keberadaan drone.
- Netralisasi Drone: Mengirim sinyal gangguan (jamming) untuk menghentikan operasi drone.
- Peringatan Visual dan Suara: Memberikan peringatan visual dan suara ketika drone terdeteksi.
- Portabel: Dapat digunakan di rumah maupun dibawa saat bepergian.
- User-Friendly Interface: Antarmuka yang mudah digunakan untuk mengontrol sistem.

## Komponen yang Dibutuhkan:
- **Raspberry Pi 4** (atau perangkat sejenis)
- **Software Defined Radio (SDR)** seperti RTL-SDR
- **Kamera IP** dengan kemampuan night vision
- **Modul RF Jamming** (sesuai dengan peraturan lokal)
- **Speaker dan LED** untuk peringatan
- **Power Bank** atau sumber daya portabel
- **Python** (untuk pemrograman)

## Step-by-Step Cara Menggunakan:
**1. Persiapan Hardware**
- **Raspberry Pi 4:** Siapkan Raspberry Pi 4 dengan OS Raspbian terinstal.
- **SDR:** Hubungkan RTL-SDR ke Raspberry Pi.
- **Kamera IP:** Hubungkan kamera IP ke Raspberry Pi.
- **Modul RF Jamming:** Hubungkan modul RF jamming ke Raspberry Pi (pastikan sesuai dengan peraturan lokal).
- **Speaker dan LED:** Hubungkan speaker dan LED ke GPIO Raspberry Pi.

**2. Instalasi Software**
Update Raspberry Pi:
```
sudo apt-get update
sudo apt-get upgrade
```
Instalasi Library yang Dibutuhkan:
```
sudo apt-get install python3-pip
pip3 install numpy opencv-python rtl-sdr
```
**3. Menjalankan Sistem**
```
python3 modar_guardian.py
```
## 5. Penggunaan Keraton (Out Of Keraton)
- **Di Rumah:** Letakkan perangkat di area yang ingin dilindungi. Sistem akan otomatis mendeteksi dan menetralisir drone yang mendekat.
- **Saat Berlibur:** Bawa perangkat portabel Anda. Nyalakan sistem saat Anda merasa perlu melindungi privasi Anda dari drone.

**4. Peringatan dan Legalitas**
- Pastikan penggunaan modul RF jamming sesuai dengan peraturan lokal. Beberapa negara memiliki regulasi ketat terhadap penggunaan perangkat jamming.
- Sistem ini hanya untuk keperluan pribadi dan tidak boleh digunakan untuk tujuan ilegal.

> [!NOTE]
> Sistem ini adalah prototipe dan mungkin memerlukan penyesuaian lebih lanjut tergantung pada lingkungan dan jenis drone yang ingin kamu deteksi. Selalu patuhi hukum dan regulasi yang berlaku di wilayah Anda.
