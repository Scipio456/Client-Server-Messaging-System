# Client-Server Messaging System

A Python-based chat application developed for educational purposes to demonstrate client-server communication using TCP sockets. This system allows multiple clients to connect to a server and exchange messages, showcasing socket programming and multi-threading concepts.

## Features
- Supports multiple clients connecting to a server on a specified port (default: 50000).
- Enables real-time message exchange between clients via the server.
- Uses multi-threading to handle concurrent client connections.
- Validates server IP and port inputs to ensure reliable connections.
- Logs connection details to `chat.log` (excluded from repository).

## Prerequisites
- **Python 3.x**: Verify installation with:
  ```bash
  python3 --version
  ```
- **Permissions**: Run the server and clients on systems you own (e.g., `127.0.0.1`) or have explicit authorization to use.
- **Firewall Configuration**: Ensure the server allows incoming TCP connections on port 50000 and clients allow outgoing connections.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd client-server-messaging
   ```
2. Verify the presence of `server.py`, `client.py`, `.gitignore`, `README.md`, and `LICENSE`:
   ```bash
   ls
   ```
3. Confirm Python 3 is installed:
   ```bash
   python3 --version
   ```

## Usage
1. **Start the Server**:
   Run the server on the desired host and port (default: `127.0.0.1:50000`):
   ```bash
   python3 server.py
   ```
   **Sample Output**:
   ```
   Server listening on 127.0.0.1:50000...
   Client connected: 127.0.0.1:54321
   ```

2. **Start Client(s)**:
   Run one or more clients, connecting to the server’s IP and port:
   ```bash
   python3 client.py
   ```
   **Sample Interaction**:
   ```
   Enter your username: Alice
   Connected to server at 127.0.0.1:50000
   Type your message (or 'quit' to exit): Hello, Bob!
   Received: Bob: Hi, Alice!
   ```

3. **Testing Across Devices**:
   - Start the server on a machine with a known IP (e.g., `<your_server_ip>`):
     ```bash
     python3 server.py
     ```
   - Configure the firewall (e.g., Windows) to allow port 50000:
     ```bash
     netsh advfirewall firewall add rule name="Chat Server" dir=in action=allow protocol=TCP localport=50000
     ```
   - Run clients on other devices, specifying the server’s IP:
     ```bash
     python3 client.py <your_server_ip> 50000
     ```

## Output Files
- **Log File**: Connection and message details are logged to `chat.log` (excluded from repository).
  - **Example Entry**:
    ```
    2025-08-31 17:14:23 - Client Alice connected from 127.0.0.1:54321
    ```

## Security Note
This tool is for **educational purposes only**. Running servers or clients on unauthorized systems or networks is prohibited. Use only on systems you own (e.g., `127.0.0.1`) or have explicit authorization to access. Replace `<your_server_ip>` with your own authorized IP address.

## Troubleshooting
- **Connection Refused**:
  - Ensure the server is running and listening on the correct IP/port.
  - Verify with:
    ```bash
    netstat -an | grep 50000
    ```
  - Check firewall settings (e.g., Windows):
    ```bash
    netsh advfirewall firewall add rule name="Chat Server" dir=in action=allow protocol=TCP localport=50000
    ```
- **Invalid IP/Port**:
  - Confirm the server’s IP is reachable:
    ```bash
    ping <your_server_ip>
    ```
- **No Messages Received**:
  - Ensure multiple clients are connected and sending messages.
  - Check `chat.log` for connection errors.
- **Slow Performance**: Increase thread limits in `server.py` (edit threading configuration) or reduce client load.

## Testing with the Port Scanner
To verify the server is running on port 50000, use the Simple Port Scanner from the same repository:
1. Start the server:
   ```bash
   python3 server.py
   ```
2. Run the port scanner:
   ```bash
   python3 port_scanner.py <your_server_ip> 50000 50000
   ```
   **Sample Output**:
   ```
   Scanning <your_server_ip> from port 50000 to 50000...
   Port 50000 is OPEN (Custom Chat App)
   Open ports found:
   Port 50000: Custom Chat App
   Scan completed in 0.12 seconds
   ```

## Repository Contents
The project is hosted at `<your-repo-url>` and includes:
- `server.py`
- `client.py`
- `.gitignore`
- `README.md`
- `LICENSE`

Sensitive files (e.g., `chat.log`) are excluded via `.gitignore` to prevent uploading logs or IP addresses.

## License
This project is licensed under the Client-Server Messaging System Educational Use Only License. See the [LICENSE](LICENSE) file for details. The code may be viewed and run for educational purposes only; modifications and distribution are prohibited without explicit permission from the author.

## Disclaimer
This project is for educational use only. Do not use on unauthorized systems or networks. The author is not responsible for any misuse.