#!/usr/bin/env python

import subprocess as sb
import optparse
import re
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
       parser.error("[-] please specify an interface, use --help for more info.")
    elif not options.new_mac:
       parser.error("[-] Please specify an interface, use --help for more info.")
    return options
def change_mac(interface, new_mac):
    print("[+] Changing Mac address for " + interface + " to " + new_mac)
    sb.call(["ifconfig ", interface, "down"])
    sb.call(["ifconfig ", interface, "hw ether", new_mac])
    sb.call(["ifconfig ", interface, "up"])
    print("[*] Mac Address has been Changed to " + new_mac)

options = get_argument()
# change_mac(options.interface, options.new_mac)

ifconfig_result = sb.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ifconfig_result)

if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[-] Could not read MAC Address.")