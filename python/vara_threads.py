import ax25
import kiss
import threading

host = 'localhost'
kiss_port = 8100

rx_queue = []

first = True

k = kiss.TCPKISS(host, kiss_port)

k.start()

def receive_process(parameter):

    print('Starting receive process...')

    while True:
        frames = k.read()

        if(len(frames) > 0):

            for frame in frames:
  
                frame = frame[1:]
                f = ax25.Frame.unpack(frame)
                print("dst={}, src={}, data={}, data_size={}, control={}".format(f.dst, f.src, f.data, len(f.data), f.control))

                transmit_process(f.src)

def transmit_process(parameter):

    if parameter not in rx_queue:

        rx_queue.append(parameter)

        c = ax25.Control(frame_type=ax25.FrameType.UI, poll_final=False, recv_seqno=0, send_seqno=0)

        message_string = ",".join(str(heard) for heard in rx_queue)
        message = bytearray(message_string, encoding='ascii')

        f = ax25.Frame(dst='APZVARA', src='N7BCP-6', data=message, control=c)

        print('Sending: ' + message)

        k.write(f)


# transmit_thread = threading.Thread(target=transmit_process, args=('randome parameter',))
# transmit_thread.start()

receive_thread = threading.Thread(target=receive_process, args=('randome parameter',))
receive_thread.start()

if first:
    transmit_process('K7MHJ-1')

# transmit_thread.join()
receive_thread.join()

print('Done')