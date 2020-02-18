from socket import * 
import sys
MAX_BUF = 2048
SERV_PORT = 50000



def subscribe(broker_ip_address,topic_name):
    serv_sock_addr = (broker_ip_address, SERV_PORT)
    cli_sock = socket(AF_INET, SOCK_STREAM)
    cli_sock.connect(serv_sock_addr)
    
    cli_sock.send(username.encode('utf-8'))

    while True:
        sys.stdout.flush()
        cli_sock.send(word[2].encode('utf-8'))
        txtout = sys.stdin.readline().strip()
        if txtout == 'quit':
            cli_sock.send(txtout.encode('utf-8'))
            break
    cli_sock.close()
    

username = input('Enter your name: ')
cmd = input('Enter your cmd: ')
word = cmd.split(' ')
broker_ip_address = word[1]
topic_name = word[2]
if word[0] == "subscribe":                        #subscribe broker_ip_address ’topic_name’
    subscribe(broker_ip_address,topic_name)
elif word[0] == "publish":                        #publish ’broker_ip_address’ ’topic_name’ ’data to publish’
    data = word[3]
    #publish(broker_ip_address,topic_name,data)
else:
    print("bye")
    





