import socket
HOST = '127.0.0.1'
PORT = 65434

# Socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
	# Associazione a indirizzo e porta
	server_socket.bind((HOST, PORT))

	print(f"Server UDP in ascolto su {HOST}:{PORT}")

	while True:
		# Ricezione dati dal client
		data, client_address = server_socket.recvfrom(1024)
		print(f"Ricevuto: {data.decode()} da {client_address}")

		# Invio messaggio di Echo
		server_socket.sendto(("Echo di: " + data.decode()).encode(), client_address)
