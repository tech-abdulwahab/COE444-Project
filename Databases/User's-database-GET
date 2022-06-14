from firebase import firebase
import socket


HOST = ''
PORT = 2345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind((HOST, PORT))
print("Socket bind complete")
s.listen(10)
print("Socket now listening")

conn, addr = s.accept()
s.setblocking(0)
 
print("Connected with: "+ addr[0]+" : " + str(addr[1]))


 
firebase1 = firebase.FirebaseApplication("https://MOH-firebase-link/", None)
firebase2 = firebase.FirebaseApplication("https://alis-firebase-link/", None)

while True:
    data = conn.recv(1024)
    if ( str(data) == "b'1023'"):
        MOH = firebase1.get('keys/', None)
        AliDB = firebase2.get('keys/', None)



        for key in MOH.keys():
            if(MOH[key]['Email'] == 'ali@gmail.com'):
                print("Verification successed")
                for key in AliDB.keys():
                    print((AliDB[key]['Email'] + ',' + AliDB[key]['Day']))
                    conn.send((AliDB[key]['Email'] + ',' + AliDB[key]['Day']).encode())

        for key in MOH.keys():
            if(MOH[key]['Email'] != 'ali@gmail.com'):
                print("Verification failed")



