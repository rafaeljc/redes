import socket

HOST = '127.0.0.1'
PORT = 65000

dicionario = {
    'propagação' : 'propagation',
    'rede' : 'network',
    'enlace' : 'link',
    'aplicação' : 'application',
    'transporte' : 'transport',
    'atraso' : 'delay',
    'roteador' : 'router',
    'pacote' : 'packet',
    'protocolo' : 'protocol',
    'hospedeiro' : 'host'
}

def run_server():
    print('Servidor UDP iniciado')
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', PORT))
        while True:
            palavra, end_cliente = s.recvfrom(1024)            
            traducao = dicionario.get(palavra.decode())
            if traducao:
                s.sendto(traducao.encode(), end_cliente)
            else:
                s.sendto(b'!ERRO', end_cliente)

def main():
    run_server()

if __name__ == '__main__':
    main()
