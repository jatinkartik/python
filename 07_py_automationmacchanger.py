import subprocess
# x = input("enter the vlaue of mac")
interface = input("Interface >")
vl = input("New MAC >")
print("[+] changing the mac for "+interface+" to "+vl)
subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("sudo ifconfig "+interface+" hw ether "+vl+" ",shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)