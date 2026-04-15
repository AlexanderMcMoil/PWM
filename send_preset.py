import serial
import numpy as np
import time

preset = [
    [500, 50, 2, 2],
    [450, 60, 4, 4],
    [400, 70, 6, 6],
    [350, 80, 8, 8],
    [300, 90, 10, 10],
    [250, 100, 12, 12],
    [200, 110, 14, 14],
    [150, 120, 16, 16],
]


# Not working yet
def send_message(ser, message):
    if isinstance(message, np.ndarray):
        # Convert NumPy array to a space-separated string
        message_str = " ".join(map(str, message.tolist()))  # ✅ Correct (Space-Separated)
    else:
        message_str = str(message)

    # Append newline for Arduino parsing
    message_bytes = (message_str + "\n").encode('utf-8')
    # print(message_bytes)

    ser.write(message_bytes)  # Send message
    print(f"Sent to Arduino: {message_str}")  # Debugging




def main():
    ser = serial.Serial(port="COM6", baudrate=115200)
    
    for i in range(1,8):
        send_message(ser, np.array([i] + preset[i]))
        time.sleep(0.5)
        input = ser.read_all().decode("utf-8").strip()
        print(input)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
    # ser = serial.Serial(port="COM6", baudrate=115200)

    # send_message(ser, "2 500 50 5 5")