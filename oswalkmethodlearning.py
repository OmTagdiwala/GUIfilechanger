import os

palist = __file__.split("\\")
print(palist)
prim = "\\".join(palist[:2])
# print(list(os.walk(prim)))

def dirparsing():
    for root, dirs, files in os.walk(prim):
        for dir in dirs:
            if dir == "":
                continue
            else:
                print(dir)

dirparsing()