counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    # if name not in counts:
    #     counts[name] = 1
    # else:
    #     counts[name] = counts[name] + 1
    counts[name] = counts.get(name, 0) + 1 # replaces if/else above
print(counts)

def getName(n, num):
    return n,counts.get(n, num) # get searches dict for key (n) and returns default value (num) if key not found

a,b = getName('csev', 0)
print(a,':',b)
print(getName('cwen', 0))
print(getName('kris', 0))

