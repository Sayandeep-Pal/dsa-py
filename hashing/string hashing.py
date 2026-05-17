s="azyxyyzaaaa"
q=['d','a','y','x']

hash={}

for i in s:
    if i in hash.keys():
        hash[i] +=1
    else:
        hash[i] = 0

print(hash)

for i in q:
    if i in hash.keys():
        print(hash[i])
    else:
        print(0)