#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfc = dir()
    for i in range(0, len(allfc)):
        if allfc[i][:2] != "__":
            print("{:s}".format(allfc[i]))
