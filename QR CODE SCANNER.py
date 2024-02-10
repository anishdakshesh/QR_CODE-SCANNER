import cv2
from pyzbar.pyzbar import decode

# Function to decode QR codes
def qr_code_scanner(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_codes = decode(gray)

    for qr_code in qr_codes:
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        qr_code_data = qr_code.data.decode('utf-8')
        print("QR Code Data:", qr_code_data)

    return image

# Main loop to capture video frames
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = qr_code_scanner(frame)
    cv2.imshow('QR Code Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
