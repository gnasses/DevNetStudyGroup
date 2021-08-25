from netmiko import Netmiko
from ntc_templates.parse import parse_output
import time

mydevice = '192.168.1.57'
mycommand = 'show mac address-table'


#Netmiko classes for all distinct device authentication methods
class CiscoDeviceRO:
    def __init__(self, host, username='devnet', password='student1', device_type='cisco_ios', timeout=90, auth_timeout=90):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.timeout = timeout
        self.auth_timeout = auth_timeout 

class CiscoDeviceRW:
    def __init__(self, host, username='admin', password='cisco123', device_type='cisco_ios', timeout=90, auth_timeout=90):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.timeout = timeout
        self.auth_timeout = auth_timeout 


# Netmiko object and session function 
def cisco_connector(device):        
    try:
        net_device = CiscoDeviceRO(host=device)
        dev_connect = Netmiko(**net_device.__dict__)
        return dev_connect
    except Exception as e:
        ret_error = "Exception found:"+ str(e)
        return  ret_error

#Find OS function to determine NXOS or IOS
def findos(device):        
    try:
        dev_connect = cisco_connector(device)
    except Exception as e:
        ret_error = "Exception found:"+ str(e)
        return  ret_error  
    try:
        show_ver = dev_connect.send_command('show version')
        dev_connect.disconnect()
        if "NX-OS" in show_ver:
            os = "cisco_nxos"
        else:
            os = "cisco_ios"
        return os
    except Exception as e:
        ret_error = "Exception found:"+ str(e)
        return  ret_error  

# # Netmiko connection function leveraging previous session function 
def cisco_command(device, command): 
    try:
        dev_connect = cisco_connector(device)
    except Exception as e:
        ret_error = "Exception found:"+ str(e)
        return  ret_error          
    try:
        os = findos(device)
        #print (os)
        result = dev_connect.send_command(command)
        dev_connect.disconnect()
        #print (command)
        try:
            output = parse_output(platform=os, command=command, data=result)
            return output
        except:
            output = result
            return output
    except Exception as e:
        ret_error = "Exception found:"+ str(e)
        return  ret_error    

#Normal Output
# results = cisco_command(mydevice, mycommand)

# for dic in results:
#     for sub in dic:
#         #print ("MAC Address: " + dic['destination_address'] + "  Port: " + dic['destination_port'])
#         mac = dic['destination_address']
#         port = dic['destination_port']
#         if not port == 'CPU' and 'fcec' in mac:
#             print ('MAC Address: ' + mac + '   Port: ' + port)


#Differential Output
pre_list = []
post_list = []
results = cisco_command(mydevice, mycommand)
for dic in results:
    for sub in dic:
        mac = dic['destination_address']
        port = dic['destination_port']
        entry = {mac : port}
        if not port == 'CPU' and entry not in pre_list:
            pre_list.append(entry)  
            #print ('MAC Address: ' + mac + '   Port: ' + port)
print ('Pausing 45 seconds!!!!!!!')            
time.sleep(45)

post_results = cisco_command(mydevice, mycommand)
for dic in post_results:
    for sub in dic:
        mac = dic['destination_address']
        port = dic['destination_port']
        entry = {mac : port}
        if not port == 'CPU' and entry not in post_list:
            post_list.append(entry)  
            #print ('MAC Address: ' + mac + '   Port: ' + port)

adds = [x for x in post_list if x not in pre_list]
subs = [x for x in pre_list if x not in post_list]

print ("Pre-List:")
print (pre_list)
print ()
print ("Post-List:")
print (post_list)
print ()
print ("Added Entries: ")
print (adds)
print ()
print ("Removed Entries: ")
print (subs)
print ()
