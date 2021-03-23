import subprocess
subprocess.call("sudo ifconfig enp2s0 up",shell=True)
print("the operation is done")