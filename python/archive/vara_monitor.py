# Streaming Client
import socket

HOST = 'localhost'
PORT = 8100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# while True:
    


    # i = input('enter somethjing:')
    # s.sendall(i.encode('utf-8'))

    # data = s.recv(1024)
    # print (repr(data))

# m = bytearray()
# m = bytearray(b'\xc0\x00\x74\x65\x73\x74\xc0')

# m = bytearray(b'\xC0\x02\x4E\x6F\x74\x42\x6C\x61\x63\x6B\x4D\x61\x67\x69\x63\xC0') # working!!


m = bytearray(b'\xc0\x00\x82\xa0\x92\x9c\x64\x62\x60\x9c\x6e\x84\x86\xa0\x40\x60\xae\x92\x88\x8a\x62\x40\x62\xae\x92\x88\x8a\x64\x40\x63\x03\xf0\x21\x33\x39\x32\x32\x2e\x37\x39\x4e\x2f\x31\x30\x34\x35\x31\x2e\x33\x36\x57\x3e\x50\x69\x6e\x50\x6f\x69\x6e\x74\x20\x76\x32\x2e\x31\xc0')



#m.append(0xc0)
#m.append(0x00)
#m.append(0x74)
#m.append(0x65)
#m.append(0x73)
#m.append(0x74)
#m.append(0xc0)

s.send(m)

s.close()
