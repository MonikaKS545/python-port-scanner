# Python Port Scanner

## 📌 About the Project

A simple Python-based TCP Port Scanner that scans a target IP address or domain for open ports within a user-defined port range.

This project was built as part of my Ethical Hacking learning journey to understand networking, sockets, and Python programming.

---

## Features

- Scan any valid IP address or domain
- User-defined port range
- Detects common services (SSH, HTTP, FTP, etc.)
- Displays the total number of open ports
- Measures scan completion time
- Saves scan results to a text file
- Handles invalid input and DNS resolution errors
- Graceful keyboard interruption handling

---

## Technologies Used

- Python 3
- Socket Module
- Time Module
- Datetime Module
- Git
- GitHub

---

## Project Structure

```
python-port-scanner/
│
├── port_scanner.py
├── README.md
├── .gitignore
├── LICENSE
└── scan_results.txt (generated after running)
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/MonikaKS545/python-port-scanner.git
```

2. Open the project folder

3. Run

```bash
python port_scanner.py
```

4. Enter:

- Target IP or Domain
- Start Port
- End Port

---

## Example Output

```
=== Python Port Scanner ===

Enter IP address or domain: scanme.nmap.org
Enter Start Port: 20
Enter End Port: 100

Scanning scanme.nmap.org (45.33.32.156)
Scanning ports 20 to 100

Port 22 (SSH) is OPEN
Port 80 (HTTP) is OPEN

Open ports found: 2
Scan completed in 40.62 seconds

Results saved to scan_results.txt
```

---

## What I Learned

- Python socket programming
- TCP port scanning
- DNS resolution
- Exception handling
- File handling
- Git version control
- GitHub workflow
- Basic networking concepts

---

## Future Improvements

- Faster scanning using multithreading
- Banner grabbing
- Service version detection
- Command-line arguments
- GUI version
- Export results in CSV format

---

## ⚠️ Disclaimer

This tool is developed for educational purposes only.
Use it only on systems you own or have explicit permission to test.

## Author

**MonikaKS545**
GitHub: https://github.com/MonikaKS545
