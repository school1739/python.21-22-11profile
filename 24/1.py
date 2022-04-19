'''with open('24_demo.txt') as f:
    s = f.readline()'''

s = 'AXXBXXXCXXXXG'
k = 1
kmax = 1
for i in range(1,len(s)):
    if s[i] == s[i-1] == 'X':
        k += 1
        kmax = max(kmax,k)
    else:
        k=1
print(kmax)
