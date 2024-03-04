import socket

HOST = '127.0.0.1'  # Loopback address
PORT = 65432        # La stessa porta su cui il server è in ascolto

# Creazione socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
	# Connessione al server
        client_socket.connect((HOST, PORT))

        while True:
            # Lettura messaggio da inviare
            message = input("Inserisci il messaggio da inviare (o 'exit' per uscire): ")

            if message.lower() == 'exit':
                break

            # Invio dati al server
            client_socket.sendall(message.encode())

            # Ricezione risposta dal server
            data = client_socket.recv(1024)

            # Stampa risposta
            print(f"Risposta dal server: {data.decode()}")


