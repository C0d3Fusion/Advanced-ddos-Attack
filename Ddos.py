import threading
import requests
import random
import time
from queue import Queue

# Configuration
url = input("Enter the target website URL (with https://): ").strip()
num_requests = int(input("Enter the total number of requests: "))
concurrent_threads = int(input("Enter the number of concurrent threads: "))
request_type = input("Enter the request type (GET/POST): ").strip().upper()

# POST request data payload (for POST requests only)
post_data = {}
if request_type == "POST":
    key = input("Enter POST data key (or leave blank): ").strip()
    value = input("Enter POST data value (or leave blank): ").strip()
    if key and value:
        post_data[key] = value

# User-Agent headers for more realistic simulation
headers_list = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},
    {"User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"}
]

# Random paths to simulate dynamic requests
random_paths = [
    "/", "/about", "/contact", "/products", "/api/data", "/login", "/random-page"
]

# Queue for managing requests
request_queue = Queue()

# Fill the queue with requests
for _ in range(num_requests):
    request_queue.put(random.choice(random_paths))

# Function to send requests
def send_request():
    while not request_queue.empty():
        path = request_queue.get()
        full_url = url + path
        headers = random.choice(headers_list)
        try:
            if request_type == "POST":
                response = requests.post(full_url, data=post_data, headers=headers, timeout=5)
            else:
                response = requests.get(full_url, headers=headers, timeout=5)
            print(f"Request to {full_url} sent: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error for {full_url}: {e}")
        finally:
            request_queue.task_done()

# Function to manage threads
def stress_test():
    threads = []
    for _ in range(concurrent_threads):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Main Execution
if __name__ == "__main__":
    start_time = time.time()
    print(f"\nStarting stress test on {url} with {num_requests} requests...\n")
    stress_test()
    end_time = time.time()
    print(f"\nStress test completed in {end_time - start_time:.2f} seconds")
