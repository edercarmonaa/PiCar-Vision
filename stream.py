import socket
import os
import time
import picamera

HOST = os.environ.get("STREAM_HOST", "127.0.0.1")
PORT = int(os.environ.get("STREAM_PORT", "8000"))

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(0)
    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()
