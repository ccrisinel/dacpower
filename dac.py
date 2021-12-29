from fcntl import ioctl

class AptinexDAC(object):
    def __init__(self, address=0x60, bus=1):
        self._addr = address
        self._file = open('/dev/i2c-{0}'.format(bus), 'r+b', buffering=0)

    def disconnect(self):
        self._file.close()

    def set_voltage(self, value, persist=False):
        data = bytearray(3)

        if value > 4095:
            value = 4095
        if value < 0:
            value = 0
        if persist:
            data[0] = 0x60 #EEPROM
        else:
            data[0] = 0x40
        data[1] = (value >> 4) & 0xFF
        data[2] = (value << 4) & 0xFF
        ioctl(self._file.fileno(), 0x0703, self._addr & 0x7F)
        self._file.write(data)



