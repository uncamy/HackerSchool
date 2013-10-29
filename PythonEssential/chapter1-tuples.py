# tuples- note that the () are not neceessary 
stock = ('goog', 100, 490.10)
address = ('www.python.org', 80)
person = 'amy', 'roberts', '3364034111'

# unpack a tuple
name, share, price = stock
host, port = address
first_name, last_name, phone = person

print name
print port
# tuples are immutable and therefore take up less memory than lists

filename = 'portfolio.csv'
portfolio = []
for line in open(filename):
    fields = line.split(',')
    name = fields[]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name, shares, price)
    portfolio.append(stock)



