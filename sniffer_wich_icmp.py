import ipaddress
import os
import socket
import struct
import sys

###class IP:
    # -- Snip --



#class ICMP:
   # def __init__(self, buff):
        #header = struct.unpack('BBHHH', buff)
        #self.type = header[0]
        #self.code = header[1]
        #self.sum = header[2]
       # self.id = header[3]
        #self.seq = header[4]
        
#def sniff(host):
 #   ip_header = IP(raw_buffer[0:20])
  #  if ip_header.protocol == "ICMP":
 #       print('Protocol: %s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
  #      print(f'Version: {ip_header.ver}')