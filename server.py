import socket
import threading
import sys
import logging



def receive_messages(client_socket, stop_event):
    while not stop_event.is_set():
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Client disconnected")
                logging.info("Client disconnected")
                stop_event.set()
                break
            print(f"Client: {message}")
            logging.info(f"Client: {message}")
            if message.lower() == 'quit':
                print("Client requested disconnection")
                logging.info("Client requested disconnection")
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

def start_server(host='0.0.0.0', port=50000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind((host, port))
        server.listen(1)
        print(f"Server listening on {host}:{port}")
        logging.info(f"Server started on {host}:{port}")

        client_socket, address = server.accept()
        print(f"Connected to {address}")
        logging.info(f"Connected to {address}")
        stop_event = threading.Event()

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket, stop_event))
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
                    logging.info("Server requested disconnection")
                    stop_event.set()
                    break
                client_socket.send(message.encode('utf-8'))
                logging.info(f"Server: {message}")
            except Exception as e:
                print(f"Error sending message: {e}")
                logging.error(f"Error sending message: {e}")
                stop_event.set()
                break

        try:
            client_socket.close()
        except:
            pass
        server.close()
    except Exception as e:
        print(f"Server error: {e}")
        logging.error(f"Server error: {e}")
    finally:
        server.close()
        print("Server closed")
        logging.info("Server closed")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
    start_server(host='0.0.0.0', port=port)