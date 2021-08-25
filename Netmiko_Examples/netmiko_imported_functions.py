from netmiko import Netmiko
import time
import util

mydevice = '192.168.1.57'
mycommand = 'show mac address-table'

results = util.cisco_command(mydevice, mycommand)

for dic in results:
    for sub in dic:
        #print ("MAC Address: " + dic['destination_address'] + "  Port: " + dic['destination_port'])
        mac = dic['destination_address']
        port = dic['destination_port']
        if not port == 'CPU' and 'fcec' in mac:
            print ('MAC Address: ' + mac + '   Port: ' + port)


#Differential Output
# pre_list = []
# post_list = []
# results = util.cisco_command(mydevice, mycommand)
# for dic in results:
#     for sub in dic:
#         mac = dic['destination_address']
#         port = dic['destination_port']
#         entry = {mac : port}
#         if not port == 'CPU' and entry not in pre_list:
#             pre_list.append(entry)  
#             #print ('MAC Address: ' + mac + '   Port: ' + port)
# print ('Pausing 45 seconds!!!!!!!')            
# time.sleep(45)

# post_results = util.cisco_command(mydevice, mycommand)
# for dic in post_results:
#     for sub in dic:
#         mac = dic['destination_address']
#         port = dic['destination_port']
#         entry = {mac : port}
#         if not port == 'CPU' and entry not in post_list:
#             post_list.append(entry)  
#             #print ('MAC Address: ' + mac + '   Port: ' + port)

# adds = [x for x in post_list if x not in pre_list]
# subs = [x for x in pre_list if x not in post_list]

# print ("Pre-List:")
# print (pre_list)
# print ()
# print ("Post-List:")
# print (post_list)
# print ()
# print ("Added Entries: ")
# print (adds)
# print ()
# print ("Removed Entries: ")
# print (subs)
# print ()
