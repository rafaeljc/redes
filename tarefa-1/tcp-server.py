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
    print('Servidor TCP iniciado')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
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
