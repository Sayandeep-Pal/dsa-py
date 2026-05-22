n = int(input())
binary = format(n, 'b')

res = ''
for i in binary:
    if i == '1':
        res+='0'
    else:
        res+='1'

res = int(res, 2)
print(res)