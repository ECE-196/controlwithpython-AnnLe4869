import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

# from serial import Serial, SerialException

# with Serial('/COM3', 9600) as ser:
#     while True:
#         print(ser.readline().decode())