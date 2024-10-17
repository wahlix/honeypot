# SSH Honeypot

This project is a simple SSH honeypot written in Python. It listens on a specified port for SSH connection attempts and logs incoming connections. The goal is to create a basic honeypot to observe and analyze SSH connection attempts, useful for understanding attack patterns and malicious activities.

## Features
- Listens for incoming connections on a specified port (default: 2222).
- Logs IP address, port, and data received from connection attempts.
- Simple setup, intended for educational purposes and learning about security.

## How It Works
The honeypot runs a basic TCP server that listens on a configurable port. When an SSH client attempts to connect, the honeypot logs the IP address, the data sent by the client, and any other relevant information. Note that this is not a fully-fledged SSH server; it is intended to simulate an SSH endpoint to attract unauthorized access attempts.

## Setup Instructions

1. **Clone the Repository**
   ```sh
   git clone https://github.com/wahlix/honeypot.git
   cd honeypot
   ```

2. **Install Dependencies**
   This script is written in Python 3 and does not require any external libraries beyond the standard Python library.
   Ensure you have Python 3 installed.

3. **Run the Honeypot**
   Navigate to the `src` directory and run the honeypot script:
   ```sh
   cd src
   python3 ssh_honeypot.py
   ```

4. **Logs**
   Connection attempts are logged in the `logs/connection_logs.txt` file. Make sure the `logs` directory exists before running the script, or it will be created automatically.

## Warning
This SSH honeypot is intended for educational purposes only. Running this honeypot could expose you to malicious activity and potentially illegal connection attempts. Use it responsibly and in a controlled environment. Never expose this honeypot to a production or public network without proper precautions.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contribution
Feel free to contribute by opening issues or pull requests. Improvements and suggestions are always welcome!

