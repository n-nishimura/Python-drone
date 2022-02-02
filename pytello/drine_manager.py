import logging
import socket
import sys
import time

from numpy import binary_repr


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class DroneManager(object):
  def __init__(self, host_ip='192.168.10.2', host_port=8889,
              drone_ip='192.168.10.1', drone_port=8889):
      self.host_ip = host_ip
      self.host_port = host_port
      self.drone_ip = drone_ip
      self.drone_port = drone_port
      self.drone_address = (drone_ip, drone_port)
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.socket.bind((self.host_ip,self.host_port))
      self.socket.sendto(b'command')



