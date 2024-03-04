import socket
HOST = '127.0.0.1'  # Loopback address
PORT = 65432  # Porta arbitraria non utilizzata dal sistema operativo

# Socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
	# Associazione a indirizzo e porta
        server_socket.bind((HOST, PORT))
        # Avvio server in ascolto
        server_socket.listen()

        print(f"Server TCP in ascolto su {HOST}:{PORT}")

        # Connessione in entrata
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connesso a {addr}")

            while True:
                # Ricezione dati dal client
                data = conn.recv(1024)
                if not data:
                    break  

                print(f"Ricevuto: {data.decode()}")

                # Invio messaggio di Echo
                conn.sendall(("Echo di: " + data.decode()).encode())
