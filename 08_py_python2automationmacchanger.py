 # #!/usr/bin/env python2

import subprocess
# x = input("enter the vlaue of mac")
interface = "eth0"
vl = raw_input("enter the value of mac address")
# print("[+] changing the mac for "+interface+" to "+vl)
subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("sudo ifconfig "+interface+" hw ether "+vl+" ",shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)