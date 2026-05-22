# ## Method 1
# arr = list(map(int, input().split()))

# s=0

# for i in range(len(arr)):
#     if arr[i] !=0:
#         arr[s] = arr[i]
#         s+=1

# for i in range(s,len(arr)):
#     arr[i] = 0

# print(arr)


#Method 2
arr = list(map(int, input().split()))

s=0

for i in range(len(arr)):
    if arr[i] !=0:
        arr[s], arr[i] = arr[i], arr[s]
        s+=1

print(arr)
