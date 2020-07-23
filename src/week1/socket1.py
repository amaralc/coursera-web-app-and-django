# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Building a Simple Web Broser in Python
#  https://www.coursera.org/learn/django-database-web-apps/lecture/alKDL/building-a-simple-web-browser-in-python

# %%
# Import socket library
import socket


# %%
# Cria socket (end point) atraves de metodo socket da biblioteca socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Realiza conexao (entre end points), partindo do socket, para o dominio e porta definidos
mysock.connect(('data.pr4e.org',80))

# Define comando que se deseja enviar, utilizando protocolo HTTP 1.0 (conforme RFC), e codifica de Unicode para UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Envia comando atraves do socket
mysock.send(cmd)

# Recebe dado ate que socket seja fechado (conforme definido no protocolo HTTP)
while True:

    # Recebe dados ate 512 caracteres por loop
    data = mysock.recv(512)

    # Se nao receber dados, significa que a conexao foi encerrada pelo servidor remoto
    if len(data) <1:

        # Encerra loop
        break

    # Imprime dados, decodificados de UTF-8 para Unicode
    print(data.decode(),end='')

# Encerra conexao
mysock.close()


