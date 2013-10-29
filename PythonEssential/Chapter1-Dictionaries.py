# this is a dictionary or hash table
stock = {
    "name"   : "GOOG",
    "shares" : 100,
    "price"  : 490.10
}

name = stock['shares']
print name 

value = stock['shares'] * stock['price']
print value

stock['shares'] = 75
value = stock['shares'] * stock['price'] 
print value
    
stock['date'] = 'October 11, 2013'
print stock['date']

prices = {
    'GOOG' : 490,
    'AAPL' : 123,
    'IBM'  : 92,
    'MSFT' : 52
}

p = prices.get('GOOG', 0.0)
print p

syms = list(prices)
print syms
del prices["MSFT"]

syms = list(prices)
print syms

#generators
def countdown(n):
    print "Counting down"
    while n> 0:
        yield n
        n-=1
c= countdown(10)

for i in c:
    print i,

#corountines
def print_matches(matchtext): 
    print "Looking for " , matchtext
    while True:
        line = (yield) #get line of text
        if matchtext in line:
            print line
matcher = print_matches('python')
matcher = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython")
]
for m in matcher: m.next()

#let's make a stack
class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)

# alt methods
class Stack(list):
    def push(self, object):
        self.append(object)

y= Stack(list)


# exceptions
try: 
    f= open("foo.txt", "r")
except IOError as e:
    print e

