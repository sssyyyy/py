import sys
fr=open(sys.argv[1],'r')
data=fr.read()
fr.close()
fw=open(sys.argv[2],'w')
fw.write(data)
fw.close()