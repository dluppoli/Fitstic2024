import socket

HOST = '127.0.0.1'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:

	while True:
		# Lettura messaggio da inviare
		message = input("Inserisci il messaggio da inviare (o 'exit' per uscire): ")

		if message.lower() == 'exit':
			client_socket.close()
			break
		
		# Invio dati al server
		client_socket.sendto(message.encode(), (HOST, PORT))
		
		# Ricezione risposta dal server
		data, server_address = client_socket.recvfrom(1024)

		# Stampa risposta
		print(f"Ricevuto: {data.decode()} da {server_address}")



