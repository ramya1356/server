import socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind((socket.gethostname(),1348))
sk.listen()
while True:
    client,address=sk.accept()
    print("connection is accepted")
    print(address)
    # client.send(bytes)("socket programming")
    client.send(b"socket programming")
