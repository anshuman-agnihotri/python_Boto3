import sys
type = sys.argv[1]

if type == "t2.micro":
    print ("this is the basic instance")
elif type == "t3.micro":
    print ("this instance is more valuable")
else:
    print("this is the wrong data")
