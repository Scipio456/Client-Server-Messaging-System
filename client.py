import socket
import threading
import sys
import logging


def receive_messages(client_socket, stop_event):
    while not stop_event.is_set():
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server")
                logging.info("Disconnected from server")
                stop_event.set()
                break
            print(f"Server: {message}")
            logging.info(f"Server: {message}")
            if message.lower() == 'quit':
                print("Server requested disconnection")
                logging.info("Server requested disconnection")
                stop_event.set()
                break
        except Exception as e:
            if not stop_event.is_set():
                print(f"Error receiving message: {e}")
                logging.error(f"Error receiving message: {e}")
            break
    try:
        client_socket.close()
    except:
        pass

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        client.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        logging.info(f"Connected to server at {host}:{port}")
        stop_event = threading.Event()

        receive_thread = threading.Thread(target=receive_messages, args=(client, stop_event))
        receive_thread.start()

        while not stop_event.is_set():
            try:
                message = input("Enter message (or 'quit' to exit): ").strip()
                if len(message) > 1024:
                    print("Error: Message too long (max 1024 characters)")
                    logging.warning("Attempted to send message longer than 1024 characters")
                    continue
                if not message:
                    continue
                if message.lower() == 'quit':
                    print("Successfully disconnected")
                    logging.info("Client requested disconnection")
                    client.send(message.encode('utf-8'))
                    stop_event.set()
                    break
                client.send(message.encode('utf-8'))
                logging.info(f"Client: {message}")
            except Exception as e:
                print(f"Error sending message: {e}")
                logging.error(f"Error sending message: {e}")
                stop_event.set()
                break
    except Exception as e:
        print(f"Connection error: {e}")
        logging.error(f"Connection error: {e}")
    finally:
        try:
            client.close()
        except:
            pass
        print("Client closed")
        logging.info("Client closed")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 client.py <server_ip> [port]")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 50000
    start_client(host, port)