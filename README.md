# net_scout
  python network scanner
  
  ## Required Modules
  
   #### scapy
    pip3 install scapy
    
   #### progress
    pip3 install progress
    
  ## Functions
      
   ### - net_scan(ip)
   
   ###### Uses the ARP Ping method to discover active hosts on a network. 
   ```
   sudo python3 net_scout.py -t <ip_address_range>
   ```
   ### - port_scan(ip, end_port)
   
   ###### uses TCP connect scan to find open ports
      
   + get_arguments()
      
   + print_net_scan()
      
   + print_port_scan()
      
     
