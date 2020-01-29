#!/usr/bin/env python3
import os
import scapy.all as scapy




'''
pdst:  destination ip address
arp_request: create ARP object.
dst: broadcast mac address. 
ff:ff:ff:ff:ff:ff is default value
broadcast: create ethernet object
'''

#* sends ARP packets to multiple hosts and returns a dictionary of responses
def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    responses = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    active_hosts = []
    for element in responses:
        host_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        active_hosts.append(host_dict)
    return active_hosts


def portScanner(ip, end_port):
    port = 1
    port_list = []

    while port <= end_port:
       target_ip = scapy.IP(dst=ip)
       target_port = scapy.TCP(dport=port,flags="S")
       syn_packet = target_ip/target_port
       resp = scapy.sr1(syn_packet)
       resp = resp.sprintf('%IP.src%\t%TCP.sport%\t%TCP.flags%')
       resp = resp.replace('SA', 'OPEN')
       ip_addr, port_name, status = resp.split('\t')
       resp_dict={"ip": ip_addr, "port": port_name, "status": status}
       port_list.append(resp_dict)
       port = port + 1
    
    return port_list
      




#* formats the scan results for the user
def print_ipScan(active_hosts):
    print(active_hosts)
    print("\n\nIP\t\t\tMAC Address")
    print("------------------------------------------")
    for host in active_hosts:
        print(host["ip"] + "\t\t" + host["mac"])

#todo set up to format the port list
def print_portScan(port_list):
    print("\n\nIP\t\t\tPort\t\t\tStatus")
    print("------------------------------------------")
    for port in active_ports:
        print(port["ip"] + "\t\t" + port["port"] + "\t\t" + port["status"])

'''
def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target",help="Target IP/IP Range")
        options = parser.parse_args()
        return options
'''


os.system('clear')
os.system('figlet "Net Scout" -f slant')
print("------------------------------------------\n\n\n\n")
target = input("\tEnter a target IP range: ")
scanner = scan(target)
print_ipScan(scanner)
portScanner("192.168.0.190", 100)
print(print_portScan)











