import serial
import numpy as np
import time

arduino_port = "COM4"  # Update this to your Arduino's port
baudrate = 115200  # Ensure this matches the Arduino's baud rate

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

preset_clear = [
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
]

preset_example_2 = [
    [90, 500, 6, 6],  
    [180, 500, 6, 6],  
    [90, 500, 3, 3],  
    [180, 1000, 6, 6],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
]

preset_example_2 = [
    [90, 500, 6, 3],  
    [180, 500, 6, 3],  
    [90, 500, 4, 2],  
    [180, 1000, 6, 3],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
    [0, 0, 0, 0],  
]

# Not working yet
def send_message(ser, message):
    if isinstance(message, np.ndarray):
        # Convert NumPy array to a space-separated string
        message_str = " ".join(map(str, message.tolist()))  # ✅ Correct (Space-Separated)
    else:
        message_str = str(message)

    # Append newline for Arduino parsing
    print(message_str)
    message_bytes = (message_str + "\n").encode('utf-8')
    # print(message_bytes)

    ser.write(message_bytes)  # Send message
    print(f"Sent to Arduino: {message_str}")  # Debugging




def pack_serial_data(channel, pulse_width, frequency, leading_amplitude, lagging_amplitude):
    """
    Packs 5 parameters into a 4-byte array for serial transmission.
    
    Bit layout (32 bits total):
    [31:29] : Padding (3 bits) - set to 0
    [29:24] : lagging_amplitude (5 bits)
    [23:18] : frequency (6 bits)
    [17:8]  : pulse_width (10 bits)
    [7:3]   : leading_amplitude (5 bits)
    [2:0]   : channel (3 bits)
    """
    
    # 1. Mask inputs to ensure they strictly fit within their bit limits
    channel &= 0x07             # 3 bits (max 7)
    leading_amplitude &= 0x1F   # 5 bits (max 31)
    pulse_width &= 0x3FF        # 10 bits (max 1023)
    frequency &= 0x3F           # 6 bits (max 63)
    lagging_amplitude &= 0x1F   # 5 bits (max 31)
    
    # 2. Shift and combine using bitwise OR
    packed_data = (channel) | \
                  (leading_amplitude << 3) | \
                  (pulse_width << 8) | \
                  (frequency << 18) | \
                  (lagging_amplitude << 24)
                  
    return packed_data.to_bytes(4, byteorder='big')

def pack_serial_data_multiground(channel, pulse_width, frequency, leading_amplitude, lagging_amplitude, signal_address, ground_address):
    """
    Packs 5 parameters into a 4-byte array for serial transmission.
    
    Bit layout (32 bits total):
    [33:32] : ground_address (2 bits)
    [31:29] : signal_address (3 bits)
    [29:24] : lagging_amplitude (5 bits)
    [23:18] : frequency (6 bits)
    [17:8]  : pulse_width (10 bits)
    [7:3]   : leading_amplitude (5 bits)
    [2:0]   : channel (3 bits)
    """

    # 1. Mask inputs to ensure they strictly fit within their bit limits
    channel &= 0x07             # 3 bits (max 7)
    leading_amplitude &= 0x1F   # 5 bits (max 31)
    pulse_width &= 0x3FF        # 10 bits (max 1023)
    frequency &= 0x3F           # 6 bits (max 63)
    lagging_amplitude &= 0x1F   # 5 bits (max 31)
    signal_address &= 0x07      # 3 bits (max 7)
    ground_address &= 0x03      # 2 bits (max 3)

    packed_data = (channel) | \
                  (leading_amplitude << 3) | \
                  (pulse_width << 8) | \
                  (frequency << 18) | \
                  (lagging_amplitude << 24) | \
                  (signal_address << 29) | \
                  (ground_address << 32)
    return packed_data.to_bytes(5, byteorder='big')



def send_serial_data(ser, channel, pulse_width, frequency, leading_amplitude, lagging_amplitude):
    packed_data = pack_serial_data(channel, pulse_width, frequency, leading_amplitude, lagging_amplitude)
    ser.write(packed_data)
    # print(f"Sent packed data to Arduino: {packed_data}")

def main_2():

    with serial.Serial(port=arduino_port, baudrate=baudrate) as ser:
        time.sleep(2)  # Wait for Arduino to reset
        try:
            while True:
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    break
                message_int = [int(x) for x in message.split(" ")]
                message  = pack_serial_data(*message_int)
                ser.write(message)
                while ser.in_waiting:
                    message = ser.read_until(b'\n')
                    print(f"Received from Arduino: {message.decode('utf-8').strip()}")
        except KeyboardInterrupt:
            print("Exiting...")

def main():
    with serial.Serial(port=arduino_port, baudrate=baudrate) as ser:
        time.sleep(2)
        for i in range(8):
            message = pack_serial_data(i, preset[i][0], preset[i][1], preset[i][2], preset[i][3])
            print(message)
            # message_bytes = pack_serial_data(i, preset[i][0], preset[i][1], preset[i][2], preset[i][3])
            ser.write(message)
            # time.sleep(1.5)

def send_preset(preset_data):
    with serial.Serial(port=arduino_port, baudrate=baudrate) as ser:
        # time.sleep(1)
        for i in range(8):
            message = pack_serial_data(i, *preset_data[i])
            # print(message)
            ser.write(message)
            # time.sleep(0.5)  # Optional delay between sending each channel's data

def ramp_up():
    with serial.Serial(port=arduino_port, baudrate=baudrate) as ser:
        time.sleep(1)
        for i in range(8):
            for j in range(0, 31):  # Ramp up leading amplitude from 0 to 30
                message = pack_serial_data(i, preset[i][0], preset[i][1], j, j)
                ser.write(message)
                time.sleep(0.1)  # Delay to observe the ramp-up effect


if __name__ == "__main__":
    # main_2()
    # ramp_up()
    send_preset(preset_clear)
    # i = 0
