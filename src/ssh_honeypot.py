import socket
import datetime
import os

# Konfigurera servern
HOST = '0.0.0.0'  # Lyssna på alla IP-adresser
PORT = 2222  # Port att lyssna på (ändra vid behov)

# Se till att loggmappen finns
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

# Funktion för att logga anslutningsförsök
def log_attempt(ip, port, timestamp):
    with open(f"{log_dir}/connection_logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Inloggningsförsök från IP: {ip}, Port: {port}\n")

# Starta socket för att lyssna på inkommande anslutningar
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Återanvänd porten direkt efter att ha stängt anslutningen
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"SSH Honeypot kör på port {PORT}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Anslutning från: {addr}")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_attempt(addr[0], addr[1], timestamp)
            try:
                # Vänta på data från klienten och logga
                data = conn.recv(1024)
                if data:
                    print(f"Mottagen data: {data.decode('utf-8', errors='ignore').strip()}")
                    log_attempt(addr[0], addr[1], f"Mottagen data: {data.decode('utf-8', errors='ignore').strip()}")
            except BrokenPipeError:
                print("Broken pipe, anslutningen stängdes oväntat.")
            conn.close()
