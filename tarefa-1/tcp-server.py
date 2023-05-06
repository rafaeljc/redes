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
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f'Conexão estabelecida {addr}')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    traducao = dicionario.get(data.decode())
                    if traducao:
                        conn.sendall(traducao.encode())
                    else:
                        conn.sendall(b'!ERRO')

def main():
    run_server()

if __name__ == '__main__':
    main()
