import subprocess as sb
import optparse

# x = input("enter the vlaue of mac")
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change macAddress")
    parser.add_option("-m","--mac",dest="vl",help="New_mac address")
    return parser.parse_args()
# interface = input("Interface >")
# vl = input("New MAC >")
def mac_changer(x,y):
    print("[+] changing the mac for "+options.interface+" to "+options.vl)
    sb.call( [" ifconfig "+options.interface+" down" ],shell=True)
    sb.call( [" sudo ifconfig "+options.interface+" hw ether "+options.vl ],shell=True)
    sb.call( [" ifconfig "+options.interface+" up " ],shell=True)
(options,arguments) = get_arguments()
print(options.interface)
mac_changer(options.vl,options.interface)
# subprocess.call(" ifconfig "+interface+" down" ,shell=True)
# subprocess.call(" sudo ifconfig "+interface+" hw ether "+vl ,shell=True)
# subprocess.call(" ifconfig "+interface+" up " ,shell=True)
# subprocess.call(["ls", "-l"])
# subprocess.call(["echo", " jatinkartiktyagi  jatin", ">", "jatin"])