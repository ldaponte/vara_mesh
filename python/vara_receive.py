
import ax25
import kiss

host = 'localhost'
kiss_port = 8100

def kiss_read(payload):
    f = ax25.Frame.unpack(payload)
    print("dst={}, src={}, data={}".format(f.dst, f.src, f.data))
    
k = kiss.TCPKISS('localhost', 8100)

k.start()

frame_count = 0

while True:
    frames = k.read()
    fram_count = frame_count + 1

    if(len(frames) > 0):
        print('got a frame')
        frame = frames[0][1:]
        f = ax25.Frame.unpack(frame)
        print("dst={}, src={}, data={}, data_size={}, control={}".format(f.dst, f.src, f.data, len(f.data), f.control))

print('done')
