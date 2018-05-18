import socket
import threading
import time
# 创建一个基于ipv4的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定监听的地址和端口
s.bind(('192.168.1.61',9998))
# 调用listen开始监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    data_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    print(data_time+'\t'+'Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print(data_time+'\t'+'Connection from %s:%s closed.'% addr)
    with open(r'server.txt','a') as file:
        file.write(data_time+'\t'+'Accept new connection from %s:%s...' % addr)
        file.write('\n')
        file.write(data_time+'\t'+'Connection from %s:%s closed.'% addr)
        file.write('\n')

# 通过循环接收来自客户端的连接
while True:
    #接受一个新连接
    sock,adder = s.accept()
    # 创建新线程接收连接
    t = threading.Thread(target=tcplink,args=(sock,adder))
    t.start()
