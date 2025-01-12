
# Advanced DDoS Attack Script

This is an advanced DDoS attack script that simulates an HTTPS flood using multiple threads. The script uses Python's `ssl` and `socket` libraries to create and send requests to the target website, simulating a flood of traffic.

## Features:
- Sends randomized HTTP GET requests with custom user agents.
- Allows the user to input the target website URL and port.
- Automatically resolves the target website's IP address.
- Supports multi-threaded attack for higher intensity.
- You can specify the duration and number of threads.

## Requirements

- Python 3.x
- Termux (for Android) or any Linux-based system

### Required Python Libraries:
1. **ssl** - for creating secure SSL connections.
2. **socket** - for managing network connections.
3. **threading** - to handle multiple threads for the attack.
4. **random** - to select random user agents.
5. **time** - for managing attack duration.
6. **sys** - for handling exceptions.

## Installation on Termux:

Follow these steps to install the required dependencies and run the script on Termux:

### Step 1: Install Python
```bash
pkg update && pkg upgrade
pkg install python
```

### Step 2: Install Required Python Modules
```bash
pip install requests
pip install socket
```

### Step 3: Clone the Repository (Optional)
```bash
git clone https://github.com/C0d3Fusion/Advanced-ddos-Attack.git
cd Advanced-ddos-Attack
```

### Step 4: Run the Script
```bash
python HeavyDdos.py
```

## Usage:

1. **Enter the target website URL** (e.g., `www.example.com`).
2. **Enter the target port** (default is 443 for HTTPS).
3. **Specify the attack duration** (in seconds).
4. **Input the number of threads** to use for the attack (e.g., 5000).

## Disclaimer:
**This script is for educational purposes only.** It should never be used for illegal activities. Use it responsibly to understand how DDoS attacks work and for testing purposes in environments where you have permission to do so.

## Contributing

Feel free to fork the repository, submit issues, and create pull requests to improve the functionality of the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
