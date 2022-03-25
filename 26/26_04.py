inf = open('26_04.txt')
l = [i for i in inf]
n, s = list(map(int, l[0].split()))
del l[0]
l = [int(i) for i in l]
video, img = [], []
for i in l:
    if i>90:
        video.append(i)
    else:
        img.append(i)
video.sort()
img.sort()
s1 = 0
cnt = 0
for i in video:
    if s1 < s/2:
        s1 += i
        cnt += 1
    else:
        print(i)
        break
s = s-s1
for i in img:
    if s - i >= 0:
        cnt += 1
        s -= i
    else:
        print(i)
        break
print(set(img))
print(set(video))
print(s, cnt)