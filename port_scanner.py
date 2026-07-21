import socket
import time
from datetime import datetime

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

target = input("Enter IP address or domain: ").strip()

try:
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    # Validate port numbers
    if start_port < 1 or end_port > 65535:
        print("Error: Port numbers must be between 1 and 65535.")
        exit()

    if start_port > end_port:
        print("Error: Start Port must be less than or equal to End Port.")
        exit()

    # Resolve hostname
    ip = socket.gethostbyname(target)

    print(f"\nScanning {target} ({ip})")
    print(f"Scanning ports {start_port} to {end_port}")
    print("-" * 40)

    start_time = time.time()

    open_ports = 0
    results = []

    # Scan ports
    for port in range(start_port, end_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            open_ports += 1

            service = common_ports.get(port, "Unknown")
            output = f"Port {port} ({service}) is OPEN"

            print(output)
            results.append(output)

        s.close()

    end_time = time.time()
    scan_time = end_time - start_time

    print("-" * 40)

    if open_ports == 0:
        print("No open ports found.")

    print(f"Open ports found: {open_ports}")
    print(f"Scan completed in {scan_time:.2f} seconds")

    # Save results to file
    with open("scan_results.txt", "w") as file:

        file.write("Python Port Scanner Results\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Scan Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Target    : {target}\n")
        file.write(f"IP Address: {ip}\n")
        file.write(f"Port Range: {start_port}-{end_port}\n\n")

        file.write("Open Ports\n")
        file.write("-" * 15 + "\n")

        if open_ports == 0:
            file.write("No open ports found.\n")
        else:
            for item in results:
                file.write(item + "\n")

        file.write(f"\nOpen Ports Found: {open_ports}\n")
        file.write(f"Scan Time: {scan_time:.2f} seconds\n")

    print("\nResults saved to scan_results.txt")

except socket.gaierror:
    print("Error: Unable to resolve the hostname.")

except ValueError:
    print("Error: Please enter valid port numbers.")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")

except Exception as e:
    print(f"Unexpected error: {e}")