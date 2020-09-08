from multiprocessing import Process
from socket import socket, AF_INET, SOCK_STREAM
from json import loads as load

class PacketProcess(Process):
    """
    The Process that listens for Packets being sent to the application's
    Socket and then adds the packet to the processing queue.

    :param host: The IP Address the PacketProcess is going to listen on.
    :param port: The Port the PacketProcess is going to listen on.
    :param queue: The queue the PacketProcess adds the packets to.
    """
    def __init__(self, application, host, port, *args, **kargs):
        self.application = application
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, port))

        super().__init__(target=self.process_packets)

    def process_packets(self):
        """
        Listen for a packet and processes the packet.
        """
        while True:
            self.socket.listen()
            conn, addr = self.socket.accept()
            data = conn.recv(1024)
            print(f"""Received Packet: {data}""")
            self.application.add_event(load(data))

    def run_event(self, event):
        """
        Executes the event.

        :param event: The event to be executed.
        """
        pass

    def close(self):
        self.socket.close()

