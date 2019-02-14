#!/bin/python3.7
# -*- coding: utf-8 -*-

"""
This file is the BeagleBone Enhanced Serial/UART setup and interface code.

It is responsible for configuring the UART1 TX/RX pins and exporting a usable
BeagleBoneSerial object importable by other files.
"""

import serialbase
import serial  # pip package pyserial


class BeagleBoneSerial (serialbase.SerialInterface):
    """
    The PlatformSerial class is responsible for interfacing with
    the serial pins and exposing a usable interface with the methods
    defined in serialbase.SerialInterface.
    """

    def __init__(self, name: str):
        """
        Create the BeagleBone serial object and set the appropriate settings.
        :param name: the name of the serial interface.
        """

        super(BeagleBoneSerial, self).__init__(name)

        self.pins = {"TX": 24,
                     "RX": 26,
                     "Vcc": 3,
                     "GND": 1
                     }

        self._serial = serial.Serial("/dev/ttyO1",
                                     baudrate=self.baudrate,
                                     timeout=0,
                                     parity=serial.PARITY_NONE,
                                     stopbits=1,
                                     )

    def read_serial_data(self):
        """
        Read all available data from the wire and write it to buffer.

        :return: nothing
        """
        readin = self._serial.readall()
        self.write_to_buffer(readin)
