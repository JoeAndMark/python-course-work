import struct


rf = open('bfile.dat', 'rb')
x = rf.read(9)
print(x)
y = struct.unpack('if?', x)
print(y)
x1 = rf.read(12)
print('bin=', x1)
y1 = x1.decode()
print('txt=', y1)
rf.close
