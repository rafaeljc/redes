import socket

HOST = '127.0.0.1'
PORT = 65000

dicionario = {
    'gato' : 'cat',
    'cachorro' : 'dog',
    'laranja' : 'orange',
    'uva' : 'grape',
    'azul' : 'blue',
    'vermelho' : 'red',
    'verde' : 'green',
    'roxo' : 'purple',
    'amarelo' : 'yellow',
    'comida' : 'food'
}

def run_server():
    print('Servidor UDP iniciado')
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('', PORT))
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
