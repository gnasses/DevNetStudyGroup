"""
Network Python Scripting Simple Example

These are lists of strings with fake network device information to use in our program. 
Run the script first without modification first to make sure it succeeds in creating these variables and does not show errors. 
If it cannot run at all, your python environment may not be working or you may have a syntax problem. 
"""

switches = ['spine01', 'spine02', 'leaf03', 'leaf04', 'leaf05', 'leaf06']
mgmt_ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6']
vlans = ['101', '102', '103', '104', '105', '106']
int_addresses = ['172.16.1.1', '172.16.1.2', '172.16.1.3', '172.16.1.4', '172.16.1.5', '172.16.1.6']



# Step 1: Uncomment The following section, and re-run to print items from your devices list. Recomment this section when finished. 
# Note: Adding a '#' character in front of a line indicates that line is a comment, removing the '#' uncomments the line 

# for s in switches:
#     print ("Switch name:")
#     print (s)
#     print ("")



# Step 2: Uncomment The following section, to find and print the number of entries in the list of switches. 
# Leave the section that sets the variable in the code for further use when finished. 
# comment out the print statement before moving on, but leave the entries variable set to proceed. 

entries = len(switches)
#print (entries)


# Step 3: Uncomment The following section, and re-run the script to build a dictionary of dictionaries using a while loop to iterate over information from these lists 
# Note: This is NOT the only way to do this, and may not even be the most efficient way.
# Comment out the print statements once you have confirmed your dictionary is being created properly

devices = {}
while entries > 0:
    print ("Number of devices left to process: " + str(entries))
    switch = switches[entries - 1]
    entry = {'mgmt_ip': mgmt_ip_addresses[(entries - 1)], 'interface_ip': int_addresses[(entries - 1)], 'vlan' : vlans[(entries - 1)]}
    devices[switch] = entry
    entries = (entries - 1)
#print (devices)


# Step 4: Uncomment the follwing line to extract the nested dictionary info using the key, which is the switch name. Recomment that line when finished

#print (devices['spine01'])


#Step 5: Uncomment the following lines to iterate though the parent dictionary and list each device (key) and all of the key/value pairs in the nested dictionary for each device entry.  

for switch, sw_info in devices.items():
    print ("Device Name: ", switch)
    for key in sw_info:
        print (key + " : ", sw_info[key])
    print ()



#Questions for review:
# What was the purpose of using the variable "entries = len(switches)" rather than just putting the number 6 in the script?" 
# When getting data out of the lists why is the "entries - 1" used as the value?
## Bonus Question: How would you approach modifying this script to prompt a user to enter a device name, then return the information only for that device?

if __name__ == "__main__":
    while True:
        try:
            print ()
            print ("What is the name of the switch to query?")
            x = input()
            for device, info in devices.items():
                if device == x:
                    print ()
                    print ("Device Name: ", device)
                    for key in info:
                        print (key + " : ", info[key])
                    print ()
            if x not in devices:
                print ()
                print ("Device entry not found.")
                print ()
            if x == 'quit':
                break
        except Exception as e:
            print(e)


