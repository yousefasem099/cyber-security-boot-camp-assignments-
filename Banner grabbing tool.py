
import socket
import ssl

target = "127.0.0.1"

def grab_banner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((target, port))

        if port == 443:
            context = ssl.create_default_context()
            s = context.wrap_socket(s, server_hostname=target)

        if port in [80, 443]:
            request = "HEAD / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
        else:
            s.send(b"\r\n")

        banner = s.recv(1024)

        if banner:
            print("\nPort:", port)
            print(banner.decode("utf-8", errors="ignore"))
        else:
            print("Port", port, ": No Banner")

        s.close()

    except socket.timeout:
        print("Port", port, ": Timeout")

    except ConnectionRefusedError:
        print("Port", port, ": Connection Refused")

    except Exception as e:
        print("Port", port, ":", e)


ports = [21, 22, 25, 80, 443, 3306, 8080]

print("Starting Banner Grabbing...")

for port in ports:
    grab_banner(port)

print("\nScanning Finished.")
