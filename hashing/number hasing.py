n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash ={}

for i in n:
    hash[i] = hash.get(i,0)+1

print(hash)

for i in m:
    print(hash.get(i,0))