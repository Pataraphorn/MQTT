from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

serv_sock_addr = ('10.50.10.143', SERV_PORT)
cli_sock = socket(AF_INET, SOCK_STREAM)
cli_sock.connect(serv_sock_addr)

username = input('Enter your name: ')
cli_sock.send(username.encode('utf-8'))

while True:
    print ('%s> ' %(username), end='') 
    sys.stdout.flush()
    txtout = sys.stdin.readline().strip()
    cli_sock.send(txtout.encode('utf-8'))
    if txtout == 'quit':
      break
    modifiedMsg = cli_sock.recv(2048)
    print (modifiedMsg.decode('utf-8'))
cli_sock.close()
