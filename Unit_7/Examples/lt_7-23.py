import struct


a = 20
b = 3.14
c = True
d = '我爱Python！'
sn = struct.pack('if?', a, b, c)
wf = open('bfile.dat', 'wb')
wf.write(sn)
wf.write(d.encode())
wf.close()
