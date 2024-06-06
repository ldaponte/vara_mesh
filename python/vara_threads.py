import ax25
import kiss
import threading
import random
import time
import keyboard

version = 1

host = 'localhost'
kiss_port = 8100

rx_queue = []

exit_app = False

max_sleep = 5

lock = threading.Lock()

k = kiss.TCPKISS(host, kiss_port)

k.start()

def receive_process(parameter):

    print('\nStarting receive process...')

    while True:

        if exit_app:
            print('\nStopping receive loop...')
            break

        frames = k.read()

        if(len(frames) > 0):

            for frame in frames:
  
                frame = frame[1:]
                f = ax25.Frame.unpack(frame)
                print("\ndst={}, src={}, data={}, data_size={}, control={}".format(f.dst, f.src, f.data, len(f.data), f.control))

                transmit_process(str(f.src))

def transmit_process(parameter=None):

    with lock:

        if parameter not in rx_queue:

            sleep_time = random.uniform(1, max_sleep)
            print('\npause before transmit: ' + str(sleep_time) + ' seconds...')

            time.sleep(sleep_time)

            if parameter is not None:
                rx_queue.append(parameter)

            c = ax25.Control(frame_type=ax25.FrameType.UI, poll_final=False, recv_seqno=0, send_seqno=0)

            message_string = ",".join(str(heard) for heard in rx_queue)
            message = bytearray(message_string, encoding='ascii')

            f = ax25.Frame(dst='APZVA-0', src='N7BCP-6', data=message, control=c)

            print('\nSending: ' + message_string)

            k.write(f)


receive_thread = threading.Thread(target=receive_process, args=('randome parameter',))
receive_thread.start()

transmit_process()

while True:

    key = keyboard.read_key()

    if key == 'esc':
        exit_app = True
        break

receive_thread.join()

print('\nDone')