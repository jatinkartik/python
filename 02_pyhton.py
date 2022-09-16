# #!/usr/bin/env python2
# from playsound import playsound
# # /home/jatintyagi/Downloads/faded.mp3 ---> path to file
# print("songs start")
# playsound('/home/jatintyagi/Desktop/python/faded.mp3')
# print("songs ends")



import optparse
import subprocess

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="interface of the network")
parser.add_option("-m","--new_mac",dest="new_mac",help="new mac address")
(options,interface) = parser.parse_args()

subprocess.call("sudo ifconfig", "eth0", "down",shell=True)
# subprocess.call("pwd",shell=True)
subprocess.call("sudo ifconfig", "eth0", "hw", "ether","00:11:33:44:55:55",shell=True)
subprocess.call("sudo ifconfig", "eth0", "up",shell=True)

