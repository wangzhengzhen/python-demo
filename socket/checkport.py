#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket, sys

socket.setdefaulttimeout(3)

def check_port(ip, port):
  port_status = -1
  try:
      s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      r=s.connect_ex((ip, port))
      if r == 0:
          port_status = 1
      else:
          port_status = 0
      s.close()
  except:
      print("Unexpected error:", sys.exc_info())
  return port_status


ip = sys.argv[1]
port = int(sys.argv[2])
cr = check_port(ip, port)
if cr == 1:
  print(ip+':'+str(port)+'端口已占用')
elif cr == 0:
  print(ip+':'+str(port)+'端口未使用')
else:
  print(ip+':'+str(port)+'端口扫描异常')
