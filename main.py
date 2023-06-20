import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port,):
    try:
        sockt = socket.socket()
        sockt.connect((ipaddress, port))
        print(ipaddress + " : [+] open : " + str(port))
        sockt.close()
    except:
        pass

targets = input("[>] Target/s - comma separated : ")
ports = int(input("[>] Number of ports : "))

if ',' in targets:
    print("[*] Scanning multiple targets.")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)