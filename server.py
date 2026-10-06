import socket
import cv2
import pickle
import os
import struct

HOST = os.environ.get("FRAME_SERVER_HOST", "127.0.0.1")
PORT = int(os.environ.get("FRAME_SERVER_PORT", "8089"))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created')

s.bind((HOST,PORT))
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')

conn,addr=s.accept()

### new
data = b""
payload_size = struct.calcsize("H")
while True:
    while len(data) < payload_size:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    if len(data) < payload_size:
        break
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("H", packed_msg_size)[0]
    while len(data) < msg_size:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    if len(data) < msg_size:
        break
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

conn.close()
s.close()
cv2.destroyAllWindows()
