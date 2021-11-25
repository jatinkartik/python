import subprocess
import optparse

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface of the network")
    parse.add_option("-m","--new_mac",dest="new_mac",help="new mac address")
    return parse.parse_args()
def change_mac(new_mac,interface):
    print("[+] changing mac to ",new_mac)
    subprocess.call(["sudo ifconfig "+options.interface+" down"],shell=True)
    subprocess.call(["sudo ifconfig "+options.interface+" hw ether "+options.new_mac],shell=True)
    subprocess.call(["sudo ifconfig "+options.interface+" up"],shell=True)
(options,interface) = get_arguments()
change_mac(options.new_mac,options.interface)






















# import subprocess
# import optparse

# parser = optparse.OptionParser()
# parser.add_option("-i","--interface",dest="interface",help="interface of the change mac")
# parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
# (options,arguments) = parser.parse_args()

# print("[+] changing the mac for "+options.interface+" to "+options.vl)
# subprocess.call( [" ifconfig "+options.interface+" down" ],shell=True)
# subprocess.call( [" sudo ifconfig "+options.interface+" hw ether "+options.vl ],shell=True)
# subprocess.call( [" ifconfig "+options.interface+" up " ],shell=True)