#!/usr/bin/env python3
import os
import scapy.all as scapy
from progress.bar import IncrementalBar
import argparse

def scan(ip): #Info: Scans network for active hosts   
    active_hosts = [] 
    arp_broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)
    responses = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]     
    for element in responses: # Parses through each element in responses and saves the IP and MAC values to host_dict
        host_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        active_hosts.append(host_dict)
    return active_hosts

def portScanner(ip, end_port): #Info: Sends SYN packets to specified port numbers and looks for SYN-ACK responses to indicate open ports
    port = 1
    port_list = []
    active_ports = []
    with IncrementalBar("scanning ports...", index=port,max=end_port, suffix='%(percent)d%%') as bar:
        while port <= end_port:
            syn_packet = scapy.IP(dst=ip)/scapy.TCP(dport=port,flags="S")
            resp = scapy.sr1(syn_packet, verbose=0, timeout=1)
            if resp is None: #error checking for resp timeouts
                continue
            resp = resp.sprintf('%IP.src%\t%TCP.sport%\t%TCP.flags%')
            resp = resp.replace('SA', 'OPEN')
            ip_addr, port_name, status = resp.split('\t')
            resp_dict={"ip": ip_addr, "port": port_name, "status": status}
            port_list.append(resp_dict)
            bar.next()
            port = port + 1

    for element in port_list:
        if element.get("status") == "OPEN":
            active_ports.append(element)
    return active_ports

def print_ipScan(active_hosts): # prints IP scan results to command line.
    print("\n\nIP\t\t\tMAC Address")
    print("------------------------------------------")
    for element in active_hosts:
        print(element["ip"] + "\t\t" + element["mac"])

def print_portScan(active_ports): # prints port scan results to command line.
    print("\n\nIP\t\t\tPort\t\tStatus")
    print("-----------------------------------------------")
    for element in active_ports:
        if element == "None":
            print("Scan Complete")
        else:
            print(element["ip"] + "\t\t" + element["port"] + "\t\t" + element["status"])

def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", dest="type", action="store_true", default="False", help="The -ps flag is used to run a port scan | default=false")
        parser.add_argument("-t", dest="target", help="Target IP range ---> [192.168.0.1/24] | ** do not include CIDR notation when running a port scan **")
        parser.add_argument("-m", dest="max", default="1024", type=int, help="Max port to scan | default=1024")
        options = parser.parse_args()
        return options

os.system('clear')
os.system('figlet Net Scout')
print("---------------------------------------------\n")
options = get_arguments()
if options.type == "False":
    scanner = scan(options.target)
    print_ipScan(scanner)
else:
    Pscanner = portScanner(options.target, options.max)
    print(print_portScan(Pscanner))







