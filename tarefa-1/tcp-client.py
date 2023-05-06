import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 65000

palavras = [
    'gato',
    'cachorro',
    'laranja',
    'uva',
    'azul',
    'vermelho',
    'verde',
    'roxo',
    'amarelo',
    'comida',
    'carro'
]

def run_client():
    print('Cliente TCP iniciado')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        palavra = np.random.choice(palavras)
        print(f'Solicitando a tradução de ({palavra})')
        s.sendall(palavra.encode())
        traducao = s.recv(1024)
        traducao = traducao.decode()
        if traducao == '!ERRO':
            print('Não existe tradução para essa palavra')
        else:
            print(f'A tradução é: {traducao}')

def main():
    run_client()

if __name__ == '__main__':
    main()
