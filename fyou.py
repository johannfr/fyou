#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import SocketServer

class SerialRequestServer(SocketServer.TCPServer):
    def __init__(
        self,
        server_address,
        RequestHandlerClass,
        serial_port
    ):
        SocketServer.TCPServer.__init__(
            self,
            server_address,
            RequestHandlerClass
        )
        self.serial_port = serial_port



class SerialRequestHandler(SocketServer.StreamRequestHandler):
    """
    Handles incoming connections and forwards everything to serial port
    """

    def handle(self):
        while True:
            incoming = self.request.recv(1024)
            if not incoming:
                break
            incoming = incoming.strip()
            self.server.serial_port.write("%s\n"%incoming)

if __name__ == "__main__":

    serial_port = serial.Serial("/dev/ttyUSB0", baudrate=9600)

    SocketServer.TCPServer.allow_reuse_address = True
    server = SerialRequestServer(
            (
                "localhost",
                7989
            ),
            SerialRequestHandler,
            serial_port
        )
    server.serve_forever()

