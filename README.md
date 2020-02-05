# net_scout
  python network scanner
  
  ## Required Modules
  
   #### scapy
    pip3 install scapy
    
   #### progress
    pip3 install progress
    
  ## Functions
      
   ### - net_scan(ip)
   
   ###### Uses the ARP Ping method to discover active hosts on a network. Provide an ip address range including CIDR notation of network. Example: -t 192.168.0.0/24 

   ```
   sudo python3 net_scout.py -t <ip_address_range>
   ```

   ### - port_scan(ip, end_port)

   ###### uses TCP connect scan to find open ports. --port flag is required. Enter a single ip_address for the target using the -t flag. The -m flag is optional. -m indicates max port number you would like to scan up to. Example --> -m 500 will scan ports 1 - 500.
   

   ```
   sudo python3 net_scout.py --port -t <ip_address> -m <max_port_number>
   ```
   
   
      
   + get_arguments()
      
   + print_net_scan()
      
   + print_port_scan()
      
     
