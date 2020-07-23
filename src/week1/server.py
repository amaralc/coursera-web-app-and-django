# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # The world's Simplest Web Server
# https://www.coursera.org/learn/django-database-web-apps/lecture/vNzDJ/building-a-simple-http-server-in-python

# %%
# Importa tudo da biblioteca socket
from socket import *


# %%
# Define servidor
def createServer():
    # Cria server socket (end point, analogo ao telefone)
    serversocket = socket(AF_INET, SOCK_STREAM)

    # 
    try:
        # Torna socket disponivel na porta 9000 (servico disponivel no 'ramal' 9000 deste servidor)
        # Obs.: apenas um software pode estar 'ouvindo' em cada porta (ou 'ramal')
        serversocket.bind(('localhost',9000))

        # Escuta ate 5 requisicoes (se estiver atendendo a uma, deixe 4 na fila)
        serversocket.listen(5)

        # Executa ciclo de resposta a uma requisicao, encerra a conexao e aguarda nova chamada
        while(1):

            # Aplicacao pronta para atender a requisicoes e aguarda ate chegar uma requisicao
            (clientsocket, adress) = serversocket.accept()

            # Quando alguem faz uma requisicao e accept funcionou ('fone call has been made')
            # Recebe e decodifica de UTF-8 para Unicode
            rd = clientsocket.recv(5000).decode()

            # Divide partes da requisicao por 'new lines'
            pieces = rd.split("\n")

            # Imprime prova de que recebeu as partes
            if( len (pieces) > 0 ): print(pieces[0])
            
            # Constroi resposta (conforme protocolo definido na RFC 2616)
            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            # Envia dados condificados como UTF-8
            clientsocket.sendall(data.encode())

            # Assim que enviar a mensagem, encerra conexao (para os dois lados da conexao)
            clientsocket.shutdown(SHUT_WR)

    # ?
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    # Encerra conexao
    serversocket.close()


# %%
# Cria servidor
print('Access http://localhost:9000')
createServer()