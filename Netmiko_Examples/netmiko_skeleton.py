from netmiko import Netmiko
from ntc_templates.parse import parse_output

mydevice = '192.168.1.57'
mycommand = 'show mac address-table'

class CiscoDeviceRO:
    def __init__(self, host, username='devnet', password='student1', device_type='cisco_ios', timeout=90, auth_timeout=90):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.timeout = timeout
        self.auth_timeout = auth_timeout 

net_device = CiscoDeviceRO(host=mydevice)

dev_connect = Netmiko(**net_device.__dict__)

# result = dev_connect.send_command(mycommand)
# dev_connect.disconnect()
# print (result)

show_ver = dev_connect.send_command('show version')
if "NX-OS" in show_ver:
    os = "cisco_nxos"
else:
    os = "cisco_ios"
 
result = dev_connect.send_command(mycommand)
dev_connect.disconnect()

output = parse_output(platform=os, command=mycommand, data=result)
print (output)
