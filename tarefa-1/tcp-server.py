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
    print('Servidor TCP iniciado')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:            
            conexao, end_cliente = s.accept()
            with conexao:
                print(f'Conexão estabelecida {end_cliente}')
                data = conexao.recv(1024)
                traducao = dicionario.get(data.decode())
                if traducao:
                    conexao.sendall(traducao.encode())
                else:
                    conexao.sendall(b'!ERRO')

def main():
    run_server()

if __name__ == '__main__':
    main()
