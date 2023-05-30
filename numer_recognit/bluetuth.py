import socket 

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

IP = '64:6e:69:cb:da:32'
PORT = 4

server.bind((IP, PORT))


server.listen(5)


try: 
    while True:
        client, add = server.accept()
        
        print(client)

        data = client.recv(1024).decode('UTF-8')

        if not data:
            print("No message !!!")
            break

        print("Message: ", data)

        message = input("enter message: ")

        client.send(message.encode('UTF-8'))

except Exception as ex:
    print(ex)

client.close()
server.close()


