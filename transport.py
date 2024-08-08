
import random

class GoBackNProtocol:
    def __init__(self, window_size):
        self.window_size = window_size
        self.next_seq_num = 0
        self.base = 0
        self.buffer = {}
        self.ack_received = {}
    
    def send(self, data):
        if self.next_seq_num < self.base + self.window_size:
            self.buffer[self.next_seq_num] = data
            self.ack_received[self.next_seq_num] = False
            self.send_segment(self.next_seq_num, data)
            self.next_seq_num += 1
        else:
            print("Window is full. Cannot send more data.")
    
    def receive_ack(self, ack_num):
        if ack_num in self.ack_received:
            self.ack_received[ack_num] = True
            while self.base in self.ack_received and self.ack_received[self.base]:
                del self.buffer[self.base]
                del self.ack_received[self.base]
                self.base += 1
    
    def send_segment(self, seq_num, data):
        
        print(f"Sending segment {seq_num}: {data}")
    
    def receive_segment(self, seq_num, data):
      
        print(f"Received segment {seq_num}: {data}")
        self.receive_ack(seq_num)

class PortManager:
    def __init__(self):
        self.well_known_ports = {i: None for i in range(1, 1024)}
        self.ephemeral_ports = {i: None for i in range(49152, 65536)}
    
    def assign_port(self, process_name, well_known=False):
        if well_known:
            for port, proc in self.well_known_ports.items():
                if proc is None:
                    self.well_known_ports[port] = process_name
                    return port
        else:
            port = random.choice(list(self.ephemeral_ports.keys()))
            while self.ephemeral_ports[port] is not None:
                port = random.choice(list(self.ephemeral_ports.keys()))
            self.ephemeral_ports[port] = process_name
            return port
    
    def release_port(self, port):
        if port in self.well_known_ports:
            self.well_known_ports[port] = None
        elif port in self.ephemeral_ports:
            self.ephemeral_ports[port] = None
