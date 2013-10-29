import sys # load sys module

# check command line arguments
if len(sys.argv) != 2: 
    print "please supply a filename"
    raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
f.close()

#convert input from strings to floats
fvalues = [float(line) for line in lines]

print "the min value is " , min(fvalues)
print "the max value is " , max(fvalues)

