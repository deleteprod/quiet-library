#!/usr/bin/env python3

import os
import sys

# Hardware related collection requirements to begin with

def get_cpu_info():
    '''
    Core count (physical)
    Core count (Hyperthreading)
    Load average
    CPU speed
    CPU type and name
    proc/cpuinfo
    '''
    pass

def get memory_info():
    '''
    Total capacity
    Current usage
    Large resident programmes
    Memory pressure over time
    '''
    pass

def get_disk_info():
    '''
    List of disks
    File systems
    Mount points
    Capacity
    '''
    pass

def get_network_info():
    '''
    Interfaces, speeds, routes, nameservers, DHCP/static IP.
    ''''

# OS and software collection requirements next

def get_process_info():
    ''' 
    ps -eaf
    '''
    pass

def get_services():
    '''
    systemctl list-unit-files | grep (enabled~running)
    pass
    ''''

def get_user_list():
    '''
    cat /etd/passwd
    List of users allowed interactive logins
    List of users by groups
    Lastlog info
    groups users are in (can anyone become root through wheel?)
    '''
    pass

def get_system_problems():
    # Read in /var/log/messages and look for WARN and ERROR
    pass

