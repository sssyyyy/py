import sys
f=open(sys.argv[1],'r')
data=f.read()
print("# of lines: ",len(data.split("\n")))
print("# of words: ",len(data.split()))