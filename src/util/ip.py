import socket
import ipaddress

def calculate_broadcast_address(mask):
    ip = get_ip_address()
    net = ipaddress.IPv4Network(ip + '/' + mask, False)
    return str(net.broadcast_address)


def get_ip_address():
  hostname = socket.gethostname()
  return socket.gethostbyname(hostname)