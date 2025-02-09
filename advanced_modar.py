import numpy as np
import cv2
import os
import time
import RPi.GPIO as GPIO
import serial
from twilio.rest import Client

# Konfigurasi GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
BUZZER_PIN = 23
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Konfigurasi GPS
gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Konfigurasi Twilio untuk Notifikasi
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_number'
YOUR_PHONE_NUMBER = 'your_phone_number'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Inisialisasi Kamera
camera = cv2.VideoCapture(0)

# Inisialisasi SDR
os.system('rtl_sdr -f 2400000000 -s 2048000 -n 1024000 drone_signal.dat')

# Fungsi untuk Mendapatkan Koordinat GPS
def get_gps_coordinates():
    while True:
        data = gps.readline().decode('utf-8')
        if data.startswith('$GPGGA'):
            parts = data.split(',')
            if parts[2] and parts[4]:  # Latitude dan Longitude
                lat = float(parts[2][:2]) + float(parts[2][2:]) / 60
                lon = float(parts[4][:3]) + float(parts[4][3:]) / 60
                return lat, lon

# Fungsi untuk Mengirim Notifikasi
def send_notification(message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )

# Fungsi untuk Mendeteksi Drone
def detect_drone():
    if os.path.exists('drone_signal.dat'):
        with open('drone_signal.dat', 'rb') as f:
            data = np.fromfile(f, dtype=np.uint8)
            if np.max(data) > 200:  # Threshold deteksi
                return True
    return False

# Fungsi untuk Melacak Drone dengan Computer Vision
def track_drone(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter kecil
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return True, frame
    return False, frame

# Fungsi untuk Netralisasi Drone
def neutralize_drone():
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(10)  # Jamming selama 10 detik
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Fungsi untuk Logging Data
def log_data(message):
    with open("drone_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()}: {message}\n")

# Fungsi Utama
def main():
    try:
        while True:
            ret, frame = camera.read()
            drone_detected = detect_drone()
            tracked, tracked_frame = track_drone(frame)
            
            if drone_detected or tracked:
                print("Drone terdeteksi! Melakukan netralisasi...")
                neutralize_drone()
                lat, lon = get_gps_coordinates()
                message = f"Drone terdeteksi di lokasi: Lat {lat}, Lon {lon}"
                send_notification(message)
                log_data(message)
                
                # Tampilkan frame dengan pelacakan
                cv2.imshow("Drone Tracking", tracked_frame)
                cv2.waitKey(1)
            else:
                print("Tidak ada drone yang terdeteksi.")
            
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
