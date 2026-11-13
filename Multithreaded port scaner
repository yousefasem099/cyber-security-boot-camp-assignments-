
import socket
from concurrent.futures import ThreadPoolExecutor

target = "127.0.0.1"

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    s.close()

print("Scanning started...")

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(1, 1025))

print("Scanning finished.")
