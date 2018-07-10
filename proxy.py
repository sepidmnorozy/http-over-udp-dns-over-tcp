import math
import argparse
import signal
import logging
import select
import socket
import time
import threading

FORMAT = '%(asctime)-15s %(levelname)-10s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger()

LOCAL_DATA_HANDLER = lambda x:x
REMOTE_DATA_HANDLER = lambda x:x

BUFFER_SIZE = 2 ** 10  # 1024. Keep buffer size as power of 2.


def serverDataLen(s):
    lines = s.splitlines()
    for line in lines:
        left, sep, right = line.partition("Content-Length:")
        print("[-*-] :", line, sep)
        if len(sep) > 0:
            return int(right.strip())
            # if "Content-Length:" in line:
            #     list = line.split(":")
            #     res = list[1].lstrip()
            #     return res
    return -1

def fragmentation(data):
    tmp = []
    i = 0
    n = math.ceil(len(data)/1000)
    for i in range (0,n):
        if i == n -1 :
            tmp.append(data[i*1000:])
        else:
            tmp.append(data[i * 1000:(i + 1) * 1000 - 1])
    f = 0
    seq = 0
    fragments = []
    if len(tmp) == 1:
        f = 0
        seq = 0
    for i in range(len(tmp)):
        if len(tmp) == 1:
            f = 0
            seq = 0
        elif i == len(tmp)-1 and len(tmp)!=1:
            f=2
            seq=i
        else:
            f=1
            seq=i
        alireza = ("f="+str(f)+";seq="+str(seq)+";\r\n").encode()
        fragment = bytearray(alireza)+bytearray(tmp[i])
        fragments.append(fragment)
    #to code alireza kharabe
    return fragments




def retreiveHostname(dataClient):
    data = dataClient.decode()
    #print(data)
    second = data.splitlines()[1]
    list2 = second.split(":")
    hostname = list2[1].lstrip()
    dst = socket.gethostbyname(hostname) + ":80"
    server_address = ip_to_tuple(dst)
    return server_address

def check_ack(ack, frag):
    contolline = frag.splitlines()[0]
    contolline = contolline.decode()
    contolbits = contolline.split(";")
    f = contolbits[0].split("=")[1]
    seq = contolbits[1].split("=")[1]

    acknum = ack.split("=")[1]

    if int(acknum)-1 == int(seq):
        return True
    else:
        return False

def check_isack(data):
    data = data.decode()
    line = data.splitlines()[0]
    left, sep, right = line.partition("seq=")
    if len(sep) > 0:
        return int(right.strip())
    else:
        return -1

def udp_client(client_socket):
    client_address = None
    while True:
        dataClient, address = client_socket.recvfrom(BUFFER_SIZE)
        print("came from client : ",dataClient.decode())
        if (client_address == None or address != client_address):
            client_address = address
        if check_isack(dataClient) >= 0  :
            counter = counter + 1
            print(counter)
            if (counter == num_frag):
                counter = 0
                continue;

            client_socket.sendto(frags[counter], client_address)
        else:
            dataServer = udp_server( dataInter = dataClient)
            #print("[*] func in <<UDP_CLIENT>> : \n" , dataServer.decode())
            print("[*] fragmantation is starting ...")
            frags = fragmentation(dataServer)
            num_frag = len(frags)
            print("[*] number of frags: " , num_frag)
            counter = 0
            client_socket.sendto(frags[counter], client_address)

        #lots of things to do
        #client_socket.sendto(dataServer, client_address)



def udp_server(dataInter = None):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = retreiveHostname(dataInter)
    server_socket.connect(server_address)
    #print("[*] data sent from <<UDP_server>>:" , dataInter.decode() )
    server_socket.send(dataInter)
    length = 0
    flag = 0
    while True:
        server_socket.send(dataInter)
        dataServer = server_socket.recv(BUFFER_SIZE)
        #print("[**]" , dataServer.decode())
        if flag == 0 :
            CL = serverDataLen(dataServer.decode())
            #print("[*] content length: " , CL)
            flag = 1
        else:
            CL = -1
        print("[*] CL is :" , CL)


        if  ( CL <= 1000 and CL >= 0 ) :
            server_socket.close()
            return dataServer
        else:
            if CL > 1000:
                flag = 1
                length =  CL
                dataFinalarray = bytearray(dataServer)
                print("*******")
            else :
                dataFinalarray= dataFinalarray +  bytearray(dataServer)
                if len(dataFinalarray) >= length:
                    server_socket.close()
                    return dataFinalarray


def udp_proxy(src):
    """Run UDP proxy.

    Arguments:
    src -- Source IP address and port string. I.e.: '127.0.0.1:8000'
    dst -- Destination IP address and port. I.e.: '127.0.0.1:8888'
    """
    LOGGER.debug('Starting UDP-to_TCP proxy...')
    LOGGER.debug('Src: {}'.format(src))
    # LOGGER.debug('Dst: {}'.format(dst))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(ip_to_tuple(src))
    udp_client(client_socket)





def tcp_proxy(src, dst):
    """Run TCP proxy.

    Arguments:
    src -- Source IP address and port string. I.e.: '127.0.0.1:8000'
    dst -- Destination IP address and port. I.e.: '127.0.0.1:8888'
    """
    LOGGER.debug('Starting TCP_to_UDP proxy...')
    LOGGER.debug('Src: {}'.format(src))
    LOGGER.debug('Dst: {}'.format(dst))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.bind(ip_to_tuple(src))
    client_socket.listen(1)
    conn, addr = client_socket.accept()
    server_address = ip_to_tuple(dst)
    global client_address
    client_address = addr

    def client(server_address):
        print("alireza")
        while True:
            dataClient = conn.recv(BUFFER_SIZE)
            print(dataClient.decode())
            server_socket.sendto(dataClient,server_address)
            thread5 = threading.Thread(target = server, args=(client_address,)).start()

    def server(client_address):
        while True:
            data, address = server_socket.recvfrom(BUFFER_SIZE)
            conn.sendall(data)
            break;
    thread4 = threading.Thread(target= client , args=(server_address,)).start()

    LOGGER.debug('Looping proxy (press Ctrl-Break to stop)...')
# end-of-function tcp_proxy








def ip_to_tuple(ip):
    """Parse IP string and return (ip, port) tuple.

    Arguments:
    ip -- IP address:port string. I.e.: '127.0.0.1:8000'.
    """
    ip, port = ip.split(':')
    return (ip, int(port))
# end-of-function ip_to_tuple


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='TCP/UPD proxy.')

    # TCP UPD groups
    proto_group = parser.add_mutually_exclusive_group(required=True)
    proto_group.add_argument('--tcp', action='store_true', help='TCP proxy')
    proto_group.add_argument('--udp', action='store_true', help='UDP proxy')

    parser.add_argument('-s', '--src', required=True, help='Source IP and port, i.e.: 127.0.0.1:8000')
    parser.add_argument('-d', '--dst', required=False, help='Destination IP and port, i.e.: 127.0.0.1:8888')

    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('-q', '--quiet', action='store_true', help='Be quiet')
    output_group.add_argument('-v', '--verbose', action='store_true', help='Be loud')

    args = parser.parse_args()

    if args.quiet:
        LOGGER.setLevel(logging.CRITICAL)
    if args.verbose:
        LOGGER.setLevel(logging.NOTSET)

    if args.udp:
        udp_proxy(args.src)
    elif args.tcp:
        tcp_proxy(args.src, args.dst)
# end-of-function main


if __name__ == '__main__':
    main()