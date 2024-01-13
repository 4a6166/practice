import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

#define DataFrame
df = pd.DataFrame({
    'points': [25, 12, 15, 14, 19, 23, 25, 29],
    'assists': [5,7,7,9,12,9,9,4],
    'rebounds': [11,8,10,6,7,5,8,6]
    })

print(df)

try:
    print(int('should fail'))
except:
    print('failed like it should')

def howToDefineAFunction(a,b):
    try:
        return a/b
    except:
        return 'inputs need to be numbers'

print(howToDefineAFunction("a","b"))
print(howToDefineAFunction(1,2))

print("+" + "concats" + "strings")
print("," , "concats" , "args to a string in print func")

def whileNoBreak():
    n = 0
    while n < 3:

        n += 1

    return n

def whileBreak():
    n = 0
    while True:
        if n == 3:
            break
        n += 1
    return n

print( "whileNoBreak == whileBreak", whileNoBreak() == whileBreak() )

for i in [2,1,5]:
    print(i)

arr = ["a", "b", "c"]
for i in arr:
    print(i)

smallest = None
print("Before:", smallest)
for itervar in [41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        # break # this will break out of loop at first iteration
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

print ( 1 is "1") # false

print( "bananas".find("na"), "== 2") # zero index
print( "bananas"[2:4]) # "na"; slice upto but not including 4
print( "bananas"[1:], "== pineapple") # "ananas"
