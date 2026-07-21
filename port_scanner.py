import socket
import time

print("=== Python Port Scanner ===")

target = input("Enter IP address or domain: ")

try:
    ip = socket.gethostbyname(target)

    print(f"\nScanning {target} ({ip})")
    print("-" * 40)

    start_time = time.time()

    for port in range(1, 101):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        s.close()

    end_time = time.time()

    print("-" * 40)
    print(f"Scan completed in {end_time - start_time:.2f} seconds")

except socket.gaierror:
    print("Error: Unable to resolve the hostname.")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")

except Exception as e:
    print(f"Unexpected error: {e}")