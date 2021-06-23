import socket

target_host = "google.com"

target_port = 80

# Create a socket objet

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client

client.connect((target_host,target_port))

# Send some data

client.send(b"get / HTTP/1.1\r\nHost: google.com \r\n\r\n")

# Receive some data

response = client.recv(4096)

print(response.decode())

client.close()