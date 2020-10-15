#!/usr/bin/env python3


"""

A simple script to invoke RTL8188eus driver.
Tested on Tp Link wn722n 2.4GHz 150Mbps WiFi adapter

"""
import subprocess
import time
import re
import random

class col:
	HEADER = '\033[95m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	Black = '\u001b[30m'
	Red = '\u001b[31m'
	Green = '\u001b[32m'
	Yellow = '\u001b[33m'
	Blue = '\u001b[34m'
	Magenta = '\u001b[35m'
	Cyan = '\u001b[36m'
	White = '\u001b[37m'



__author__ = "nikhildr22"
interface = "wlan0"

def get_random_mac():
	even_chars = ['2','4','6','8','A','C','E']
	chars = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	mac = random.choice(chars) + random.choice(even_chars) + ':'
	for i in range(10):
		mac = mac + random.choice(chars)
		if i != 9 and i%2 != 0:
			mac += ':'
	return mac


def change_mac_address(interface):
	mac_address = get_random_mac()
	print("")
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
	subprocess.call(["ifconfig",interface,"up"])

	print(f"[+] Changing Mac Address of Interface {interface} to {mac_address}")

if __name__=="__main__":
	pointer = f"{col.Red}[+]{col.ENDC} "
	print(f"{pointer}{col.WARNING}MAKE SURE WiFi ADAPTER IS NOT INSERTED{col.ENDC}")
	input(f"{pointer}{col.Blue}Press ENTER to continue....{col.ENDC}")
	subprocess.call(["sudo", "modprobe", "8188eu"])
	subprocess.call(["sudo", "exit"])
	print(f"{pointer}{col.Green}Successfully activated the WiFi Driver RTL8188eus{col.ENDC}")
	print(f"{pointer}{col.Red}Now, Insert the adapter")
	input(f"{pointer}{col.Blue}Press ENTER to continue....{col.ENDC}")
	change_mac_address(interface)
	subprocess.call(["ifconfig", "wlan0"])
	exit()




