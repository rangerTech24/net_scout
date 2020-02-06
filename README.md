# Net_Scout
  python3 network/port scanner built and tested within ubuntu 18.04.4 using python3.6.9
  
  ## Dependencies
  
   #### scapy
    pip3 install scapy
    
   #### progress
    pip3 install progress
    
   #### yaspin
    pip3 install yaspin
    
   #### figlet
     sudo apt install figlet
    
  ## Functions
      
   ### ---> net_scan(ip, tout)
   
   ###### Uses the ARP Ping method to discover active hosts on a network. Provide an ip address range including CIDR notation of network. -to (timeout) flag is optional; defaults to 5. Example: -t 192.168.0.0/24 -to 10

   ```
   sudo python3 net_scout.py -t <ip_address_range> -to <timeout>
   ```
   
   ### --->  port_scan(ip, end_port)

   ###### Uses TCP connect scan to find open ports. --port flag is required. Enter a single ip_address for the target using the -t flag. The -m flag is optional. -m indicates max port number you would like to scan up to. Example --> -m 500 will scan ports 1 - 500.
   

   ```
   sudo python3 net_scout.py --port -t <ip_address> -m <max_port_number>
   ```
   
   Flag | Name | Scan Type | Optional | Description
   --- | --- | --- | --- | ---
   -m  | MAX | port_scan | yes | a P_S scans from port 1 ---> MAX. Defaults to 1024.
   -t  | TARGET | both | no |N_S targets a range of ips & P_S targets one ip.
   -to | TIMEOUT | net_scan | yes | Timeout of scapy sr1() scan. Defaults to 5 seconds.
   --port | TYPE | port_scan | yes | Tells script to run a P_S.
   
   ### ---> print_net_scan(active_hosts)
   ###### Formats the results of a net_scan.
   
   ### ---> print_port_scan(active_ports)
   ###### Formats the results of port_scan.
      
   ### ---> get_arguments()
   ###### uses argparse module to parse the command line arguments entered when script is executed.
   

      
   
      
   
      
     
