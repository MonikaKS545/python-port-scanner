import socket

print("=== Python Port Scanner ===")

target = input("Enter IP address or domain: ")

try:
    ip = socket.gethostbyname(target)

    print("Target:", target)
    print("IP Address:", ip)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((ip, 80))

    if result == 0:
        print("Port 80 is OPEN")
    else:
        print("Port 80 is CLOSED")

    s.close()

except socket.gaierror:
    print("Error: Unable to resolve the hostname.")