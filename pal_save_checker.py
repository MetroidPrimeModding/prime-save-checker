import struct
import sys


def convert_offset(offset):
    return int(offset / 8), int(offset % 8)

file = sys.argv[1]

if not file.endswith('.gci'):
    print('Not a GCI file')
    sys.exit(1)

with open(file, 'rb') as f:
    time1offset = convert_offset(133705)
    time2offset = convert_offset(155201)
    time3offset = convert_offset(176697)

    f.seek(time1offset[0])
    time1bytes = f.read(9) # 40ae1806e4790000
    time1 = int.from_bytes(time1bytes, 'big')
    f.seek(time2offset[0])
    time2bytes = f.read(9) # 40ca7e3847fc3000
    time2 = int.from_bytes(time2bytes, 'big')
    f.seek(time3offset[0])
    time3bytes = f.read(9) # 40beae401ad87800
    time3 = int.from_bytes(time3bytes, 'big')

    time1 = (time1 >> (7 - time1offset[1])) & 0xFFFFFFFF_FFFFFFFF
    time2 = (time2 >> (7 - time2offset[1])) & 0xFFFFFFFF_FFFFFFFF
    time3 = (time3 >> (7 - time3offset[1])) & 0xFFFFFFFF_FFFFFFFF

    time1 = struct.unpack('>d', bytes(time1.to_bytes(8, 'big')))[0]
    time2 = struct.unpack('>d', bytes(time2.to_bytes(8, 'big')))[0]
    time3 = struct.unpack('>d', bytes(time3.to_bytes(8, 'big')))[0]

    print(f"Save 1: {time1} seconds: {int(time1 / 60 / 60)}:{int(time1 / 60 % 60):02}:{int(time1 % 60):02}")
    print(f"Save 2: {time2} seconds: {int(time2 / 60 / 60)}:{int(time2 / 60 % 60):02}:{int(time2 % 60):02}")
    print(f"Save 3: {time3} seconds: {int(time3 / 60 / 60)}:{int(time3 / 60 % 60):02}:{int(time3 % 60):02}")

input("Press enter to close...")