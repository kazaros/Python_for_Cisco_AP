#!/usr/bin/python
from netmiko import ConnectHandler
import time


device1 = { 
    'device_type': 'cisco_ios',
    'ip': 'X.X.X.X',
    'username': 'XXXXX',
    'password': 'XXXXXX',
#     global_delay_factor=2,
     'secret': 'XXXXXX',
}

device2 = { 
    'device_type': 'cisco_ios',
    'ip': 'X.X.X.X',
    'username': 'XXXXX',
    'password': 'XXXXXX',
#     global_delay_factor=2,
     'secret': 'XXXXXX',
}

all_devices = [device1,device2,device3,device4,device5]


for device in all_devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    prompt = net_connect.find_prompt()
    net_connect.send_command('reload reason test', expect_string='[confirm]')
    time.sleep(2)
    net_connect.send_command_timing("y")
    print("--------- End ---------")
