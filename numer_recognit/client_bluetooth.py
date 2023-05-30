import socket 

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

IP = '64:6e:69:cb:da:32'
PORT = 4

client.connect((IP, PORT))

client.send("Hello".encode('UTF-8'))

try: 
    while True:

        data = client.recv(1024).decode('UTF-8')

        if not data:
            print("No message !!!")
            break

        print("Message: ", data)

        message = input("enter message: ")

        client.send(message.encode('UTF-8'))

except Exception as ex:
    print(ex)
