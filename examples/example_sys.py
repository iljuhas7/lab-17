import sys

print("count argv: ", len(sys.argv), sep="")

if len(sys.argv[0]):
    print("sys.argv[0] = \"", sys.argv[0], "\";", sep="")

if len(sys.argv[1:]):
    for ind, curarg in enumerate(sys.argv[1:]):
        print("sys.argv[", ind + 1, "] = \"", curarg, "\";", sep="")
        
else:
    print("Null argument")


