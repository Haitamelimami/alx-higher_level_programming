#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    suminit = 0
    for i in range(1, len(argv)):
        suminit += int(argv[i])
    print("{}".format(suminit))
