import numpy as np
import cv2
import os
import time
import RPi.GPIO as GPIO

# Konfigurasi GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
BUZZER_PIN = 23
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Inisialisasi Kamera
camera = cv2.VideoCapture(0)

# Inisialisasi SDR
os.system('rtl_sdr -f 2400000000 -s 2048000 -n 1024000 drone_signal.dat')

def detect_drone():
    # Analisis sinyal RF untuk mendeteksi drone
    if os.path.exists('drone_signal.dat'):
        with open('drone_signal.dat', 'rb') as f:
            data = np.fromfile(f, dtype=np.uint8)
            if np.max(data) > 200:  # Threshold deteksi
                return True
    return False

def neutralize_drone():
    # Aktifkan modul RF jamming
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(10)  # Jamming selama 10 detik
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def main():
    try:
        while True:
            ret, frame = camera.read()
            if detect_drone():
                print("Drone terdeteksi! Melakukan netralisasi...")
                neutralize_drone()
            else:
                print("Tidak ada drone yang terdeteksi.")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        camera.release()

if __name__ == "__main__":
    main()
