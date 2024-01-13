fhand = open('mbox-short.txt', 'r') # fhand == file handle, mode w == write, r == read
# fhand = open('mbox-short.txt') # mode is not essential

print(fhand)

# count = 0
# for line in fhand:
#     count += 1 # No increment or decrement operators in Python
#     # print(line) # print each line in the file
# print(count)

# count2 = 0
# for line in fhand:
#     count2 += 1
# print(count2) # => 0, file gets garbage collected after first read

# fhand = open('mbox-short.txt')
# first20 = fhand.read() # read() reads entire file into a string
first20 = ""
ctr = 0
for line in fhand:
    if line.startswith('From:'):
    # if not '@utc.ac.za' in line: # prints out lines without '@utc.ac.za'
        first20 += str(ctr) + ": "
        # first20 += line.restrip() # strips white space from right (like the \n)
        first20 += line
        ctr += 1
    if ctr == 20:
        break

print(first20)

## inputs

fileNotOpened = True
fname =None
fhand = None
while fileNotOpened:
    fname = input('Enter file name: ') # input does not work on vim console
    try:
        fhand = open(fname)
        fileNotOpened = False
    except:
        print('File cannot be opened:', fname)

ctr = 0
lNumber = 0
for line in fhand:
    if 'From:' in line: # no wildcards, it looks like
        print(str(ctr)+": ", "Line "+str(lNumber),line)
        ctr += 1
    lNumber += 1
print('Done')






