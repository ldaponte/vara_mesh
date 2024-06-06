
import ax25
import kiss
import socket
import keyboard

host = 'localhost'
kiss_port = 8100
    
k = kiss.TCPKISS('localhost', 8100)

k.start()

c = ax25.Control(frame_type=ax25.FrameType.UI, poll_final=False, recv_seqno=0, send_seqno=0)
message = bytearray('how now brown cow?', encoding='ascii')
f = ax25.Frame(dst='N7BCP-5', src='N7BCP-6', data=message, control=c)

k.write(f)

print('done')
