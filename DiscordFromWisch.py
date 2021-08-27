  
from vidstream import AudioReceiver
from vidstream import AudioSender

import threading
import socket

receiver = AudioReceiver()
receive_thread = threading.Thread(target=receiver.start_server)

receiver = AudioReceiver()
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender()
sender_thread = threading.Thread(target=sender.start_stream)

sender2 = AudioSender()
sender2_thread = threading.Thread(target=sender2.start_stream)


receive_thread.start()
sender_thread.start()
sender2_thread.start()
