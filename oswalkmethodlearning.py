import os

palist = __file__.split("\\")
print(palist)
prim = ("\\".join(palist[:2])) + "\\"
# print(list(os.walk(prim)))

def alldirparsing():
    for root, dirs, files in os.walk(prim):
        for dir in dirs:
            if dir == "":
                continue
            else:
                print(dir, end="---------")
            print(root)

# print(help(os.walk))
# alldirparsing()

def scaledirparsing(level=None):
    global prim
    if level != None:
        directoryy = level.split(",")
        print(directoryy)
        dirpath = ("\\".join(directoryy)) + "\\"
        prim = os.path.join(prim, dirpath)
        print(prim)
    for i in os.scandir(prim):
        if not os.path.isdir(i):
            continue
        print(i)
    print(prim)

location = input("Where would you like to search? Seperate directories with commas instead of spaces: ")

scaledirparsing(location)