import socket
import time
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

print("=== Python Port Scanner ===")

target = input("Enter IP address or domain: ")

try:
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    ip = socket.gethostbyname(target)

    print(f"\nScanning {target} ({ip})")
    print(f"Scanning ports {start_port} to {end_port}")
    print("-" * 40)

    start_time = time.time()

    for port in range(start_port, end_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"Port {port} ({service}) is OPEN")

        s.close()

    end_time = time.time()

    print("-" * 40)
    print(f"Scan completed in {end_time - start_time:.2f} seconds")

except socket.gaierror:
    print("Error: Unable to resolve the hostname.")

except ValueError:
    print("Error: Please enter valid port numbers.")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")

except Exception as e:
    print(f"Unexpected error: {e}")