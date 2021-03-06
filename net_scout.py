#!/usr/bin/env python3
import os
import scapy.all as scapy
from progress.bar import IncrementalBar
from yaspin import yaspin
import argparse


def net_scan(ip, tout):  #Scans network for active hosts 
     
    spinner = yaspin(text="Scanning Network", color="green")
    spinner.start()
    active_hosts = [] 
    arp_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)
    responses = scapy.srp(arp_packet, timeout=tout, verbose=False)[0] 
    #responses.summary()  #print test to show arp broadcast  
    for element in responses:  #Parses through each element in responses and saves the IP and MAC values to host_dict
        host_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        active_hosts.append(host_dict)
    spinner.stop()
    return active_hosts


def port_scan(ip, end_port):  #Sends SYN packets to specified port numbers and looks for SYN-ACK responses to indicate open ports
    port = 1
    port_list = []
    active_ports = []
    with IncrementalBar("scanning ports...",index=port,max=end_port,suffix='%(percent)d%%') as bar:
        while port <= end_port:
            #syn_packet.show()
            syn_packet = scapy.sr1(scapy.IP(dst=ip)/scapy.TCP(dport=port,flags="S"),verbose=0, timeout=.05) 
            if(str(type(syn_packet))!="<class 'scapy.layers.inet.IP'>"):
                port = port + 1
                bar.next()
                continue
            resp = syn_packet.sprintf('%IP.src%\t%TCP.sport%\t%TCP.flags%')
            #print(resp)
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


def print_net_scan(active_hosts):  #prints net_scan() results to command line.
    host_num = 0
    print("\n\nIP\t\t\tMAC Address")
    print("------------------------------------------")
    for element in active_hosts:
        print(element["ip"] + "\t\t" + element["mac"])
        host_num = host_num + 1
    print("------------------------------------------")
    print("\t---> Active hosts discovered:", host_num)
    print("\t---> Scan Complete\n")


def print_port_scan(active_ports):  #prints port_scan() results to command line.
    print("\n\nIP\t\t\tPort\t\tStatus")
    print("-----------------------------------------------")
    for element in active_ports:
        if element == "None":
            print("Scan Complete")
        else:
            print(element["ip"] + "\t\t" + element["port"] + "\t\t" + element["status"])


def get_arguments():  #parses the command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", dest="type", action="store_true", default="False", help="The -ps flag is used to run a port scan | default=false")
        parser.add_argument("-t", dest="target", help="Target IP range ---> [192.168.0.1/24] or single host for port scan [192.168.0.1] **")
        parser.add_argument("-m", dest="max", default="1024", type=int, help="Max port to scan | default=1024")
        parser.add_argument("-to", dest="timeout", default="5", type=int, help="timeout of scan")
        options = parser.parse_args()
        return options


os.system('clear')
os.system('figlet Net Scout')
print("---------------------------------------------\n")
options = get_arguments()
if options.type == "False":
    scanner = net_scan(options.target, options.timeout)
    print_net_scan(scanner)
else:
    Pscanner = port_scan(options.target, options.max)
    print(print_port_scan(Pscanner))







