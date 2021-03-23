import subprocess
subprocess.call("sudo ifconfig eth0 down",shell=True)
subprocess.call("sudo ifconfig eth0 hw ether 00:11:22:33:33:55",shell=True)
subprocess.call("sudo ifconfig eth0 up",shell=True)
print("the operation is done")