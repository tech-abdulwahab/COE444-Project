from firebase import firebase
import socket

HOST = ''
PORT = 7891

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind((HOST, PORT))
print("Socket bind complete")
s.listen(10)
print("Socket now listening")

conn, addr = s.accept()
s.setblocking(0)

print("Connected with: "+ addr[0]+" : " + str(addr[1]))

firebase = firebase.FirebaseApplication("https://user-firebase-link/", None)



while True:
    data1 = conn.recv(1024)
    d = data1.decode().split(",")


    data = {
            'Email':(d[0]),
            'Day': (d[1])
    }


    result = firebase.post('/user-firebase-link/keys',data)
    print("Data was posted" , result)




