from netmiko import Netmiko
from ntc_templates.parse import parse_output

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
        
# Netmiko  session function 
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
