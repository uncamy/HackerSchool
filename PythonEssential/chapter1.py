#File input and output
f = open("foo.txt")
line = f.readline()
while line:
    print line,
    line = f.readline()
f.close() 

# a better version
for line in open("foo.txt"):
    print line

principal = 1000
rate = 0.05
numyears = 5
year = 1

f = open("out", "w") # opens file for writing 
while year <= numyears:
    principal = principal * (1+ rate)
    print >>f, "%3d %0.2f" % (year, principal)
    year +=1
f.close()




