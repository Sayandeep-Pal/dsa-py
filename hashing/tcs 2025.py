'''Rock Sample Range Classification
Problem Statement 
Juan Marquinhos is a geologist and he needs to count rock samples to send them to a chemical laboratory. He receives rock samples one by one and must classify them according to the size ranges accepted by the laboratory. Given the sizes of rock samples and several laboratory ranges, determine how many samples fall within each range. Topic Tags Array, Hash Map, Range Counting 

Constraints  10<S<10000  1<R<1000000  1≤sample size≤1000 

Example 1 
Input
10 2 
345 604 321 433 704 470 808 718 517 811 
300 350 
400 700 

Output 2 4 
Explanation
 Range 300–350 → 345, 321 → 2 samples Range 400–700 → 604, 433, 470, 517 → 4 samples 
 
Example 2 
Input
20 3
921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
1 100
50 600 
1 1000 
Output 1 12 20 
Explanation Each range counts the number of samples whose values fall within that range.'''



size, n = map(int, input().split())

arr = list(map(int, input().split()))

hash = {}

ranges = []

for i in range(n):
    l, h = map(int, input().split())
    ranges.append([l,h])

res = []

for j in ranges:
    r =0
    for i in arr:
        if j[0] <= i <=j[1]:
            r+=1
    res.append(r)

print(res)