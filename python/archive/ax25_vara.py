
import ax25
import kiss
import socket
import keyboard

host = 'localhost'
kiss_port = 8100
# data_port = 8301

'''
data_socket = socket.socket()

data_socket.bind((host, kiss_port))

data_socket.listen(1)

c, address = data_socket.accept()

while True:

    vara_data = c.recv(1024)

    if not vara_data:
        break
    
    ax25_frame = ax25.Frame.unpack(vara_data)

    print("dst={}, src={}, data={}".format(ax25_frame.dst, ax25_frame.src, ax25_frame.data))


'''

def kiss_read(payload):
    f = ax25.Frame.unpack(payload)
    print("dst={}, src={}, data={}".format(f.dst, f.src, f.data))
    
k = kiss.TCPKISS('localhost', 8100)

k.start()

# k.read(callback=kiss_read)

frame_count = 0

while True:
    frames = k.read()
    fram_count = frame_count + 1

    if(len(frames) > 0):
        print('got a frame')
        frame = frames[0][1:]
        f = ax25.Frame.unpack(frame)
        print("dst={}, src={}, data={}, control={}".format(f.dst, f.src, f.data, f.control))

    # print(len(frames))
'''
while True:
    if keyboard.read_key() == 'space':
        break
'''

print('done')
