from random import randint
vals = [randint(-100,100) for i in range(30)]
print("\n Starter list: \n", vals)

mNum = max(vals)
pos = vals.index(mNum)

print("\n Max element of the list:", mNum, "\n Max element position:", pos)
print("\n Pairs of negative numbers:")

for i in range(len(vals)-1):
    print(vals[i],vals[i+1])if vals[i]<0 and vals[i+1]<0 else None
