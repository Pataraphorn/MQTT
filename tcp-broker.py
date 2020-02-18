from socket import * 
import sys

mainToken = []


SERV_PORT = 50000

serv_sock_addr1 = ('10.50.9.139', SERV_PORT)
welcome_sock = socket(AF_INET, SOCK_STREAM)
welcome_sock.bind(serv_sock_addr1)
welcome_sock.listen(1)

#serv_sock_addr2 = ('10.50.9.139', SERV_PORT)
#cli_sock = socket(AF_INET, SOCK_STREAM)
#cli_sock.connect(serv_sock_addr2)

print ('TCP server started ...')
while True:
  conn_sock, cli_sock_addr = welcome_sock.accept()
  print ('New client connected ..')
  username = conn_sock.recv(1024)

  while True:
     txtin = conn_sock.recv(1024)
     print ('%s>%s'%(username.decode('utf-8'),txtin.decode('utf-8')))

     #token = token.append(txtin.decode('utf-8'),cli_sock_addr[0])
     if txtin == b'quit':
       print('Client disconnected ..')
       print('Waiting for a new client ...')
       break
     else:
       txtout = txtin.upper()    
       conn_sock.send(txtout)
       newToken = [txtin.decode('utf-8'), cli_sock_addr[0]]
       mainToken.append(newToken)
       print(mainToken)
       #cli_sock.send(txtout)
       #print('send %s to subscriber'%(txtout.decode('utf-8'))
  #cli_sock.close()
  conn_sock.close()

s.close()

