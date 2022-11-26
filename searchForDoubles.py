import struct

import bitstream

from bitstream import BitStream
import numpy as np

with open('01-GM8P-MetroidPrime_01.gci', 'rb') as f:
# with open('01-GM8E-MetroidPrime A.orig.gci', 'rb') as f:
    data = f.read()


def find_offset(hours, minutes):
    bs = BitStream(data)
    min = hours * 60 * 60 + minutes * 60
    max = hours * 60 * 60 + minutes * 60 + 60
    print(f"Searching between {min} and {max} seconds")
    start = 0
    for i in range(0, len(data) * 8):
        start = start << 1 | bs.read(bool)
        start = start & 0xFFFFFFFF_FFFFFFFF
        double = struct.unpack('>d', bytes(start.to_bytes(8, 'big')))[0]
        if min < double < max:
            offset = i - 64
            print(offset, double, f"{int(offset/8)}.{offset%8}", struct.pack(">d", double).hex())


find_offset(1, 4)
find_offset(3, 46)
find_offset(2, 10)