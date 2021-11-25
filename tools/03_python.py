import os
dir = '/home/jatintyagi/Downloads/'
print(os.listdir(dir))
count = 0
def filepath(dir):
    global count
    for path in os.listdir(dir):
        childPath = os.path.join(dir,path)
        if os.path.isdir(childPath):
            filepath(childPath)
        else:
            count += 1
            print(childPath)
    print(count)
filepath(dir)