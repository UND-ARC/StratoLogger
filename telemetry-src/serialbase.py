#!/bin/python3.7
# -*- coding: utf-8 -*-

"""
This file is responsible for providing a basic SerialInterface object that can
be used by other programs to read serial data in an easier manner.
"""

from typing import List

STRATOLOGGER_LINEFEED = '\r\n'
UNIX_LINEFEED = '\n'


class SerialInterface (object):
    """
    The SerialInterface class is a user-land interface to a serial port on
    either the BeagleBone Enhanced or Raspberry Pi 3B+.
    """

    def __init__(self, name: str):
        """Create a SerialInterface object.

        :param name: str: the name of the interface.
        """
        self.name: str = name
        self.pins: dict = {"RX": -1,
                           "TX": -1,
                           "Vcc": -1,
                           "GND": -1,
                           }
        self.baudrate: int = 115200  # decently safe default, changeable later
        self.stopbits: int = 1
        self.parity: str = 'even'

        self.serial_buffer: str = ""

    def write_to_buffer(self, chars: str):
        """
        Appends the characters to the internal serial data buffer.

        :param chars: characters to add
        :return: nothing
        """
        self.serial_buffer += chars

    def read_buffer_no_overwrite(self):
        """
        Returns the current status of the serial buffer, but does *NOT*
        empty it.  For that case, use the method

            read_buffer()

        :return: a string representing the current buffer
        """
        return self.serial_buffer

    def read_buffer(self):
        """
        Returns the buffer, and empties it.

        :return: the current serial data buffer.
        """
        bufcpy = self.serial_buffer
        self.serial_buffer = ""
        return bufcpy

    def normalize_altitudes(self):
        """
        This method returns a list of integers that represents the
        output data from the PerfectFlite StratoLogger altimeter.

        It is effectively a data parser for the serial buffer, and requires that
        the buffer not be empty.  It does *NOT* empty the serial buffer.

        :return: a list of integers
        """

        assert self.serial_buffer != "", "Cannot parse empty data"
        altitudes: List[int] = []

        # read the buffer, nondestructively, and replace CRLF with LF
        clean_buffer: str = self.read_buffer_no_overwrite().replace(
            STRATOLOGGER_LINEFEED, UNIX_LINEFEED
        )

        for line in clean_buffer.splitlines():
            clean_line: str = line.strip()
            try:
                alt = int(clean_line)
                altitudes.append(alt)
            except ValueError:
                # error converting to int
                # TODO: handle error somehow instead of skipping
                pass

        return altitudes

