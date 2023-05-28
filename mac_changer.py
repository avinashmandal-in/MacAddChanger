#                                    !! Welcome to MAC Changer !!
#
#                         -------------------------------------------------
#                         | --------------------------------------------- |
#                         | | Created & CopyRighted by Avinash Mandal   | |
#                         | | Github:- www.github.com/AvinashMandal-in  | |
#                         | --------------------------------------------- |
#                         -------------------------------------------------

# !/usr/bin/env python

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


def get_current_mac(interface):
    ifconfig_result = sb.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")


options = get_argument()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was Successfully Changed to " + current_mac + '.')
    print("Thank you for using MAC Changer Tool by Avinash Mandal.")
else:
    print("[-] MAC Address didn't get Changed.")


