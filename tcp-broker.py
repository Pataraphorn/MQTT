from socket import *
import sys
mainToken = []
SERV_PORT = 50000

serv_sock_addr1 = ('10.50.9.139', SERV_PORT)
welcome_sock = socket(AF_INET, SOCK_STREAM)
welcome_sock.bind(serv_sock_addr1)
welcome_sock.listen(1)

print('TCP server started ...')
while True:
  conn_sock, cli_sock_addr = welcome_sock.accept()
  username = conn_sock.recv(1024).decode('utf-8')

  print ('New client: %s IP=%s connected ..'%(username,cli_sock_addr[0]))
  
  while True:
     txtin = conn_sock.recv(1024)
     print ('%s>%s'%(username,txtin.decode('utf-8')))

     #token = token.append(txtin.decode('utf-8'),cli_sock_addr[0])
     if txtin == b'quit':
       print('Client disconnected ..')
       print('Waiting for a new client ...')
       break
     else:
       conn_sock.send(txtout)
       txtin_d = txtin.decode('utf-8')
       if txtin_d.split('|')[0] == "subscribe":
          print("55555555555")
          newToken = [txtin_d, cli_sock_addr[0]]
          mainToken.append(newToken)
          print(mainToken)
       elif txtin_d.split('|')[0] == "publish":
          print("22222222222")
          for i in range(len(mainToken)):
            if mainToken[i][0] == txtin.decode('utf-8').split('|')[1] :
              sub(mainToken[i][1])

       #cli_sock.send(txtout)
       #print('send %s to subscriber'%(txtout.decode('utf-8'))
  #cli_sock.close()
  conn_sock.close()
s.close()


       for i in range(len(mainToken)):
                if mainToken[i][0] == input:
                    sub(mainToken[i][1])