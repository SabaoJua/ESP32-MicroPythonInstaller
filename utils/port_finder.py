import platform
import os
import serial.tools.list_ports

def find_serial_port():
    system = platform.system()
    print("Sistema é: ",system)

    if system == "Windows":
        ports = [p.device for p in serial.tools.list_ports.comports() if 'USB' in p.description or 'UART' in p.description]
    if system == "Darwin":
        ports = ["/dev/" + p for p in os.listdir('/dev') if p.startswith('cu.usb')]
        print("Porta(s) encontrada(s): ",ports);
    else:  # Linux e outros sistemas baseados em Unix
        ports = ["/dev/" + p for p in os.listdir('/dev') if p.startswith('ttyUSB') or p.startswith('ttyACM')]

    return ports[0] if ports else None
