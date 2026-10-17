import socket

host = input("Host or IP (example: 127.0.0.1): ").strip()
first = int(input("First port: "))
second = int(input("Last port: "))  

if not (1 <= first <= second <= 65535):
    raise ValueError("from 1 to 65535")

for port in range(first, second + 1):
    try:
        with socket.create_connection((host, port), timeout=0.5):
            print(f"{port}: open")
    except ConnectionRefusedError:
        print(f"{port}: closed")
    except TimeoutError:
        print(f"{port}: no response")
    except OSError as error:
        print(f"{port}: error - {error}")